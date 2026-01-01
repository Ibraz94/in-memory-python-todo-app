"""
Domain models for the Todo In-Memory Python Console Application.

This module contains the core data structures and business entities
that represent the application's domain.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoItem:
    """
    Represents a single todo item with an identifier, description, and completion status.

    This entity follows the specification requirements:
    - Has a unique identifier assigned when created
    - Has a description that is required and non-empty
    - Has a completion status that defaults to False (pending)
    """

    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the TodoItem after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"ID must be a positive integer, got {self.id}")

        if not isinstance(self.description, str):
            raise ValueError(f"Description must be a string, got {type(self.description)}")

        if not self.description.strip():
            raise ValueError("Description must not be empty or contain only whitespace")

        if len(self.description) > 1000:
            raise ValueError("Description must be between 1 and 1000 characters")

        if not isinstance(self.completed, bool):
            raise ValueError(f"Completed status must be a boolean, got {type(self.completed)}")

    def mark_complete(self) -> None:
        """Mark this todo item as complete."""
        self.completed = True

    def update_description(self, new_description: str) -> None:
        """Update the description of this todo item."""
        if not isinstance(new_description, str):
            raise ValueError(f"Description must be a string, got {type(new_description)}")

        if not new_description.strip():
            raise ValueError("Description must not be empty or contain only whitespace")

        if len(new_description) > 1000:
            raise ValueError("Description must be between 1 and 1000 characters")

        self.description = new_description.strip()