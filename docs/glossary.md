# Glossary

> Key terms for this project.

## 1. Streaming Concepts

### streaming data

Data that is generated and processed continuously over time,
one event at a time, rather than collected and analyzed all at once.
A sale completing, a sensor reading, a page view - each is a streaming event.

### data in motion

Another way to describe streaming data.
The data is moving from where it is created to where it is needed,
rather than sitting in a file waiting to be read.

### producer

A program that generates and sends messages into a stream.
In this project, the producer simulates online sales arriving one at a time.

### consumer

A program that reads and processes messages from a stream.
Producers create data. Consumers use it.
Producers and consumers can run at the same time.

### message / event

One unit of data in a stream.
In this project, one message provides information about one sale.

### generator

A Python function that uses `yield` to produce one value at a time
instead of computing and returning everything at once.
Generators are a natural fit for streaming because real data also arrives one item at a time.

```python
def generate_messages(count: int):
    for i in range(count):
        yield i + 1   # produces one value, then pauses
```

## 2. Python Basics

### variable

A name that holds a value.

```python
course_name: str = "Streaming Data"
```

### constant

A variable whose value does not change while the program runs.
Named in `ALL_CAPS` by convention.

```python
MESSAGE_COUNT: Final[int] = 10
```

### type hint

An annotation that declares what type of data a variable holds.
Helps editors catch errors early. Does not change how the code runs.

```python
amount: float = 81.87
products: list[str] = ["Shoes", "Mat"]
```

### f-string

A string that embeds variable values directly into text.

```python
region: str = "North"
LOG.info(f"Sale from region: {region}")
```

### logging

Recording messages about what a program is doing while it runs.
Preferred over `print()` in professional projects.

```python
LOG.info("Starting producer.")
LOG.warning("No data received.")
```

### main function

The starting point of a script. Called by the conditional execution guard.

### conditional execution guard

The standard block at the bottom of every script.
Ensures `main()` only runs when the file is executed directly.

```python
if __name__ == "__main__":
    main()
```
