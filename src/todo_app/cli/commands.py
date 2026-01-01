"""
CLI command definitions for the Todo In-Memory Python Console Application with Rich UI.

This module defines the command-line interface commands that map to
the core functionality of the application using Rich components for enhanced UI.
"""
import argparse
from typing import Any
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import print

from ..services.todo_service import TodoService
from ..domain.exceptions import TodoNotFoundError, InvalidTodoError


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


def handle_add_command(args: argparse.Namespace, todo_service: TodoService, console: Console) -> None:
    """
    Handle the 'add' command execution with Rich UI components.

    Implements the logic for adding a new todo item based on command-line arguments.
    """
    description = ' '.join(args.description)

    try:
        new_todo = todo_service.add_todo(description)
        print(f"[green]+[/green] Added todo with ID [bold]{new_todo.id}[/bold]: {new_todo.description}")
    except InvalidTodoError as e:
        print(f"[red]X Error adding todo:[/red] {e}")
    except Exception as e:
        print(f"[red]X Unexpected error adding todo:[/red] {e}")


def handle_list_command(args: argparse.Namespace, todo_service: TodoService, console: Console) -> None:
    """
    Handle the 'list' command execution with Rich UI components.

    Implements the logic for listing all todo items based on command-line arguments.
    """
    try:
        todos = todo_service.list_todos()

        if not todos:
            print("[yellow]No todos found.[/yellow]")
            return

        # Create a Rich table for displaying todos
        table = Table(title="Todo List")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Status", width=8)
        table.add_column("Description", min_width=20)

        for todo in todos:
            status = "[green]DONE[/green]" if todo.completed else "[red]TODO[/red]"
            description = "[strikethrough]" + todo.description if todo.completed else todo.description
            table.add_row(str(todo.id), status, description)

        console.print(table)

    except Exception as e:
        print(f"[red]X Error listing todos:[/red] {e}")


def handle_update_command(args: argparse.Namespace, todo_service: TodoService, console: Console) -> None:
    """
    Handle the 'update' command execution with Rich UI components.

    Implements the logic for updating a todo item based on command-line arguments.
    """
    description = ' '.join(args.description)

    try:
        updated_todo = todo_service.update_todo(args.id, description)
        print(f"[green]+[/green] Updated todo with ID [bold]{updated_todo.id}[/bold]: {updated_todo.description}")
    except TodoNotFoundError as e:
        print(f"[red]X Error updating todo:[/red] {e}")
    except InvalidTodoError as e:
        print(f"[red]X Error updating todo:[/red] {e}")
    except Exception as e:
        print(f"[red]X Unexpected error updating todo:[/red] {e}")


def handle_complete_command(args: argparse.Namespace, todo_service: TodoService, console: Console) -> None:
    """
    Handle the 'complete' command execution with Rich UI components.

    Implements the logic for marking a todo as complete based on command-line arguments.
    """
    try:
        completed_todo = todo_service.mark_complete(args.id)
        print(f"[green]+[/green] Marked todo with ID [bold]{completed_todo.id}[/bold] as complete: {completed_todo.description}")
    except TodoNotFoundError as e:
        print(f"[red]X Error marking todo as complete:[/red] {e}")
    except Exception as e:
        print(f"[red]X Unexpected error marking todo as complete:[/red] {e}")


def handle_delete_command(args: argparse.Namespace, todo_service: TodoService, console: Console) -> None:
    """
    Handle the 'delete' command execution with Rich UI components.

    Implements the logic for deleting a todo item based on command-line arguments.
    """
    try:
        # First, get the todo to show its details before deletion
        todo = todo_service.get_todo(args.id)

        # Confirm deletion with Rich confirmation dialog
        confirm = Confirm.ask(f"[yellow]Are you sure you want to delete todo '{todo.description}'?[/yellow]")

        if confirm:
            success = todo_service.delete_todo(args.id)
            if success:
                print(f"[green]+[/green] Deleted todo with ID [bold]{args.id}[/bold]")
            else:
                print(f"[red]X[/red] Failed to delete todo with ID [bold]{args.id}[/bold]")
        else:
            print("[blue]Deletion cancelled.[/blue]")

    except TodoNotFoundError as e:
        print(f"[red]X Error deleting todo:[/red] {e}")
    except Exception as e:
        print(f"[red]X Unexpected error deleting todo:[/red] {e}")