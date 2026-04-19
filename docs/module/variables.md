# Variables and Variable Types

> Naming and storing values in Python.

## What Is a Variable

In Python, a **variable** is a name that holds a value.

A variable associates a readable name with a piece of data
so it can be reused and inspected throughout a program.

## Common Variable Types

| Type | Holds | Example value |
|------|-------|---------------|
| `str` | text | `"Kansas City"` |
| `int` | a whole number | `42` |
| `float` | a decimal number | `3.14` |
| `bool` | true or false | `True` |
| `list[str]` | an ordered collection of text values | `["patience", "curiosity"]` |

## Type Hints

Type hints make the intended type of a variable explicit.

```python
name: str = "Abbie"
age: int = 5
weight_lbs: float = 9.8
is_cat: bool = True
skills: list[str] = ["patience", "curiosity"]
```

Benefits:

- clearer intent
- better editor feedback
- easier to collaborate

Type hints do **not** change how Python runs the code.

## Include Units in Numeric Names

Units matter when working with numbers.
Build the unit into the variable name to avoid confusion.

```python
weight_lbs: float = 9.8
height_ft: float = 2.4
temperature_f: float = 98.6
```

## Constants

Values that do not change are indicated by:

- naming them in `ALL_CAPS_WITH_UNDERSCORES`
- adding `Final` to the type hint

```python
from typing import Final

COURSE_NAME: Final[str] = "Streaming Data"
MAX_RETRIES: Final[int] = 3
```

## Collections

A `list` holds an ordered sequence of values of the same type.
The type inside the square brackets is called a **type parameter**.
It describes what kind of values the list contains.

```python
topics: list[str] = ["variables", "functions", "data"]
scores: list[float] = [92.5, 88.0, 95.5]
```

A `dict` maps keys to values.
Two type parameters are used: one for the key type, one for the value type.

```python
grades: dict[str, float] = {"Alice": 92.5, "Bob": 88.0}
```

`dict` is introduced in a later module. It is shown here for completeness.

## Why Variables Come First

Variables are introduced early because:

- programs are built from values
- data analysis depends on naming data clearly
- readable variable names make intent visible to anyone reading the code
