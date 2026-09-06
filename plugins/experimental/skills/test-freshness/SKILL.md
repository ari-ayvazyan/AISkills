---
name: test-freshness
description: Audit tests that pass despite broken behavior, stale mocks, or changed interfaces in any repository. Use when reviewing test validity or proposing SHA-256 freshness guards; not for routine test execution or CI configuration.
---

# Test contract freshness

Determine whether passing tests still verify the intended behavior. Apply this workflow across languages, frameworks and repository layouts, especially where tests replace a dependency with a mock, fake, generated fixture or saved response.

Start with the repository's instructions, supported environment and existing test commands. Locate the affected implementation and its consumers rather than assuming file paths, build tools, deployment model or a particular agent harness. For broader reproduction or flaky-test work, reuse an existing regression-testing workflow when available; this skill focuses on stale expectations, component contracts and fingerprint limits.

## Trace the behavior and its test oracle

Build a small evidence map: intended behavior, implementation or producer, consuming code, test double or fixture, assertion, and a defect that assertion should detect. Derive expected behavior from requirements or a reviewed contract, not solely from the current implementation.

For example, a service returns `account_id`, but its client test still supplies a hand-written `id` field. The unit test passes while the real client cannot parse the service response. A test hashing only its own file cannot detect this drift. Similar failures occur in library adapters, command-line wrappers, event handlers, database mappings and file-format readers.

- Compare test doubles with the current real interface, serialized data and relevant semantics. Check defaults, errors, field presence, value meaning, ordering, state transitions and side effects where they matter.
- Exercise the actual consuming code against the real producer on a small synthetic fixture. If the producer cannot run locally, use an authorized provider-verification environment or versioned producer evidence and state the remaining integration gap. Do not silently substitute another mock and call the integration verified.
- Keep mocks for focused branch tests, but verify their contract against the real dependency. Generated schemas and fixtures reduce duplication; they do not independently establish correctness.
- Cover the specific successful path, meaningful failure and sequence involved in the defect. Two components agreeing on the same wrong behavior is still wrong; assert domain invariants and effects separately from message compatibility.
- Add property-based or metamorphic checks when a requirement justifies the property or relation. A serializer/deserializer round trip, for example, can pass when both share a defect; pair it with an independent expected representation where interoperability matters.

## Demonstrate that the tests detect defects

For a reproduced defect or a high-risk test-validity review, run the targeted test against a known-bad implementation or deliberate mutation and confirm failure for the expected behavioral reason. Run the positive control against the intended implementation.

Use an isolated copy, worktree or equivalent supported by the environment. Preserve existing work. A compilation error, missing dependency, timeout unrelated to the intended failure, or unrelated red test does not establish that the regression was detected.

Keep fingerprint checks separate from this experiment: changing a source hash on every mutation must not count as a behavioral assertion killing the mutant. Review surviving, uncovered and behaviorally equivalent mutations rather than imposing an unexplained universal mutation score. Scale the audit to the affected risk; routine harmless edits do not require mutation testing.

## Use fingerprints as bounded freshness evidence

SHA-256 detects differences in the bytes supplied to it. It does not establish correct behavior or the quality of a test oracle.

| Target | Useful signal | Limitation |
| --- | --- | --- |
| Test file | Test code changed | Production and dependency changes can remain invisible |
| Declared source inputs | Previously reviewed inputs changed | Harmless edits also trigger; omitted dependencies are invisible |
| Canonical interface schema | Contract shape changed | Wrong values, effects or transitions may preserve the schema |
| Reviewed output samples | Selected results changed | Uncovered inputs and an incorrect original baseline remain undetected |
| Verification inputs and result evidence | A result belongs to specified inputs | Input completeness and oracle correctness still need review |

First consider whether existing version control, contract tests and test selection already address the problem. Prefer a narrow optional freshness manifest for a fragile boundary over a mandatory hash for every test. Loading this skill does not authorize introducing a new gate.

When a fingerprint gate is justified and implementation is requested:

1. Define the boundary and its intended behavior. Record the relevant implementation, consumers, schema, tests, synthetic fixtures, and behavior-affecting dependency, configuration and toolchain identities. Make omissions explicit.
2. Use a deterministic, versioned representation. Preserve meaningful field distinctions and ordering. Keep the expected baseline separate from current computation; exclude the baseline's own digest from its inputs. Check that inputs did not change during verification.
3. Retain readable expected values or diffs alongside hashes. Control nondeterminism and normalize only data demonstrated irrelevant to the contract.
4. On mismatch, report that freshness review is required and identify changed inputs. Review semantics and run appropriate behavioral checks before updating an intentional baseline change. Never regenerate expectations merely to restore green.
5. Treat a match as evidence of unchanged declared inputs or samples only. It does not waive required tests, establish correctness, or prove compatibility with an untested environment.

A hash is not an authorization decision or proof of trusted provenance. Preserve the project's existing access controls and evidence policies.

## Verify and report

Use the repository's own supported tools and verification commands within the available execution permissions. Keep fixtures synthetic and deterministic; do not copy credentials or sensitive production data into tests. Store artifacts and learning notes according to the project's policy.

Report the violated requirement, real boundary exercised, negative and positive controls, any fingerprint's scope and baseline rationale, exact checks run and remaining gaps. Distinguish code failures from environment blockers. Source tests do not prove a deployed application or an external service runs the tested version.

Review neighboring doubles when evidence suggests similar drift; do not turn one defect into an unsolicited repository-wide audit.

## Research basis

These sources explain the principles; they do not mandate a framework or dependency:

- [NIST FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final): message digests detect changes.
- [Pact consumer tests](https://docs.pact.io/consumer) and [contract versus functional tests](https://docs.pact.io/consumer/contract_tests_not_functional_tests): verify real participants' message agreement and test business effects separately.
- [Jest snapshots](https://jestjs.io/docs/snapshot-testing): review expected outputs and control nondeterminism.
- [Stryker mutant states](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/): distinguish detected, surviving, uncovered and invalid mutations.
- [Bazel remote caching](https://bazel.build/remote/caching): reuse depends on declared inputs and environment; omitted tools can invalidate assumptions.