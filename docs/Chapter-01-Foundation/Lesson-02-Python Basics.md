# Lesson 1 – Application Entry Point

## Objective

Learn how a Python application starts and why every application has a single entry point.

---

## What is an Entry Point?

An entry point is the first piece of code executed when an application starts.

It acts as the application's front door.

Example:

User

↓

Application Starts

↓

main.py

↓

Application Logic

---

## Why use main.py?

Instead of starting from feature-specific files, the application starts from one location.

Benefits:

- Easier to understand
- Easier to maintain
- Single place to initialize the application

---

## What is a Function?

A function is a reusable block of code that performs one specific task.

Example:

```python
def greet():
    print("Hello")
```

Instead of repeating code, call:

```python
greet()
```

---

## What is a Docstring?

A docstring describes the purpose of a module, class, or function.

Example:

```python
"""Application entry point."""
```

It helps developers and documentation tools understand the code.

---

## What is a Type Hint?

Example:

```python
def main() -> None:
```

`-> None` indicates that the function does not return a value.

Type hints improve readability and help IDEs catch mistakes.

---

## Interview Questions

### Q1. What is an entry point?

The first code executed when an application starts.

---

### Q2. Why do we create a `main()` function?

To provide a clear and organized starting point for the application's workflow.

---

### Q3. Are type hints mandatory?

No. Python runs without them, but they improve readability and tooling support.

---

## Summary

Today we learned:

- What an entry point is.
- Why applications use `main.py`.
- What functions are.
- What docstrings are.
- What type hints are.