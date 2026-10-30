import datetime as dt
import tempfile
import unittest
from pathlib import Path

from kb_check import check

TODAY = dt.date(2026, 10, 30)
TOPIC = "---\nupdated: 2026-10-01\n---\n- a -> b\n"


class KbCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("_index.md", "- [[one]] - x\n- [sub/](sub/_index.md) - y\n")
        self.write("one.md", TOPIC + "\nSee: [[two]]\n")
        self.write("sub/_index.md", "- [[two]] - z\n")
        self.write("sub/two.md", TOPIC)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def errors(self, needle):
        errors, _, _ = check(self.root, TODAY)
        self.assertTrue(any(needle in e for e in errors), errors)

    def test_valid_tree(self):
        errors, stale, n = check(self.root, TODAY)
        self.assertEqual((errors, stale, n), ([], [], 2))

    def test_broken_link_after_delete(self):
        self.write("one.md", TOPIC + "\nSee: [[gone]]\n")
        self.errors("broken link [[gone]]")

    def test_quoted_shell_syntax_is_no_link(self):
        self.write("one.md", TOPIC + "- use [[ $a == b ]] and [[cut:n]] and [[/A]]\n")
        self.assertEqual(check(self.root, TODAY)[0], [])

    def test_link_survives_move(self):
        (self.root / "sub/two.md").rename(self.root / "two.md")
        self.write("_index.md", "- [[one]] - x\n- [[two]] - t\n- [sub/](sub/_index.md) - y\n")
        self.write("sub/_index.md", "")
        self.assertEqual(check(self.root, TODAY)[0], [])

    def test_unlisted_topic(self):
        self.write("three.md", TOPIC)
        self.errors("topic file three not listed")

    def test_index_lists_missing_topic(self):
        self.write("sub/_index.md", "- [[two]] - z\n- [[ghost]] - g\n")
        self.errors("lists missing topic file ghost")

    def test_unlisted_folder_and_missing_index(self):
        self.write("new/four.md", TOPIC)
        self.errors("folder new/ not listed")
        self.errors("new: missing _index.md")

    def test_duplicate_slug(self):
        self.write("sub/one.md", TOPIC)
        self.errors("duplicate slug one")

    def test_bullet_limit(self):
        self.write("one.md", "---\nupdated: 2026-10-01\n---\n" + "- x\n" * 31)
        self.errors("31 bullets")

    def test_exactly_at_limits_is_fine(self):
        self.write("one.md", "---\nupdated: 2026-10-01\n---\n" + "- x\n" * 30)
        self.assertEqual(check(self.root, TODAY)[0], [])

    def test_entry_limit(self):
        names = [f"n{i}" for i in range(31)]
        self.write("sub/_index.md", "".join(f"- [[{n}]] - d\n" for n in names))
        for n in names:
            self.write(f"sub/{n}.md", TOPIC)
        self.errors("31 entries")

    def test_entry_word_limit(self):
        self.write("sub/_index.md", "- [[two]] - " + "word " * 30 + "\n")
        self.errors("over 25 words")

    def test_missing_and_bad_date(self):
        self.write("one.md", "- no frontmatter\n")
        self.errors("no updated date")
        self.write("one.md", "---\nupdated: soon\n---\n- x\n")
        self.errors("invalid updated date")
        self.write("one.md", "---\nupdated: 2030-01-01\n---\n- x\n")
        self.errors("future")

    def test_stale_is_reported_not_error(self):
        self.write("one.md", "---\nupdated: 2020-01-01\n---\n- x\n")
        errors, stale, _ = check(self.root, TODAY, stale_days=365)
        self.assertEqual(errors, [])
        self.assertEqual(len(stale), 1)

    def test_invalid_slug(self):
        self.write("Bad_Name.md", TOPIC)
        self.write("_index.md", "- [[one]] - x\n- [[Bad_Name]] - b\n- [sub/](sub/_index.md) - y\n")
        self.errors("invalid slug")

    def test_reference_file_present_and_assets_not_indexed(self):
        self.write(".assets/grid.png", "x")
        self.write("one.md", TOPIC + "- ref image .assets/grid.png -> tight grid\n- ref website https://a.at -> nav\n")
        self.assertEqual(check(self.root, TODAY)[0], [])

    def test_missing_reference_file(self):
        self.write("one.md", TOPIC + "- ref audio .assets/gone.mp3 -> intro\n")
        self.errors("missing reference file .assets/gone.mp3")

    def test_crlf_files(self):
        self.write("one.md", TOPIC.replace("\n", "\r\n"))
        self.assertEqual(check(self.root, TODAY)[0], [])


if __name__ == "__main__":
    unittest.main()
