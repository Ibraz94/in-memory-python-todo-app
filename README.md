# In-Memory Python Todo App

A simple, lightweight todo application implemented in Python with in-memory storage.

## Overview

This project implements a todo application in Python with in-memory storage. It provides basic todo functionality without requiring a persistent database.

## Features

- Add new todo items
- Mark todos as complete/incomplete
- Delete todo items
- List all todos with Rich UI formatting
- **Interactive mode** with Rich questionnaire for enhanced UX
- **CSV persistence** - todos are saved to `todos.csv` and persist across sessions
- In-memory performance with automatic CSV synchronization

## Project Structure

- `.claude/` - Claude Code configuration
- `.specify/` - SpecKit Plus templates and scripts
- `specs/` - Feature specifications and plans
- `history/` - History of decisions and prompts
  - `history/adr/` - Architecture Decision Records
  - `history/prompts/` - Prompt History Records
- `CLAUDE.md` - Claude Code rules and project instructions
- `README.md` - This file

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd in-memory-python-todo-app
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode (Recommended)

Run the app without arguments to enter interactive mode with Rich questionnaire:

```bash
uv run todo-app
```

This will present a menu where you can:
1. Add a new todo
2. List all todos
3. Mark todo as complete
4. Update a todo
5. Delete a todo
6. Exit

**Benefits of Interactive Mode:**
- Todos persist in memory during the session
- Rich UI with colored menus and tables
- Easy-to-use questionnaire interface
- All changes are automatically saved to `todos.csv`

### Command-Line Mode

You can also use individual commands:

```bash
# Add a new todo
uv run todo-app add "Buy groceries"

# List all todos
uv run todo-app list

# Mark a todo as complete
uv run todo-app complete 1

# Update a todo
uv run todo-app update 1 "Buy groceries and cook dinner"

# Delete a todo
uv run todo-app delete 1
```

### Data Persistence

All todos are automatically saved to `todos.csv` in the project root directory. The file format is:

```csv
id,description,completed
1,Write documentation,False
2,Review pull requests,True
```

Your todos will persist across sessions!

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[Add license information if applicable]