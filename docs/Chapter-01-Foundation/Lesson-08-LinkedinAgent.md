# Lesson 07 - LinkedIn Writer Agent

## Goal

Build the business layer responsible for generating LinkedIn posts.

---

# What is an Agent?

An Agent coordinates multiple services to achieve a business goal.

In our application:

- PromptService prepares the prompt.
- GroqClient communicates with the AI.
- LinkedInWriterAgent coordinates both.

The agent contains the business logic.

---

# Responsibilities

The LinkedInWriterAgent should:

- Load the prompt template.
- Replace placeholders.
- Send the prompt to the LLM client.
- Return the generated LinkedIn post.

The agent should NOT:

- Read environment variables.
- Call the Groq SDK directly.
- Read Markdown files itself.
- Know API keys.

---

# Architecture

LinkedInWriterAgent

↓

PromptService

↓

linkedin_post.md

↓

GroqClient

↓

Groq API

---

# Why Inject Dependencies?

Instead of creating PromptService and GroqClient inside the agent, we pass them through the constructor.

Benefits:

- Easier testing
- Better flexibility
- Loose coupling
- Follows Dependency Injection

---

# Why Catch Exceptions?

The agent converts lower-level client exceptions into a business-level exception:

ContentGenerationError

This hides infrastructure details from the rest of the application.

---

# Design Principles Used

- Single Responsibility Principle
- Dependency Injection
- Separation of Concerns
- Exception Abstraction

---

# Key Takeaways

- The agent is the business layer.
- It coordinates services.
- It does not know implementation details.
- It depends on abstractions rather than implementation details.