"""src/streaming/producer_case.py - Simple producer example.

Uses a Python generator to simulate a
stream of online sales, one at a time.

Author: Denise Case
Date: 2026-04

Practice key Python skills related to:
- imports
- logging
- variables
- type hints
- global constants
- f-strings
- functions
- generators
- main function
- conditional execution guard

Terminal command to run this file from the root project folder:

    uv run python -m streaming.producer_case

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it app_yourname.py, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

from collections.abc import Generator
import csv
from pathlib import Path
import random
import statistics
import time
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG = get_logger("P01", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT - they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# `Final` is added to indicate these variables should not be reassigned.

COURSE_NAME: Final[str] = "Streaming Data"

# These constants define our simulated online sales stream.
# In a real system, this data would come from a live website or payment API.
MESSAGE_COUNT: Final[int] = 3
MESSAGE_INTERVAL_SECONDS: Final[float] = 1.0

# Declare a list of products, each is a string.
# This simulates the variety of items being sold in real-time.
PRODUCTS: Final[list[str]] = [
    "Running Shoes",
    "Yoga Mat",
    "Water Bottle",
    "Backpack",
    "Sunglasses",
]

# Declare a list of regions where sales occur.
REGIONS: Final[list[str]] = ["North", "South", "East", "West", "Online"]

# Declare the min and max sale amounts
# to simulate realistic transaction values in our generated messages.
SALE_MIN: Final[float] = 5.00
SALE_MAX: Final[float] = 150.00


# === DECLARE GLOBAL CONSTANTS FOR FOLDERS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"

# === DECLARE GLOBAL CONSTANTS FOR FILES ===

OUTPUT_CSV: Final[Path] = DATA_DIR / "sales.csv"

# === DEFINE A GENERATOR FUNCTION TO PRODUCE A STREAM OF SALES ===

# A generator function uses `yield` instead of `return`.
# It produces one value at a time instead of computing everything at once.
# This is how we model data in motion - one event arriving at a time.
# A real sales feed works the same way: each sale arrives as it happens.


def generate_messages(count: int) -> Generator[tuple[int, float, str, str]]:
    """Generate a stream of simulated online sales, one at a time.

    A generator function uses `yield` instead of `return`.
    It produces one value at a time instead of computing everything at once.
    This models data in motion - one sale event arriving at a time.
    A real sales feed works the same way: each sale arrives as it happens.

    Arguments: count - how many sales to generate.

    Yields: one tuple of (sale_number, amount, product, region) at a time.
    """
    for i in range(count):
        sale_number: int = i + 1
        amount: float = round(random.uniform(SALE_MIN, SALE_MAX), 2)
        product: str = random.choice(PRODUCTS)
        region: str = random.choice(REGIONS)
        yield sale_number, amount, product, region


# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===


def get_statistics(amounts: list[float]) -> str:
    """Get a formatted summary showing descriptive statistics on sale amounts.

    Arguments: amounts - a list of sale amount floats from the stream.

    Returns: - a formatted multi-line string.
    """
    count: int = len(amounts)

    minimum: float = min(amounts) if count > 0 else 0.0
    maximum: float = max(amounts) if count > 0 else 0.0
    average: float = statistics.mean(amounts) if count > 0 else 0.0
    std_dev: float = statistics.stdev(amounts) if count > 1 else 0.0

    summary: str = f"""
    Descriptive Statistics for Streaming Sales Amounts ($):
        Count of sales   : {count}
        Minimum sale     : ${minimum:.2f}
        Maximum sale     : ${maximum:.2f}
        Average sale     : ${average:.2f}
        Standard deviation: ${std_dev:.2f}
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Main entry point for this script.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented.
    This is a multiline docstring - a special type of comment
    that explains what the function does.

    Use log_path to log privacy-aware paths for debugging.
    This is a good practice to verify things are working as expected.

    Arguments: None.

    Returns: None.
    """
    log_header(LOG, "P01")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Use the log_path() function to log paths for debugging.
    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_DIR", DATA_DIR)
    log_path(LOG, "OUTPUT_CSV", OUTPUT_CSV)

    # Create the data/ folder if it does not already exist.
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    LOG.info(f"Streaming {MESSAGE_COUNT} sales to {OUTPUT_CSV} ...")
    LOG.info("Watch each sale arrive. Press CTRL+C to stop early.\n")

    # Declare an empty list to store sale amounts for later analysis.
    messages: list[float] = []

    for message in generate_messages(MESSAGE_COUNT):
        # 1. Log the message tuple as INFO.
        LOG.info(message)

        # 2. Append the sale amount (the second item in the tuple) to the messages list.
        messages.append(message[1])  # Append the sale amount to the list

        # 3. Write the message to the output CSV file, one row at a time.
        with OUTPUT_CSV.open(mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(message)

        # 4. Call the function we defined above to get the statistics string.
        stats: str = get_statistics(messages)
        LOG.info(stats)

        # 5. Wait before generating the next message
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(MESSAGE_INTERVAL_SECONDS)

    LOG.info("========================")
    LOG.info("Producer executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main().
# This is standard Python "boilerplate".

if __name__ == "__main__":
    main()
