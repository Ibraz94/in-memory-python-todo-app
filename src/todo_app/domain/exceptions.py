"""
Custom domain exceptions for the Todo In-Memory Python Console Application.

This module contains all custom exceptions that represent domain-specific
error conditions in the application.
"""


class TodoError(Exception):
    """Base exception for all todo-related errors."""
    pass


class TodoNotFoundError(TodoError):
    """Raised when a requested todo item is not found."""

    def __init__(self, todo_id: int):
        self.todo_id = todo_id
        super().__init__(f"Todo item with ID {todo_id} not found")


class InvalidTodoError(TodoError):
    """Raised when a todo item has invalid data."""

    def __init__(self, message: str):
        super().__init__(message)


class DuplicateTodoError(TodoError):
    """Raised when attempting to create a duplicate todo item."""

    def __init__(self, todo_id: int):
        self.todo_id = todo_id
        super().__init__(f"Todo item with ID {todo_id} already exists")