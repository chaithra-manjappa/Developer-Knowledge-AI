# Lesson 04 - LLM Clients

## Goal

Understand what an LLM Client is, why we need it, and why every AI application should separate AI provider communication from business logic.

---

# What is an LLM Client?

An LLM (Large Language Model) Client is a class responsible for communicating with an AI provider such as:

- Groq
- OpenAI
- Google Gemini
- Anthropic Claude
- Ollama (Local Models)

Instead of allowing the rest of the application to directly call an AI provider's SDK, we create our own client class.

Example:

```
LinkedIn Agent
        │
        ▼
   GroqClient
        │
        ▼
    Groq API
```

The application talks to **GroqClient**, not directly to the Groq SDK.

---

# Why do we need an LLM Client?

Imagine our application directly uses the Groq SDK.

```python
from groq import Groq

client = Groq(api_key="...")
```

Now suppose our company decides to switch to OpenAI.

Every file importing Groq must be modified.

Instead, we hide the SDK behind our own client.

```
Application
      │
      ▼
GroqClient
      │
      ▼
Groq SDK
```

If we later replace Groq with OpenAI, only the client changes.

The rest of the application remains unchanged.

---

# Responsibilities of GroqClient

The GroqClient has only one responsibility:

> Communicate with the Groq API.

Its responsibilities include:

- Initialize the Groq SDK
- Send prompts
- Receive responses
- Handle API errors
- Return generated text

---

# Responsibilities GroqClient Should NOT Have

The client should **NOT**:

- Know what LinkedIn is
- Generate prompts
- Read Markdown prompt templates
- Read environment variables
- Parse command-line arguments
- Perform business logic

Those responsibilities belong to other classes.

---

# Why do we pass the API key into the constructor?

Instead of this:

```python
Groq(api_key=os.getenv("GROQ_API_KEY"))
```

we use:

```python
GroqClient(api_key, model)
```

Why?

Because configuration should come from the Settings class.

The GroqClient should not know where the API key came from.

This follows the **Dependency Injection** principle.

---

# Why don't we call os.getenv() inside GroqClient?

Imagine tomorrow we use:

- AWS Secrets Manager
- Azure Key Vault
- Docker Secrets

The client should continue working without any changes.

It only needs:

- API Key
- Model Name

It should not care where those values originated.

---

# Why create a custom exception?

Instead of exposing SDK-specific exceptions to the rest of the application, we create:

```python
class GroqClientError(Exception):
    pass
```

Now the application only needs to handle:

```python
GroqClientError
```

instead of understanding Groq's internal exception types.

This makes our application less dependent on the external SDK.

---

# Project Architecture

```
                 Settings
                     │
                     ▼
               GroqClient
                     │
                     ▼
               Groq Python SDK
                     │
                     ▼
                  Groq API
```

Notice that only **GroqClient** knows about the Groq SDK.

---

# Why wrap the SDK?

Wrapping an SDK provides several benefits:

- Easier testing
- Easier maintenance
- Easier migration to another provider
- Cleaner business logic
- Better error handling

The rest of the application communicates with our own interface instead of a third-party library.

---

# Real-World Example

Today:

```
LinkedIn Agent
        │
        ▼
    GroqClient
```

Tomorrow:

```
LinkedIn Agent
        │
        ▼
   OpenAIClient
```

The LinkedIn Agent remains exactly the same.

Only the client changes.

This is one of the biggest advantages of good software architecture.

---

# Interview Questions

## What is an LLM Client?

An LLM Client is a wrapper around an AI provider's SDK that is responsible for communicating with the language model while hiding provider-specific implementation details.

---

## Why shouldn't business logic directly call the AI SDK?

Because it tightly couples the application to a specific provider.

Using a client allows providers to be replaced with minimal code changes.

---

## Why pass configuration into the constructor?

This follows Dependency Injection.

The client receives everything it needs instead of fetching configuration itself.

This improves testability and flexibility.

---

## Why create a custom exception?

It hides provider-specific exceptions from the rest of the application.

The application only needs to understand one exception type.

---

## What design principles are used here?

- Single Responsibility Principle (SRP)
- Dependency Injection (DI)
- Encapsulation
- Separation of Concerns

---

# Common Mistakes

❌ Calling `os.getenv()` inside every class.

❌ Importing the Groq SDK in multiple places.

❌ Mixing prompt generation with API communication.

❌ Hardcoding model names.

❌ Returning SDK-specific exceptions throughout the application.

---

# Key Takeaways

- The application should never communicate directly with the AI provider.
- All AI communication should go through a dedicated client.
- The client is responsible only for interacting with the AI provider.
- Configuration should come from the Settings class.
- Business logic should remain independent of the AI provider.
- Wrapping third-party SDKs makes applications easier to maintain and extend.