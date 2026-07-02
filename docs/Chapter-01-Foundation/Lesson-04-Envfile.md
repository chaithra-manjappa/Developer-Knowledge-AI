# Lesson 03 - Environment Variables

## Goal

Understand what environment variables are, why they are used in modern applications, and why we separate loading environment variables from reading application configuration.

---

# What are Environment Variables?

Environment variables are key-value pairs maintained by the operating system that applications can read at runtime.

They allow applications to access configuration without hardcoding values into the source code.

Examples:

```text
GROQ_API_KEY=gsk_xxxxxxxxxxxxx
LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile
LOG_LEVEL=INFO
```

---

# Why do we use Environment Variables?

Imagine we hardcode an API key inside our application.

```python
api_key = "gsk_xxxxxxxxxxxxx"
```

Problems:

- The API key is visible in the source code.
- It may accidentally be committed to GitHub.
- Every developer would need to modify the source code.
- Different environments (Development, Testing, Production) require different values.

Environment variables solve these problems.

Benefits:

- Improve security.
- Support multiple environments.
- Keep secrets out of the source code.
- Make applications easier to configure.

---

# What is a `.env` File?

A `.env` file is **not** a Python feature.

It is simply a text file that stores environment variables in a convenient format for local development.

Example:

```text
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_xxxxxxxxxxxxx
LLM_MODEL=llama-3.3-70b-versatile
LOG_LEVEL=INFO
```

Python does **not** automatically read this file.

---

# Difference Between `.env` and Environment Variables

This is one of the most important concepts to understand.

| `.env` File | Environment Variables |
|-------------|-----------------------|
| A plain text file | Variables stored by the operating system |
| Used mostly during local development | Available while the application is running |
| Python cannot read it automatically | Python can access them using `os.getenv()` |
| Must be loaded into the environment first | Can be read directly by the application |

Think of the `.env` file as a convenient way to define environment variables during development.

---

# Why do we need an `EnvLoader`?

Our application should not know **how** environment variables are loaded.

Instead, we create a dedicated class whose only responsibility is:

> Load values from a `.env` file into the application's environment.

Responsibilities of `EnvLoader`:

- Read the `.env` file.
- Ignore blank lines and comments.
- Parse `KEY=VALUE` pairs.
- Store them in `os.environ`.

Responsibilities it should **NOT** have:

- Validate configuration.
- Decide which AI provider to use.
- Create a `Settings` object.
- Contain business logic.

---

# Why keep `EnvLoader` separate from `Settings`?

Following the **Single Responsibility Principle (SRP)**:

**EnvLoader**

Responsible only for loading environment variables.

**Settings**

Responsible only for reading environment variables and exposing them as application configuration.

Separating these responsibilities makes the application easier to maintain and extend.

---

# Real-World Example

Suppose today our application uses Groq.

```text
LLM_PROVIDER=groq
```

Tomorrow we decide to use OpenAI.

```text
LLM_PROVIDER=openai
```

The application code does **not** change.

Only the configuration changes.

This makes the application flexible and easier to maintain.

---

# Interview Questions

## What are environment variables?

Environment variables are key-value pairs provided by the operating system that allow applications to receive configuration at runtime.

---

## Why shouldn't API keys be hardcoded?

- Security risk
- Difficult to maintain
- Different environments require different values
- Violates separation of configuration from business logic

---

## Does Python automatically read `.env` files?

No.

Python only reads environment variables.

A `.env` file must first be loaded into the environment using a custom loader or a library such as `python-dotenv`.

---

## Why do we separate `EnvLoader` and `Settings`?

Because they have different responsibilities.

`EnvLoader` loads environment variables.

`Settings` reads those variables and provides application configuration.

This follows the Single Responsibility Principle.

---

# Key Takeaways

- Environment variables store runtime configuration.
- A `.env` file is only a convenience for local development.
- Python does not automatically read `.env` files.
- `EnvLoader` is responsible for loading variables.
- `Settings` is responsible for reading configuration.
- Keeping responsibilities separate results in cleaner, more maintainable software.