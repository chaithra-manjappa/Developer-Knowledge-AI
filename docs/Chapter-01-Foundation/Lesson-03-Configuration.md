# Configuration

## What is Configuration?

Configuration is a centralized place where an application stores values that can change between different environments without modifying the source code.

Some common configuration values are:

- API Keys
- Model name (e.g., Groq, OpenAI, Gemini)
- Log level
- Environment (Development, Testing, Production)
- Database URL
- Server port

---

## Why do we need Configuration?

Imagine our application has the API key written directly in multiple Python files.

If the API key changes, we would have to update it everywhere.

Instead, we store it in one place and let the application read it when it starts.

This makes the application:
- Easier to maintain
- More secure
- Easier to configure for different environments

---

## Why shouldn't API keys be hardcoded?

Hardcoding API keys is a bad practice because:

- Anyone with access to the code can see the key.
- If the code is pushed to GitHub, the API key could be exposed publicly.
- Changing the key requires modifying the source code.

Instead, API keys should be stored in environment variables or a `.env` file that is not committed to Git.

---

## Real-world Example

For our AI project, we may want to switch between different AI providers.

Development:

LLM_PROVIDER=groq

Production:

LLM_PROVIDER=openai

We should be able to switch providers by changing only the configuration, without changing any Python code.

---

## What I Learned

Today I learned that configuration is not business logic.

Its responsibility is only to provide application settings.

A well-designed application keeps configuration separate from the rest of the code, making it easier to maintain, secure, and extend.

# Lesson 02 - Configuration

## Goal

Understand why applications use configuration and how to centralize it using a Settings class.

---

# Why do we use a Settings class?

The Settings class acts as a **single source of truth** for the application's configuration.

Instead of reading environment variables throughout the application, we read them once and expose them through a single object.

Benefits:

- Centralized configuration
- Easier maintenance
- Cleaner code
- Easier testing
- Supports multiple environments
- Reduces duplicate code

---

# Why use a Dataclass?

A dataclass is ideal when a class is primarily used to store data.

Python automatically creates:

- Constructor
- String representation
- Equality methods

This reduces boilerplate code.

---

# Why use frozen=True?

Configuration should not change after the application starts.

Using `frozen=True` makes the Settings object immutable, preventing accidental modifications.

---

# Why use Environment Variables?

Environment variables allow us to:

- Keep secrets out of the source code.
- Use different configurations for Development, Testing, and Production.
- Share code without exposing sensitive information.

---

# Real-world Example

Development:

LLM_PROVIDER=groq

Production:

LLM_PROVIDER=openai

The application code remains exactly the same.

Only the configuration changes.

---

# Interview Questions

### What is Configuration?

Configuration contains values that control how an application runs but are not part of its business logic.

---

### Why shouldn't API keys be hardcoded?

- Security
- Easier maintenance
- Different environments
- Separation of concerns

---

### Why do we use a Settings class?

To centralize configuration and provide a single source of truth for the application.

---

### Why use a dataclass?

Because the Settings class only stores data and does not contain business logic.

---

# Key Takeaways

- Configuration is separate from business logic.
- Store configuration in one place.
- Never hardcode API keys.
- Read environment variables once.
- Expose configuration through a Settings object.