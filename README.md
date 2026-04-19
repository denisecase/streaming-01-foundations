# streaming-01-foundations

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: streaming foundations.

Data analytics requires a variety of skills.
This course builds capabilities through working projects.

In the age of generative AI, **durable skills** are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project introduces the basics of "data in motion",
data generated live, in real time,
and how we run analytics on it.

For example, when someone buys something online,
a record is typically created instantly that includes
what was bought, for how much, and where.

The message doesn't wait in a file.
It travels immediately to where it is needed.
This is **streaming data**: data in motion, arriving live, one event at a time.

This project simulates that experience.
We create a **producer** that generates a **simulated stream of sales messages**.
Each message is logged to the console as it arrives and saved to a CSV file.
After each new event, statistics are calculated the full set of sales messages.

In this project: run the producer, watch the sales arrive,
and see the numbers change live.

## Working Files

You'll work with just these areas:

- **docs/** - the project narrative and documentation
- **src/streaming/** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Producer executed successfully!
========================
```

A new file `project.log` will appear in the root project folder
and a new folder `data` will appear with the streaming messages.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/username/streaming-01-foundations

cd streaming-01-foundations
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files

# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# run the producer
uv run python -m streaming.producer_case

# do chores
uv run python -m ruff format .
uv run python -m ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "your message here"

# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>> or ...

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output

```shell
| INFO | P01 | ========================
| INFO | P01 | START main()
| INFO | P01 | ========================
| INFO | P01 | ROOT_DIR = .
| INFO | P01 | DATA_DIR = data
| INFO | P01 | OUTPUT_CSV = data\sales.csv
| INFO | P01 | Streaming 3 sales to C:\Repos\streaming\streaming-01-foundations\data\sales.csv ...
| INFO | P01 | Watch each sale arrive. Press CTRL+C to stop early.

| INFO | P01 | (1, 81.87, 'Backpack', 'East')
| INFO | P01 | Generated formatted multi-line SUMMARY string.
| INFO | P01 | Returning the str to the calling function.
| INFO | P01 |
    Descriptive Statistics for Streaming Sales Amounts ($):
        Count of sales   : 1
        Minimum sale     : $81.87
        Maximum sale     : $81.87
        Average sale     : $81.87
        Standard deviation: $0.00

| INFO | P01 | (2, 101.58, 'Water Bottle', 'North')
| INFO | P01 | Generated formatted multi-line SUMMARY string.
| INFO | P01 | Returning the str to the calling function.
| INFO | P01 |
    Descriptive Statistics for Streaming Sales Amounts ($):
        Count of sales   : 2
        Minimum sale     : $81.87
        Maximum sale     : $101.58
        Average sale     : $91.72
        Standard deviation: $13.94

| INFO | P01 | (3, 27.15, 'Running Shoes', 'East')
| INFO | P01 | Generated formatted multi-line SUMMARY string.
| INFO | P01 | Returning the str to the calling function.
| INFO | P01 |
    Descriptive Statistics for Streaming Sales Amounts ($):
        Count of sales   : 3
        Minimum sale     : $27.15
        Maximum sale     : $101.58
        Average sale     : $70.20
        Standard deviation: $38.56

| INFO | P01 | ========================
| INFO | P01 | Producer executed successfully!
| INFO | P01 | ========================
```
