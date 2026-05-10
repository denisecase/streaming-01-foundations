# streaming-01-foundations

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Streaming data analytics: local streaming foundations.

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

This project introduces the workflow shape used throughout the course.

The project does not require Kafka to run,
but we start the install process
and begin practicing with multiple terminals.

Installations are early to allow for issues.

Our producer this week reads sales records from a local CSV file,
processes each record one at a time,
and writes consumed records to an output CSV (it's a proxy for a
Kafka topic that we will use for "real" streaming projects).

Kafka setup begins here,
but Kafka does not need to be running for this project to succeed.
The goal is to get the local project working first and
begin work with Kafka so we can use it in the next module.

Ask lots of questions - we are here to help.
It's only really bad the very first time we use it.
It gets better.

## Working Files

You'll work with just these areas:

- **data/** - input data and generated output files
- **docs/** - the project narrative and documentation
- **src/streaming/** - producer, consumer, and supporting code
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

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

After completing Phase 1. **Start & Run**, you'll have your own GitHub project
running with Kafka.

Use four named terminals for practice:

1. **kafka** - where kafka will run (if Win, use WSL)
2. **topics** - manage topics (if Win, use WSL)
3. **producer** - run the project and producer
4. **consumer** - run the consumer

After the producer and consumer run successfully, you should see:

```shell
========================
Consumer executed successfully!
========================
```

A new file `project.log` will appear in the root project folder and
the producer will stream messages to a new **data/output** file.
The consumer will read and process message events from that file.

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

### In VS Code Terminal 1: Start Kafka (kafka)

For full instructions see
[**start kafka**](https://denisecase.github.io/pro-analytics-02/kafka/start-kafka/).

If any command fails,
repeat the steps at
[**install kafka**](https://denisecase.github.io/pro-analytics-02/kafka/install-kafka/)
until starting up is reliable.

Open a new VS Code terminal. Rename it `kafka`.
If running Windows, specify the terminal type as **wsl** or
type `wsl`.
Run the commands one at a time.

Step 1. Verify Java and PATH

```bash
echo "$JAVA_HOME"

"$JAVA_HOME/bin/java" --version
```

Step 2. Rebuild ClusterID (as needed)

```bash
cd ~/kafka

rm -rf /tmp/kraft-combined-logs

KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

echo "Cluster ID: $KAFKA_CLUSTER_ID"

bin/kafka-storage.sh format --standalone -t "$KAFKA_CLUSTER_ID" -c config/server.properties
```

Step 3. Start kafka server (keep running)

```bash
cd ~/kafka

bin/kafka-server-start.sh config/server.properties
```

### In VS Code terminal 2: Create Topic (topics)

For full instructions see
[**create topic**](https://denisecase.github.io/pro-analytics-02/kafka/create-topic/).

The topic name must match the name defined in your
`.env` file (copy `.env.example` to `.env`).

Open another VS Code terminal. Rename it `topics`.
If running Windows, specify the terminal type as **wsl** or
type `wsl`.
Run the commands one at a time.

```bash
cd ~/kafka

bin/kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1 \
  --topic streaming-01-foundations-case
```

### In VS Code Terminal 3: Run Project and Producer (producer)

Open another VS Code terminal. Rename it `producer`.
If running Windows, use **PowerShell**.
Run the commands one at a time.

```shell

```shell
# reset uv cache only after suspected cache corruption or strange dependency errors
# uv cache clean

uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files

# repeat if changes were made by pre-commit tasks
git add -A
uvx pre-commit run --all-files

# run the producer (produces messages)
uv run python -m streaming.producer_case

# do chores
uv run ruff format .
uv run ruff check . --fix
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

### In VS Code Terminal 4: Run Consumer (consumer)

Open another VS Code terminal. Rename it `consumer`.
If running Windows, use **PowerShell**.
Run the commands one at a time.
Verify Kafka is reachable, then start the consumer.

```shell
clear
uv run python -m streaming.consumer_case
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>> or

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Missing .env?

See [create topic](https://denisecase.github.io/pro-analytics-02/kafka/create-topic/)
for why we must copy `.env.example` to `.env`.

## Many Terminals

See [many terminals](https://denisecase.github.io/pro-analytics-02/kafka/many-terminals/)
for how we name our terminals (and if Windows, how we get the different types).
You can split terminals shown below, or just click between them as you like.

## Example Producer Output

```text
| P01 | === RUN START ===
| P01 | project=P01
| P01 | repo_dir=streaming-01-foundations
| P01 | python=3.14.0
| P01 | os=Windows 11
| P01 | shell=powershell
| P01 | cwd=.
| P01 | github_actions=False
| P01 | ========================
| P01 | START producer main()
| P01 | ========================
| P01 | ROOT_DIR = .
| P01 | DATA_DIR = data
| P01 | SALES_CSV = data\sales.csv
| P01 | TOPIC_CSV = data\output\streaming-01-foundations-case.csv
| P01 | ========================
| P01 | SECTION A. Acquire
| P01 | ========================
| P01 | Loading settings from .env...
| P01 | KAFKA_TOPIC                       = streaming-01-foundations-case
| P01 | KAFKA_CLEAR_TOPIC_ON_START        = True
| P01 | PRODUCER_MESSAGE_COUNT            = 3
| P01 | PRODUCER_MESSAGE_INTERVAL_SECONDS = 2.0
| P01 | Verifying local source data...
| P01 | Source file found: sales.csv
| P01 | Preparing local simulated topic file...
| P01 | Deleted existing topic file: streaming-01-foundations-case.csv
| P01 | Topic file will be created: streaming-01-foundations-case.csv
| P01 | ========================
| P01 | SECTION P. Produce Messages
| P01 | ========================
| P01 | Sending messages...
| P01 | Sending up to 3 local message(s).
| P01 | Writing to simulated topic file: streaming-01-foundations-case.csv
| P01 | Watch each sale arrive. Press CTRL+C to stop early.

| P01 | {
  order_id: e7324981-a9f0-419f-b708-d0a333451fff
  datetime: 2026-05-04T08:11:00Z
  region_id: US-TX
  currency_code: USD
  product_id: PY-STREAM-005
  unit_price: 59.99
  quantity: 3
  is_online: true
  customer_id: CUST-4150
  is_new_customer: false
  device_type: tablet
  payment_method: paypal
  referral_source: paid_search
  discount_code:
  customer_note: Gift for my team
}
| P01 |   Sending local message with key=US-TX
| P01 |   MESSAGE SENT  sent=1
2026-05-10 07:37:20 | P01 | {
  order_id: d61943e0-f543-4b5f-9c9a-18605ea4cfe5
  datetime: 2026-05-04T08:23:00Z
  region_id: US-TX
  currency_code: USD
  product_id: PY-DATA-002
  unit_price: 49.99
  quantity: 1
  is_online: true
  customer_id: CUST-1106
  is_new_customer: false
  device_type: mobile
  payment_method: paypal
  referral_source: paid_search
  discount_code:
  customer_note: Gift for my team
}
2026-05-10 07:37:20 | P01 |   Sending local message with key=US-TX
2026-05-10 07:37:20 | P01 |   MESSAGE SENT  sent=2
| P01 | {
  order_id: 14da1915-8e74-47be-9e10-f7275d31af46
  datetime: 2026-05-04T08:28:00Z
  region_id: CA-QC
  currency_code: CAD
  product_id: PY-NLP-006
  unit_price: 54.99
  quantity: 1
  is_online: true
  customer_id: CUST-2133
  is_new_customer: false
  device_type: desktop
  payment_method: paypal
  referral_source: organic
  discount_code:
  customer_note: Learning at my own pace
}
| P01 |   Sending local message with key=CA-QC
| P01 |   MESSAGE SENT  sent=3
| P01 | ========================
| P01 | SECTION E. Exit
| P01 | ========================
| P01 | Summary:
| P01 | Sent 3 message(s).
| P01 | WROTE TOPIC_CSV = data\output\streaming-01-foundations-case.csv
| P01 | ========================
| P01 | Producer executed successfully!
| P01 | ========================
```

## Example Consumer Output

```text
| C01 | ========================
| C01 | START consumer main()
| C01 | ========================
| C01 | ROOT_DIR = .
| C01 | DATA_DIR = data
| C01 | TOPIC_CSV = data\output\streaming-01-foundations-case.csv
| C01 | OUTPUT_CSV = data\output\consumed_sales.csv
| C01 | ========================
| C01 | SECTION A. Acquire
| C01 | ========================
| C01 | Loading settings from .env...
| C01 | KAFKA_TOPIC                    = streaming-01-foundations-case
| C01 | CONSUMER_MAX_MESSAGES          = 1000
| C01 | CONSUMER_POLL_INTERVAL_SECONDS = 0.5
| C01 | CONSUMER_TIMEOUT_SECONDS       = 10.0
| C01 | Verifying local simulated topic file...
| C01 | Topic file found: streaming-01-foundations-case.csv
| C01 | ========================
| C01 | SECTION C. Consume and Process Messages
| C01 | ========================
| C01 | Initializing output...
| C01 | Output CSV cleared: consumed_sales.csv
| C01 | Consuming local messages...
| C01 | Waiting for up to 1000 message(s).
| C01 | Stopping after 10.0s with no new message.

| C01 | {'order_id': 'e7324981-a9f0-419f-b708-d0a333451fff', 'datetime': '2026-05-04T08:11:00Z', 'region_id': 'US-TX', 'currency_code': 'USD', 'product_id': 'PY-STREAM-005', 'unit_price': '59.99', 'quantity': '3', 'is_online': 'true', 'customer_id': 'CUST-4150', 'is_new_customer': 'false', 'device_type': 'tablet', 'payment_method': 'paypal', 'referral_source': 'paid_search', 'discount_code': '', 'customer_note': 'Gift for my team'}
| C01 | Processing raw local message.
| C01 | MESSAGE CONSUMED
| C01 | consumed=1
| C01 | {'order_id': 'd61943e0-f543-4b5f-9c9a-18605ea4cfe5', 'datetime': '2026-05-04T08:23:00Z', 'region_id': 'US-TX', 'currency_code': 'USD', 'product_id': 'PY-DATA-002', 'unit_price': '49.99', 'quantity': '1', 'is_online': 'true', 'customer_id': 'CUST-1106', 'is_new_customer': 'false', 'device_type': 'mobile', 'payment_method': 'paypal', 'referral_source': 'paid_search', 'discount_code': '', 'customer_note': 'Gift for my team'}
| C01 | Processing raw local message.
| C01 | MESSAGE CONSUMED
| C01 | consumed=2
| C01 | {'order_id': '14da1915-8e74-47be-9e10-f7275d31af46', 'datetime': '2026-05-04T08:28:00Z', 'region_id': 'CA-QC', 'currency_code': 'CAD', 'product_id': 'PY-NLP-006', 'unit_price': '54.99', 'quantity': '1', 'is_online': 'true', 'customer_id': 'CUST-2133', 'is_new_customer': 'false', 'device_type': 'desktop', 'payment_method': 'paypal', 'referral_source': 'organic', 'discount_code': '', 'customer_note': 'Learning at my own pace'}
| C01 | Processing raw local message.
| C01 | MESSAGE CONSUMED
| C01 | consumed=3
| C01 | No new message received within 10.0s timeout.
| C01 | Producer finished or paused. Stopping consumer.
| C01 | Saving artifacts...
| C01 | WROTE OUTPUT_CSV = data\output\consumed_sales.csv
| C01 | ========================
| C01 | SECTION E. Exit
| C01 | ========================
| C01 | Summary:
| C01 | Consumed 3 message(s).
| C01 | OUTPUT_CSV = data\output\consumed_sales.csv
| C01 | ========================
| C01 | Consumer executed successfully!
| C01 | ========================
```
