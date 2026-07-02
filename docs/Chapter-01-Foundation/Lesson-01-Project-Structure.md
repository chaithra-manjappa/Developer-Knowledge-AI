# Lesson 01 - Project Structure

## Goal

Understand why we create a project structure before writing any code.

---

# What is a Project Structure?

A project structure is the way we organize files and folders inside an application.

Just like a house has separate rooms for different purposes (bedroom, kitchen, living room), a software project has different folders for different responsibilities.

A well-organized project is:

- Easier to understand
- Easier to maintain
- Easier to scale
- Easier for other developers to contribute to

---

# Our Project Structure

```
Developer-Knowledge-AI/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── docs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

---

# Why do we have an `app` folder?

The `app` folder contains the application's source code.

Instead of placing Python files in the project root, we keep them inside `app`.

Benefits:

- Separates source code from configuration and documentation.
- Keeps the project clean.
- Makes the project easier to navigate.
- Scales well as the application grows.

Example:

```
app/
    agents/
    services/
    models/
    config/
    prompts/
```

Everything related to the application lives inside `app`.

---

# Why not keep everything in the root folder?

Imagine a project with 50 Python files:

```
main.py
settings.py
groq_client.py
linkedin_agent.py
news_service.py
...
```

Finding files becomes difficult.

Instead:

```
app/
    agents/
    services/
    models/
```

Everything has a dedicated place.

---

# What is `main.py`?

`main.py` is the application's entry point.

It is the first file that runs when the application starts.

Example:

```
python -m app.main
```

Responsibilities of `main.py`:

- Start the application
- Load configuration
- Create required objects
- Call the appropriate workflow

It should **not** contain business logic.

---

# Why do we use `__init__.py`?

This is one of the most common questions in Python interviews.

`__init__.py` tells Python that a directory should be treated as a package.

Example:

```
app/
    __init__.py
    main.py
```

Now Python understands that `app` is a package.

Without it, importing modules may not work consistently across environments (especially in older Python versions).

---

# What happens inside `__init__.py`?

Sometimes nothing.

An empty file is perfectly fine.

Sometimes it is used to:

- Initialize the package
- Export commonly used classes
- Define package-level variables
- Configure logging

In our project, we will keep it empty.

---

# Why is it named `__init__.py`?

`init` stands for **initialize**.

When Python imports a package for the first time, it executes `__init__.py`.

Example:

```
import app
```

Python loads:

```
app/__init__.py
```

before loading other modules.

---

# What is `README.md`?

The README is the first document people see when they visit your GitHub repository.

It should answer:

- What is this project?
- Why was it built?
- How do I run it?
- What technologies are used?

Think of it as the project's user manual.

---

# What is `requirements.txt`?

This file lists all Python dependencies required to run the project.

Example:

```
groq
python-dotenv
requests
```

Instead of installing packages one by one, users can run:

```
pip install -r requirements.txt
```

---

# What is `.gitignore`?

`.gitignore` tells Git which files should **not** be tracked.

Examples:

```
venv/
__pycache__/
.env
```

We don't commit these because:

- Virtual environments can be recreated.
- Cache files are generated automatically.
- `.env` contains secrets like API keys.

---

# What is `.env.example`?

This file documents the environment variables required by the application.

Example:

```
LLM_PROVIDER=
GROQ_API_KEY=
OPENAI_API_KEY=
```

It acts as a template.

Each developer creates their own `.env` file based on it.

The actual `.env` file is never committed to Git.

---

# Real-World Example

Imagine joining a company where the project contains over 5,000 files.

Without a proper folder structure, finding the right file would be extremely difficult.

A clean project structure allows any developer to quickly understand where code belongs.

---

# Interview Questions

### Why do we keep source code inside an `app` folder?

To separate application code from configuration, documentation, and other project files. It improves organization and scalability.

---

### Why do we use `__init__.py`?

It marks a directory as a Python package and is executed when the package is imported. It can also be used for package initialization.

---

### What is the purpose of `requirements.txt`?

It lists the Python packages required to run the application, making setup consistent across different environments.

---

### Why should `.env` not be committed to Git?

Because it contains sensitive information such as API keys and credentials.

---

# Key Takeaways

- A good project structure improves maintainability.
- Every folder should have a clear responsibility.
- `app` contains application source code.
- `main.py` is the application's entry point.
- `__init__.py` marks a directory as a Python package.
- `.gitignore` protects unnecessary and sensitive files.
- `.env.example` documents required environment variables without exposing secrets.