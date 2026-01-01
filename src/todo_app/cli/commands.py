"""
CLI command definitions for the Todo In-Memory Python Console Application.

This module defines the command-line interface commands that map to
the core functionality of the application.
"""

import argparse
from typing import Any
from todo_app.services.todo_service import TodoService


def add_command_parser(subparsers: argparse._SubParsersAction) -> None:
    """
    Add the 'add' command to the argument parser.

    This command implements the 'add todo' feature from the specification.
    """
    parser_add = subparsers.add_parser('add', help='Add a new todo item')
    parser_add.add_argument('description', nargs='+', help='The description of the todo item')


def list_command_parser(subparsers: argparse._SubParsersAction) -> None:
    """
    Add the 'list' command to the argument parser.

    This command implements the 'view todos' feature from the specification.
    """
    parser_list = subparsers.add_parser('list', help='View all todo items')


def update_command_parser(subparsers: argparse._SubParsersAction) -> None:
    """
    Add the 'update' command to the argument parser.

    This command implements the 'update todo' feature from the specification.
    """
    parser_update = subparsers.add_parser('update', help='Update the description of a todo item')
    parser_update.add_argument('id', type=int, help='The ID of the todo item to update')
    parser_update.add_argument('description', nargs='+', help='The new description for the todo item')


def complete_command_parser(subparsers: argparse._SubParsersAction) -> None:
    """
    Add the 'complete' command to the argument parser.

    This command implements the 'mark todo as complete' feature from the specification.
    """
    parser_complete = subparsers.add_parser('complete', help='Mark a todo item as complete')
    parser_complete.add_argument('id', type=int, help='The ID of the todo item to mark as complete')


def delete_command_parser(subparsers: argparse._SubParsersAction) -> None:
    """
    Add the 'delete' command to the argument parser.

    This command implements the 'delete todo' feature from the specification.
    """
    parser_delete = subparsers.add_parser('delete', help='Delete a todo item')
    parser_delete.add_argument('id', type=int, help='The ID of the todo item to delete')


def handle_add_command(args: argparse.Namespace, todo_service: TodoService) -> None:
    """
    Handle the 'add' command execution.

    Implements the logic for adding a new todo item based on command-line arguments.
    """
    description = ' '.join(args.description)

    try:
        new_todo = todo_service.add_todo(description)
        print(f"Added todo with ID {new_todo.id}: {new_todo.description}")
    except Exception as e:
        print(f"Error adding todo: {e}")


def handle_list_command(args: argparse.Namespace, todo_service: TodoService) -> None:
    """
    Handle the 'list' command execution.

    Implements the logic for listing all todo items based on command-line arguments.
    """
    todos = todo_service.list_todos()

    if not todos:
        print("No todos found.")
        return

    print("ID\tStatus\tDescription")
    print("--\t------\t-----------")

    for todo in todos:
        status = "✓" if todo.completed else "○"
        print(f"{todo.id}\t{status}\t{todo.description}")


def handle_update_command(args: argparse.Namespace, todo_service: TodoService) -> None:
    """
    Handle the 'update' command execution.

    Implements the logic for updating a todo item based on command-line arguments.
    """
    description = ' '.join(args.description)

    try:
        updated_todo = todo_service.update_todo(args.id, description)
        print(f"Updated todo with ID {updated_todo.id}: {updated_todo.description}")
    except Exception as e:
        print(f"Error updating todo: {e}")


def handle_complete_command(args: argparse.Namespace, todo_service: TodoService) -> None:
    """
    Handle the 'complete' command execution.

    Implements the logic for marking a todo as complete based on command-line arguments.
    """
    try:
        completed_todo = todo_service.mark_complete(args.id)
        print(f"Marked todo with ID {completed_todo.id} as complete: {completed_todo.description}")
    except Exception as e:
        print(f"Error marking todo as complete: {e}")


def handle_delete_command(args: argparse.Namespace, todo_service: TodoService) -> None:
    """
    Handle the 'delete' command execution.

    Implements the logic for deleting a todo item based on command-line arguments.
    """
    try:
        success = todo_service.delete_todo(args.id)
        if success:
            print(f"Deleted todo with ID {args.id}")
        else:
            print(f"Todo with ID {args.id} not found")
    except Exception as e:
        print(f"Error deleting todo: {e}")