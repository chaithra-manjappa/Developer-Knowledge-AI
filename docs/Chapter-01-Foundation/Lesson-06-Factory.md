# Lesson 05 - Factory Pattern

## What is a Factory?

A Factory is a class responsible for creating objects.

Instead of creating objects throughout the application, we centralize object creation in one place.

---

## Why do we need a Factory?

Without a factory:

main.py

↓

if provider == "groq"

↓

GroqClient

↓

else

↓

OpenAIClient

Every new provider requires modifying application code.

With a Factory:

main.py

↓

LLMClientFactory

↓

GroqClient / OpenAIClient

Only the factory changes.

---

## Responsibilities

LLMClientFactory should:

- Read the provider name
- Create the correct client
- Return it

It should NOT:

- Generate AI responses
- Read prompt templates
- Know about LinkedIn
- Call generate()

---

## Advantages

- Centralized object creation
- Easier maintenance
- Easier testing
- Supports multiple providers
- Follows Open/Closed Principle

---

## Interview Question

Why use a Factory Pattern?

Because it separates object creation from object usage.

The application requests an object without knowing how it is created.

---

## Common Mistakes

❌ Creating clients in multiple files

❌ Using if/else throughout the application

❌ Mixing creation logic with business logic

---

## Key Takeaways

- Factory creates objects.
- Business logic uses objects.
- Object creation should have one place.
- Adding new providers becomes much easier.