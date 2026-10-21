# CampusFlow Next — Baseline and Regression Check

## 1. Purpose

This document records the baseline evidence available for CampusFlow and
the checks used to assess whether CampusFlow Next preserves existing
behaviour while adding new features.

A passing current test suite is regression evidence. It does not, by
itself, establish what passed before development began.

## 2. Team and project history

### Original CampusFlow

- Engineer A: Bashir Hassan.
- Engineer B: Timothy Yusuf.

### Current CampusFlow Next

- Engineer A: Timothy Yusuf.
- Engineer B: Fredrick Ogbodo.

Historical contributions retain their original authorship.

## 3. Repository and checked revision

- Repository: https://github.com/Timstrings/campusNext-team
- Branch checked: To be recorded.
- Full commit SHA of application revision checked: To be recorded.
- Date checked: To be recorded.
- Python version: To be recorded.
- Checked by: To be recorded.

The SHA above identifies the application revision tested. A later
documentation-only commit may contain this completed report.

## 4. Original baseline evidence

- Original pre-sprint commit SHA: Not yet recorded.
- Original pre-sprint test command: Not yet recorded.
- Original pre-sprint test result: Not yet recorded.
- Original CLI behaviour checked: Not yet recorded.

### Limitation

The evidence assembled for this document does not currently establish a
complete pre-sprint baseline.

Do not treat a later test run as evidence that the original version
passed the same tests. If the original revision is checked retrospectively,
record its exact SHA, the date of that retrospective check, and its actual
results.

## 5. Previously recorded test result

An earlier user-shared terminal run reported:

    python3 -m unittest discover -s tests -v

    Ran 124 tests in 0.064s

    OK

The full commit SHA for that run was not recorded.

This is historical test evidence only. It does not prove that the latest
submitted revision passes.

## 6. Current automated regression check

Command:

    python3 -m unittest discover -s tests -v

Record the actual result:

- Application commit SHA tested: To be recorded.
- Date run: To be recorded.
- Tests run: To be recorded.
- Failures: To be recorded.
- Errors: To be recorded.
- Skips: To be recorded.
- Overall result: Pending.
- Evidence location or captured output: To be recorded.

## 7. Manual regression checks

Use test data, not sensitive personal information. Record actual outputs
rather than marking a feature as passing because its menu option exists.

| Check | Expected behaviour | Actual result / evidence | Status |
|---|---|---|---|
| Application startup | The interactive menu appears | Not yet recorded | Pending |
| Valid ticket creation | A ticket is created with an ID and calculated priority | Not yet recorded | Pending |
| Invalid ticket creation | Invalid input is rejected without creating a ticket | Not yet recorded | Pending |
| Ticket listing | Saved ticket fields are displayed | Not yet recorded | Pending |
| Assignment | A valid staff label is recorded | Not yet recorded | Pending |
| Start assigned ticket | A permitted move to `in_progress` succeeds | Not yet recorded | Pending |
| Start unassigned ticket | The action is rejected without changing ticket state | Not yet recorded | Pending |
| Resolution | A permitted move to `resolved` succeeds | Not yet recorded | Pending |
| Reopening | A resolved ticket can be reopened | Not yet recorded | Pending |
| Work queue | Unresolved tickets are ordered according to the implemented queue rules; resolved tickets are excluded | Not yet recorded | Pending |
| Reports | Counts agree with the known ticket data | Not yet recorded | Pending |
| Search | A known title query finds the expected ticket | Not yet recorded | Pending |
| Combined search filters | Results satisfy all selected filters | Not yet recorded | Pending |
| Add follow-up note | A valid note is accepted on an eligible ticket | Not yet recorded | Pending |
| View notes | The recorded note ID, author, and message are displayed | Not yet recorded | Pending |
| Save and restart | Tickets and notes remain available after restarting | Not yet recorded | Pending |
| Understanding check | Questions, scoring, and reflection recording behave as implemented | Not yet recorded | Pending |
| Invalid menu choice | The application displays an error and remains usable | Not yet recorded | Pending |

## 8. Storage and data-integrity checks

Record automated or manual evidence for:

- Rejection of malformed saved data.
- Rejection of duplicate ticket IDs.
- Rejection of duplicate note IDs.
- Ticket and note ID continuity after reload.
- Handling of older tickets without notes.

For any manual corrupt-data check, use an isolated test copy. Do not
overwrite the team's only working data file.

Results and evidence: Pending.

## 9. Defects and limitations

For each observed problem, record:

- Commit tested:
- Feature:
- Steps to reproduce:
- Input:
- Expected result:
- Actual result:
- Relevant file/function:
- Suggested retest:
- Retest result:

No claim is made here that the application is defect-free. Unperformed
checks remain pending.

## 10. Review.
- Timothy Yusuf — Engineer A: Pending.
- Fredrick Ogbodo — Engineer B: Pending.
- Review date: To be recorded.

## Integrity statement

This document separates historical evidence, current verification, and
missing checks.

Pending entries are not passing results. Complete this report using the
exact application revision tested and genuine observed evidence.