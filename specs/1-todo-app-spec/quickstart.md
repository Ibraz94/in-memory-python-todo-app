# Quickstart Guide: Todo In-Memory Python Console Application

## Prerequisites

- Python 3.13 or higher installed
- UV package manager installed

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m src.todo_app.cli.app
   ```

## Basic Usage

### Adding a Todo
```bash
python -m src.todo_app.cli.app add "Buy groceries"
```

### Viewing Todos
```bash
python -m src.todo_app.cli.app list
```

### Updating a Todo
```bash
python -m src.todo_app.cli.app update 1 "Buy groceries and cook dinner"
```

### Marking a Todo as Complete
```bash
python -m src.todo_app.cli.app complete 1
```

### Deleting a Todo
```bash
python -m src.todo_app.cli.app delete 1
```

## Available Commands

- `add <description>`: Add a new todo item
- `list`: View all todo items
- `update <id> <new_description>`: Update the description of a todo
- `complete <id>`: Mark a todo as complete
- `delete <id>`: Delete a todo item

## Example Workflow

1. Add a few todos:
   ```bash
   python -m src.todo_app.cli.app add "Write report"
   python -m src.todo_app.cli.app add "Schedule meeting"
   python -m src.todo_app.cli.app add "Review code"
   ```

2. View your todos:
   ```bash
   python -m src.todo_app.cli.app list
   ```

3. Complete a task:
   ```bash
   python -m src.todo_app.cli.app complete 1
   ```

4. Update a task:
   ```bash
   python -m src.todo_app.cli.app update 2 "Schedule team meeting"
   ```

5. Delete a completed task:
   ```bash
   python -m src.todo_app.cli.app delete 1
   ```

## Error Handling

- Invalid commands will show usage help
- Non-existent todo IDs will show an appropriate error message
- Empty descriptions will be rejected with an error message
- Invalid input formats will show helpful error messages