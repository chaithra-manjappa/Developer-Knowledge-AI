# Lesson 07 — LinkedIn Publisher

## Objective

Learn why publishing is separated from content generation.

---

## What is a Publisher?

A Publisher is responsible for delivering generated content to an external platform.

Examples:

- LinkedIn
- Microsoft Teams
- Slack
- Medium
- Dev.to

The Publisher never generates content.

It only receives content and sends it to a destination.

---

## Why separate Publisher from Agent?

The LinkedInWriterAgent creates knowledge.

The LinkedInPublisher shares that knowledge.

Separating these responsibilities follows the Single Responsibility Principle (SRP).

Benefits:

- Easier testing
- Better maintainability
- Easier to support multiple platforms
- Cleaner architecture

---

## Current Flow

User

↓

main.py

↓

LinkedInWriterAgent

↓

Generated Post

↓

LinkedInPublisher

↓

LinkedIn

---

## Current Implementation

At this stage the publisher only prints the generated post.

In the next lesson it will automate LinkedIn using Playwright.