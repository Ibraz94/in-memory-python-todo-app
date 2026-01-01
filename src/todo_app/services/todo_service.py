"""
Business logic service for the Todo In-Memory Python Console Application.

This module implements the core business logic for todo operations,
following the specification requirements for the five core features:
add, view, update, delete, and mark complete.
"""

from typing import List, Optional
from todo_app.domain.models import TodoItem
from todo_app.domain.exceptions import TodoNotFoundError, InvalidTodoError
from todo_app.services.memory_store import MemoryStore
from todo_app.utils.validators import validate_todo_description, validate_todo_id


class TodoService:
    """
    Service layer for todo operations.

    This class implements the business logic for all todo operations,
    coordinating between the domain models and the in-memory storage.
    """

    def __init__(self, storage: Optional[MemoryStore] = None):
        """
        Initialize the TodoService.

        Args:
            storage: Optional MemoryStore instance. If not provided,
                    a new instance will be created.
        """
        self.storage = storage if storage is not None else MemoryStore()

    def add_todo(self, description: str) -> TodoItem:
        """
        Add a new todo item with the given description.

        This method implements the 'add todo' feature from the specification:
        - Validates the description
        - Creates a new TodoItem with the next available ID
        - Stores the item in memory
        - Returns the created item

        Args:
            description: The description of the new todo item

        Returns:
            The newly created TodoItem

        Raises:
            InvalidTodoError: If the description is invalid
        """
        # Validate the description
        validated_description = validate_todo_description(description)

        # Get the next available ID
        new_id = self.storage.get_next_id()

        # Create a new TodoItem
        new_todo = TodoItem(id=new_id, description=validated_description, completed=False)

        # Add to storage
        self.storage.add(new_todo)

        return new_todo

    def list_todos(self) -> List[TodoItem]:
        """
        Retrieve all todo items.

        This method implements the 'view todos' feature from the specification:
        - Returns all todo items in insertion order
        - Includes status and identifiers

        Returns:
            A list of all TodoItems in insertion order
        """
        return self.storage.get_all()

    def get_todo(self, todo_id: int) -> TodoItem:
        """
        Retrieve a specific todo item by ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The TodoItem with the specified ID

        Raises:
            TodoNotFoundError: If no todo with the specified ID exists
        """
        # Validate the ID
        validate_todo_id(todo_id)

        # Get from storage
        return self.storage.get(todo_id)

    def update_todo(self, todo_id: int, new_description: str) -> TodoItem:
        """
        Update the description of an existing todo item.

        This method implements the 'update todo' feature from the specification:
        - Validates the ID and new description
        - Updates the existing item's description
        - Preserves other attributes as required

        Args:
            todo_id: The ID of the todo item to update
            new_description: The new description for the todo item

        Returns:
            The updated TodoItem

        Raises:
            TodoNotFoundError: If no todo with the specified ID exists
            InvalidTodoError: If the new description is invalid
        """
        # Validate the ID
        validate_todo_id(todo_id)

        # Validate the new description
        validated_description = validate_todo_description(new_description)

        # Get the existing todo
        existing_todo = self.storage.get(todo_id)

        # Update the description
        updated_todo = TodoItem(
            id=existing_todo.id,
            description=validated_description,
            completed=existing_todo.completed
        )

        # Update in storage
        return self.storage.update(todo_id, updated_todo)

    def mark_complete(self, todo_id: int) -> TodoItem:
        """
        Mark a todo item as complete.

        This method implements the 'mark todo as complete' feature from the specification:
        - Validates the ID
        - Updates the completion status to True
        - Handles already completed items gracefully

        Args:
            todo_id: The ID of the todo item to mark as complete

        Returns:
            The updated TodoItem

        Raises:
            TodoNotFoundError: If no todo with the specified ID exists
        """
        # Validate the ID
        validate_todo_id(todo_id)

        # Get the existing todo
        existing_todo = self.storage.get(todo_id)

        # Mark as complete
        updated_todo = TodoItem(
            id=existing_todo.id,
            description=existing_todo.description,
            completed=True
        )

        # Update in storage
        return self.storage.update(todo_id, updated_todo)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item.

        This method implements the 'delete todo' feature from the specification:
        - Validates the ID
        - Removes the item from storage
        - Returns whether the item was found and deleted

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the item was found and deleted, False otherwise
        """
        # Validate the ID
        validate_todo_id(todo_id)

        # Delete from storage
        return self.storage.delete(todo_id)