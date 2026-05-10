# Project Instructions

## WEDNESDAY: Complete Workflow Phases 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs
2. Phase 2. **Change Authorship** - update the project to your name and GitHub account
3. Phase 3. **Read & Understand** - review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Again, follow the instructions above to complete:

1. Phase 4. **Make a Technical Modification** - make a change and verify it still runs
2. Phase 5. **Apply the Skills to a New Problem**

## Topic

Foundations for streaming data projects.

This project introduces the basic project structure used throughout the course.

The example project:

- reads sales records from a local CSV file
- processes each record one at a time
- writes consumed records to a local output CSV file
- logs each step of the workflow

## Example Files

Review these files before making your changes:

| File                             | Purpose                            |
| -------------------------------- | ---------------------------------- |
| `src/streaming/consumer_case.py` | Reads and processes local messages |
| `src/streaming/core/utils.py`    | Provides shared project helpers    |
| `data/sales.csv`                 | Provides example input records     |

The example data starts in:

```text
data/sales.csv
```

NOTE: Consumers handle analytics, so our work focuses on them.
Producers can typically be used and copied with
few changes (just authorship) throughout the course,
unless you decide you want to work with a custom dataset
(which is always optional, and never required).

## Phase 4 Suggestions

Make a small technical change that does not break the script.
Choose any one of these (or a different modification as you like):

- Edit `.env` and change the number of messages created to 6-10 or more.

Be very careful when making changes.
Confirm the script still runs successfully after your change.

## Phase 5 Suggestions

Copy the consumer case file:

```text
src/streaming/consumer_case.py
```

Rename your copy:

```text
src/streaming/consumer_yourname.py

Then:

- Add the command you use to run your file to the README.md
- Share your observations about this example project.

## Key Skill Focus

As you work, focus on:

- the way streaming producers and consumers act independently
- how might a small business owner need more computers as business grows
- how can we keep important messages from "getting lost"
  hint: explore "replication"

Your goal is to make small changes and keep the project running.

## Professional Communication

Make sure the title and narrative reflect your work.
Verify key files:

- README.md
- docs/ (source and hosted on GitHub Pages)
- src/ (your renamed script)

Ensure your project clearly demonstrates:

- successful script execution
- output in the project.log
- newly streamed data file in `data/output`
