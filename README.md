# Feature Flags API

A small, opinionated backend service built with **FastAPI** to manage and serve feature flags.

This project is intended as a **learning-focused, production-oriented** example of how to structure a Python backend using modern tools such as FastAPI, Pydantic, PostgreSQL, and Alembic.

The initial scope is intentionally minimal to keep the codebase understandable and extensible.

---

## 🎯 Goals

- Practice building a real-world FastAPI backend
- Learn how to structure a Python API project cleanly
- Use PostgreSQL with SQLAlchemy and Alembic migrations
- Avoid overengineering while following good backend practices

---

## 🧩 Planned Features

- Create and manage feature flags
- Enable or disable features via API
- Persist data in PostgreSQL
- Database migrations using Alembic

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Pydantic
- PostgreSQL
- SQLAlchemy
- Alembic

---

## 🚧 Project Status

🚧 **Work in progress**

The project is being built step by step.  
The focus is on clarity, learning, and clean structure rather than completeness.

## How to run the project:

### Create the virtual environment

1. Create a virtual environment on the terminal:

```bash
python3 -m venv venv
```

If there is an error creating the venv just delete the venv and try again. Worked for me.

2. Activate the virtual environment:

```bash
source venv/bin/activate
```

Tipp: If you just open a new terminal in vscode the venv is activated automatically

### Install requirements

For the project to work, you need to install all the required packages for this project:

```bash
pip install -r requirements.txt
```

### Install Prostgresql, if not existing

#### IMPORTANT: IF version check fails add path to shell

```bash
echo 'export PATH="/usr/local/opt/postgresql@16/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

```bash
brew install postgresql@16 #install postresql
```

```bash
brew psql --version #check version
```

```bash
brew services start postgresql@16 #start postgresql
```

```bash
\q #quit postgresql
```

### Create DB

```bash
createdb feature_flags
```

### Apply Revisions

```bash
alembic upgrade head
```

### Start Application

To start the application use:

```bash
uvicorn main:app --reload
```

- Open http://127.0.0.1:8000/ to see {"status":"ok"}
- Open http://127.0.0.1:8000/docs to see API documentation
