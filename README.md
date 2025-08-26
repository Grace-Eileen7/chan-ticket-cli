# Phase 3 CLI Project Chan Tickets CLI

## Learning Goals

-A CLI application that solves a real-world problem and adheres to best practices.
-A database created and modified with SQLAlchemy ORM with 3+ related tables.
-A well-maintained virtual environment using Pipenv.
-Proper package structure in your application.
-Use of lists, dicts, and tuples.

***

c Overview

Chan Tickets CLI is a Python-based command-line interface application for buying and managing football match tickets, ensuring fans can not buy tickets that are already sold, cannot be sold twice. A problem witnessed so many times. The project leverages SQLAlchemy ORM for database management, follows OOP best practices, and uses Python lists, dictionaries, and tuples where appropriate.

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py            # Main CLI script
    ├── db
    │   ├── models.py     # ORM models for Matches, Users, Tickets
    │   └── seedy.py      # Optional seed script for test data
    ├── helpers.py        # Helper functions for CLI operations
    └── migrations        # Alembic migrations for database schema

```

***

## Features Implemented 


## Getting Started

```
1. Clone the Repository:
```

***
## Notes

-The application is interactive and relies on user input from the command line.
-Database migrations are managed using Alembic.
-Ensure your database is set up before running CLI commands.

## Generating  CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`. It will ask for
input, do some work, and accomplish some sort of task by the end.

Past that, CLIs can be whatever you'd like. An inventory navigator? A checkout
station for a restaurant? A choose-your-adventure video game? Absolutely!

itHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
