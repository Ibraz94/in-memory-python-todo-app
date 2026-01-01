"""
Input validation utilities for the Todo In-Memory Python Console Application.

This module contains validation functions that ensure data integrity
across the application, as specified in the research document for
validation at the service layer.
"""


def validate_todo_description(description: str) -> str:
    """
    Validate a todo description according to the specification requirements.

    Args:
        description: The description to validate

    Returns:
        The validated and stripped description

    Raises:
        ValueError: If the description is invalid
    """
    if not isinstance(description, str):
        raise ValueError(f"Description must be a string, got {type(description)}")

    if not description.strip():
        raise ValueError("Description must not be empty or contain only whitespace")

    if len(description) > 1000:
        raise ValueError("Description must be between 1 and 1000 characters")

    return description.strip()


def validate_todo_id(todo_id: int) -> int:
    """
    Validate a todo ID according to the specification requirements.

    Args:
        todo_id: The ID to validate

    Returns:
        The validated ID

    Raises:
        ValueError: If the ID is invalid
    """
    if not isinstance(todo_id, int):
        raise ValueError(f"ID must be an integer, got {type(todo_id)}")

    if todo_id <= 0:
        raise ValueError(f"ID must be a positive integer, got {todo_id}")

    return todo_id


def validate_todo_completion_status(completed: bool) -> bool:
    """
    Validate a todo completion status.

    Args:
        completed: The completion status to validate

    Returns:
        The validated completion status

    Raises:
        ValueError: If the completion status is invalid
    """
    if not isinstance(completed, bool):
        raise ValueError(f"Completion status must be a boolean, got {type(completed)}")

    return completed