---
name: image-gen-edit-agy
description: Generate or modify an image with ai by using agy
---

# Generating images with Antigravity

Claude Code has no image generation tool of its own. Images are produced by shelling out to
the Antigravity CLI (`agy`), which has a `generate_image` skill. You write the prompt, `agy`
runs the generation, and reports back the absolute path of the file it wrote.

## The call

Run `agy` in print mode with one self-contained instruction:

```bash
agy -p "Use your image generation skill to generate an image.
Prompt: <the full description>
ImageName: <lowercase_underscored_name>
AspectRatio: <one of 1:1 2:3 3:2 3:4 4:3 9:16 16:9>
Save it to <absolute/target/path.png> and report the full absolute path of the written file back to me."
```

Always state the target filename **and** ask for the full path back — `agy` otherwise saves into
its own artifact directory and you will not know where the file landed.

## Parameters of `generate_image`

| Parameter | Required | Meaning |
| --------- | -------- | ------- |
| `Prompt` | yes | Text describing what to generate, or the edit instruction when editing an existing image. |
| `ImageName` | yes | Filename prefix for the saved artifact. All lowercase with underscores, descriptive, **max 3 words** (`grass_tile`, `pine_sprite`, `login_page_mockup`). |
| `AspectRatio` | no | Defaults to `1:1`. One of `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`, `16:9`. |
| `ImagePaths` | no | Array of paths to input images — supply these to **edit** or use existing art as reference instead of generating from scratch. |

There is no arbitrary pixel-size parameter: choose the aspect ratio, then downscale to the
target dimensions yourself if this is needed (`sharp`).

## Editing an existing asset

Pass the current file through `ImagePaths` and make `Prompt` the edit instruction:

```bash
agy -p "Use your image generation skill to edit an image.
ImagePaths: <full_escaped_path>
Prompt: Darken the needle canopy and remove the ground shadow, keep the silhouette identical.
ImageName: <full_escaped_path>.png
Report the full absolute path of the written file back to me."
```

Isolated crops and field stamps cannot pass a round.

## Useful `agy` flags

- `-p` / `--print` — single non-interactive prompt (what you want here).
- `--print-timeout 10m` — raise the wait for slow generations.
- `--output-format json` — machine-readable result if you want to parse the path out.
