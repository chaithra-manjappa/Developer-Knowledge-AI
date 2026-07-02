# Lesson 06 - Prompt Service

## Goal

Understand why AI prompts should be stored separately from Python code and how a Prompt Service makes AI applications more maintainable, reusable, and scalable.

---

# What is a Prompt?

A prompt is the instruction we send to a Large Language Model (LLM).

Example:

```
Write a LinkedIn post about SwiftUI Observation Framework.
```

The quality of the AI's response depends heavily on the quality of the prompt.

This is why Prompt Engineering has become an important skill in AI development.

---

# What is a Prompt Template?

A Prompt Template is a reusable prompt with placeholders.

Instead of writing:

```
Write a LinkedIn post about SwiftUI.
```

we write:

```
Write a LinkedIn post about

{{topic}}
```

At runtime, the application replaces `{{topic}}` with the actual topic.

Example:

```
SwiftUI Observation Framework
```

Result:

```
Write a LinkedIn post about

SwiftUI Observation Framework
```

This makes prompts reusable for different topics.

---

# Why Store Prompts in Markdown Files?

Instead of writing prompts inside Python code:

```python
prompt = """
Write a LinkedIn post...
"""
```

we store them in:

```
app/prompts/linkedin_post.md
```

Advantages:

- Easier to edit
- Easier to read
- No code changes required
- Non-developers can improve prompts
- Version controlled using Git
- Keeps business logic separate from prompt content

---

# What is PromptService?

PromptService is responsible for:

- Loading prompt templates
- Replacing placeholders
- Returning the final prompt

It acts as the bridge between Markdown templates and the AI agent.

Architecture:

```
linkedin_post.md
        │
        ▼
PromptService
        │
        ▼
Final Prompt String
        │
        ▼
LinkedIn Agent
```

---

# Responsibilities of PromptService

PromptService SHOULD:

- Read Markdown files
- Replace placeholders
- Return the completed prompt

PromptService SHOULD NOT:

- Call Groq/OpenAI
- Generate AI responses
- Know about LinkedIn
- Read environment variables
- Handle API keys

This follows the Single Responsibility Principle (SRP).

---

# Understanding Placeholders

Suppose the template contains:

```
Write about

{{topic}}
```

and we call:

```python
prompt_service.load(
    "linkedin_post.md",
    topic="SwiftUI Observation Framework",
)
```

PromptService replaces:

```
{{topic}}
```

with

```
SwiftUI Observation Framework
```

The final prompt becomes:

```
Write about

SwiftUI Observation Framework
```

---

# Why Use **variables?

Instead of creating different methods:

```python
load(topic)

load(topic, company)

load(topic, company, role)
```

we use:

```python
load(template_name, **variables)
```

This allows unlimited placeholders.

Example:

```python
prompt_service.load(
    "resume.md",
    company="OpenAI",
    role="Senior iOS Engineer",
    experience="11 years",
)
```

The service does not need to know in advance which placeholders exist.

This makes it reusable for every future AI agent.

---

# Why Pass the Prompt Folder in the Constructor?

Instead of hardcoding:

```python
Path("app/prompts")
```

inside the service, we pass it through the constructor.

Example:

```python
PromptService(Path("app/prompts"))
```

Benefits:

- Easier testing
- More flexible
- Supports multiple prompt folders
- Follows Dependency Injection

The service doesn't decide where prompts are stored.

Someone else provides that information.

---

# Real-World Example

Today our project has:

```
linkedin_post.md
```

Tomorrow we might add:

```
resume_review.md

pr_review.md

meeting_summary.md

daily_learning.md
```

The same PromptService can load every template.

No code changes are required.

Only new Markdown files are added.

---

# Project Architecture

```
Prompt Templates (.md)
           │
           ▼
     PromptService
           │
           ▼
     LinkedIn Agent
           │
           ▼
      Groq Client
           │
           ▼
        Groq API
```

Notice that PromptService does not know anything about AI providers.

Its only job is preparing prompts.

---

# Interview Questions

## What is a Prompt Template?

A Prompt Template is a reusable prompt containing placeholders that are replaced with actual values at runtime.

---

## Why shouldn't prompts be hardcoded in Python?

Hardcoded prompts are difficult to maintain, update, and reuse.

Separating prompts from code improves maintainability and allows prompt updates without modifying business logic.

---

## What is the responsibility of PromptService?

PromptService is responsible for loading prompt templates and replacing placeholders before sending them to the AI model.

---

## Why use Markdown files for prompts?

Markdown files are easy to read, edit, version control, and maintain.

They separate prompt content from application logic.

---

## What software design principles are used?

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Dependency Injection
- Reusability

---

# Common Mistakes

❌ Writing prompts directly inside Python code.

❌ Creating one PromptService for every agent.

❌ Mixing prompt generation with AI API calls.

❌ Hardcoding values instead of using placeholders.

❌ Making PromptService responsible for calling the AI model.

---

# Key Takeaways

- A prompt is an instruction sent to an AI model.
- Prompt templates make prompts reusable.
- Markdown files separate prompt content from application logic.
- PromptService loads templates and replaces placeholders.
- PromptService should never communicate with the AI provider.
- One PromptService can support multiple AI agents and prompt templates.

---

# Summary

PromptService is a reusable utility responsible for preparing prompts before they are sent to an AI model.

By storing prompts in Markdown files and using placeholders, we make our application easier to maintain, easier to scale, and more flexible for future AI agents.

This architecture is commonly used in production AI applications because it separates prompt management from business logic and AI communication.