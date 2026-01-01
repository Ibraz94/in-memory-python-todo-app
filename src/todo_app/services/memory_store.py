"""
In-memory storage implementation for the Todo In-Memory Python Console Application.

This module provides an in-memory storage mechanism that stores all todo items
in a Python dictionary, following the constitutional requirement for in-memory
only storage with no persistent storage.
"""

from typing import Dict, List, Optional
from todo_app.domain.models import TodoItem
from todo_app.domain.exceptions import TodoNotFoundError, DuplicateTodoError


class MemoryStore:
    """
    In-memory storage for todo items.

    This class implements the storage layer using Python's built-in dictionary
    for O(1) lookup performance, as specified in the research document.
    All data is stored in memory only and will be lost when the application terminates.
    """

    def __init__(self):
        """Initialize the in-memory store with an empty collection of todos."""
        self._todos: Dict[int, TodoItem] = {}
        self._next_id = 1

    def add(self, todo: TodoItem) -> int:
        """
        Add a new todo item to the in-memory store.

        Args:
            todo: The TodoItem to add

        Returns:
            The ID of the added todo item

        Raises:
            DuplicateTodoError: If a todo with the same ID already exists
        """
        if todo.id in self._todos:
            raise DuplicateTodoError(todo.id)

        self._todos[todo.id] = todo

        # Update the next ID if necessary
        if todo.id >= self._next_id:
            self._next_id = todo.id + 1

        return todo.id

    def get(self, todo_id: int) -> TodoItem:
        """
        Retrieve a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The TodoItem with the specified ID

        Raises:
            TodoNotFoundError: If no todo with the specified ID exists
        """
        if todo_id not in self._todos:
            raise TodoNotFoundError(todo_id)

        return self._todos[todo_id]

    def get_all(self) -> List[TodoItem]:
        """
        Retrieve all todo items in insertion order.

        Returns:
            A list of all TodoItems, ordered by insertion (ID)
        """
        # Return todos in insertion order (by ID)
        return [self._todos[todo_id] for todo_id in sorted(self._todos.keys())]

    def update(self, todo_id: int, updated_todo: TodoItem) -> TodoItem:
        """
        Update an existing todo item.

        Args:
            todo_id: The ID of the todo to update
            updated_todo: The updated TodoItem

        Returns:
            The updated TodoItem

        Raises:
            TodoNotFoundError: If no todo with the specified ID exists
        """
        if todo_id not in self._todos:
            raise TodoNotFoundError(todo_id)

        if updated_todo.id != todo_id:
            raise ValueError("Updated todo ID must match the ID being updated")

        self._todos[todo_id] = updated_todo
        return updated_todo

    def delete(self, todo_id: int) -> bool:
        """
        Remove a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to remove

        Returns:
            True if the item was found and deleted, False otherwise
        """
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo item.

        Returns:
            The next available ID
        """
        next_id = self._next_id
        self._next_id += 1
        return next_id

    def clear(self) -> None:
        """Clear all todos from the store."""
        self._todos.clear()
        self._next_id = 1