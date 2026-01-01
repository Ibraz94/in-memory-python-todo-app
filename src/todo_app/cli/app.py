"""
Main CLI application for the Todo In-Memory Python Console Application.

This module implements the main entry point for the command-line interface,
coordinating all CLI operations and providing the primary user interaction.
"""

import argparse
import sys
from todo_app.services.todo_service import TodoService
from todo_app.services.memory_store import MemoryStore
from todo_app.cli import commands


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the CLI application.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description='Todo In-Memory Python Console Application',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Add a new todo: todo-app add "Buy groceries"
  List all todos: todo-app list
  Mark as complete: todo-app complete 1
  Update a todo: todo-app update 1 "Buy groceries and cook dinner"
  Delete a todo: todo-app delete 1
        """.strip()
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command parsers
    commands.add_command_parser(subparsers)
    commands.list_command_parser(subparsers)
    commands.update_command_parser(subparsers)
    commands.complete_command_parser(subparsers)
    commands.delete_command_parser(subparsers)

    return parser


def main() -> None:
    """
    Main entry point for the CLI application.

    This function parses command-line arguments, initializes the application
    services, and executes the appropriate command handler.
    """
    # Create the argument parser
    parser = create_parser()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Parse the arguments
    args = parser.parse_args()

    # Initialize the memory store and todo service
    memory_store = MemoryStore()
    todo_service = TodoService(memory_store)

    # Execute the appropriate command based on the subcommand
    if args.command == 'add':
        commands.handle_add_command(args, todo_service)
    elif args.command == 'list':
        commands.handle_list_command(args, todo_service)
    elif args.command == 'update':
        commands.handle_update_command(args, todo_service)
    elif args.command == 'complete':
        commands.handle_complete_command(args, todo_service)
    elif args.command == 'delete':
        commands.handle_delete_command(args, todo_service)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()