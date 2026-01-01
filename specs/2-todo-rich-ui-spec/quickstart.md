# Quickstart: Rich UI Todo Application

## Prerequisites
- Python 3.13 or higher
- UV package manager
- Terminal that supports Rich formatting

## Setup
1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
3. Verify Rich library is installed:
   ```bash
   uv pip list | grep rich
   ```

## Running the Application
1. Start the application:
   ```bash
   uv run python -m todo_app
   ```
2. Use the Rich-based menu system to interact with todos
3. Available operations: Add, View, Update, Delete, Mark Complete

## Key Features
- Rich-formatted tables for viewing todos
- Interactive prompts for all operations
- Visual status indicators with color coding
- Confirmation dialogs for destructive operations
- Rich-formatted error messages

## Validation
1. Add a new todo using the Rich interface
2. View todos in the formatted table
3. Update a todo description
4. Mark a todo as complete
5. Delete a todo with confirmation dialog