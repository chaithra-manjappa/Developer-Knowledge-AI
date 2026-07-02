# Lesson 08 – Playwright Basics

## Objective

Understand how browser automation works before writing automation code.

---

## What is Playwright?

Playwright is a modern browser automation framework that allows Python to control Chromium, Firefox, and WebKit browsers.

Instead of sending HTTP requests directly to a website, Playwright automates a real browser just like a human user.

---

## Browser Hierarchy

Browser

↓

Browser Context

↓

Page

---

### Browser

Represents an instance of Chromium, Firefox, or WebKit.

---

### Browser Context

An isolated browser profile.

Each context has its own:

- Cookies
- Cache
- Local Storage
- Session

Using Browser Contexts allows applications to stay logged in without affecting other sessions.

---

### Page

Represents a browser tab.

Every website interaction happens inside a Page.

---

## Why a BrowserManager?

The BrowserManager is responsible for:

- Launching browsers
- Creating contexts
- Opening pages
- Closing resources

It does not know anything about LinkedIn.

This separation follows the Single Responsibility Principle (SRP).

---

## Future Flow

main.py

↓

LinkedInPublisher

↓

BrowserManager

↓

Playwright

↓

Chromium

↓

LinkedIn