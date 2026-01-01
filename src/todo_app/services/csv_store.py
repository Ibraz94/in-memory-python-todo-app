"""
CSV-backed storage implementation for the Todo In-Memory Python Console Application.

This module provides persistent storage using CSV files while maintaining
in-memory performance for operations.
"""

import csv
import os
from typing import Dict, List, Optional
from ..domain.models import TodoItem
from ..domain.exceptions import TodoNotFoundError, DuplicateTodoError


class CsvStore:
    """
    CSV-backed storage for todo items with in-memory caching.

    This class implements persistent storage using CSV files while maintaining
    in-memory performance. Data is loaded on initialization and saved after
    each modification.
    """

    def __init__(self, csv_file: str = "todos.csv"):
        """
        Initialize the CSV store.
        
        Args:
            csv_file: Path to the CSV file for storing todos
        """
        self.csv_file = csv_file
        self._todos: Dict[int, TodoItem] = {}
        self._next_id = 1
        self._load_from_csv()

    def _load_from_csv(self) -> None:
        """Load todos from the CSV file into memory."""
        if not os.path.exists(self.csv_file):
            return

        try:
            with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    todo_id = int(row['id'])
                    todo = TodoItem(
                        id=todo_id,
                        description=row['description'],
                        completed=row['completed'].lower() == 'true'
                    )
                    self._todos[todo_id] = todo
                    
                    # Update next_id
                    if todo_id >= self._next_id:
                        self._next_id = todo_id + 1
        except Exception as e:
            print(f"Warning: Could not load todos from {self.csv_file}: {e}")

    def _save_to_csv(self) -> None:
        """Save all todos from memory to the CSV file."""
        try:
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['id', 'description', 'completed']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for todo in sorted(self._todos.values(), key=lambda t: t.id):
                    writer.writerow({
                        'id': todo.id,
                        'description': todo.description,
                        'completed': str(todo.completed)
                    })
        except Exception as e:
            print(f"Error: Could not save todos to {self.csv_file}: {e}")

    def add(self, todo: TodoItem) -> int:
        """
        Add a new todo item to the store and save to CSV.

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

        self._save_to_csv()
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
        return [self._todos[todo_id] for todo_id in sorted(self._todos.keys())]

    def update(self, todo_id: int, updated_todo: TodoItem) -> TodoItem:
        """
        Update an existing todo item and save to CSV.

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
        self._save_to_csv()
        return updated_todo

    def delete(self, todo_id: int) -> bool:
        """
        Remove a todo item by its ID and save to CSV.

        Args:
            todo_id: The ID of the todo item to remove

        Returns:
            True if the item was found and deleted, False otherwise
        """
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        self._save_to_csv()
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
        """Clear all todos from the store and CSV file."""
        self._todos.clear()
        self._next_id = 1
        self._save_to_csv()
