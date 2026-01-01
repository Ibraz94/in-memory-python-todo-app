"""
Main CLI application for the Todo In-Memory Python Console Application with Rich UI.

This module implements the main entry point for the command-line interface,
coordinating all CLI operations and providing the primary user interaction
with Rich-based formatting and components.
"""
import argparse
import sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import print

from ..services.todo_service import TodoService
from ..services.memory_store import MemoryStore
from ..services.csv_store import CsvStore
from . import commands


def create_parser(console: Console) -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the CLI application.

    Args:
        console: The Rich console instance for UI components

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description='Todo In-Memory Python Console Application with Rich UI',
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


def interactive_mode(console: Console, todo_service: TodoService) -> None:
    """
    Run the application in interactive mode with Rich questionnaire.
    
    This mode keeps the app running and maintains todos in memory across operations.
    """
    from rich.prompt import Prompt, IntPrompt
    
    # Display welcome banner
    console.print(Panel.fit(
        "[bold cyan]Todo In-Memory App[/bold cyan]\n",
        border_style="cyan"
    ))
    
    while True:
        console.print("\n[bold]What would you like to do?[/bold]")
        console.print("1. Add a new todo")
        console.print("2. List all todos")
        console.print("3. Mark todo as complete")
        console.print("4. Update a todo")
        console.print("5. Delete a todo")
        console.print("6. Exit")
        
        choice = Prompt.ask("\n[cyan]Choose an option[/cyan]", choices=["1", "2", "3", "4", "5", "6"])
        
        try:
            if choice == "1":
                description = Prompt.ask("[green]Enter todo description[/green]")
                new_todo = todo_service.add_todo(description)
                console.print(f"[green]✓[/green] Added todo with ID [bold]{new_todo.id}[/bold]: {new_todo.description}")
                
            elif choice == "2":
                todos = todo_service.list_todos()
                if not todos:
                    console.print("[yellow]No todos found.[/yellow]")
                else:
                    table = Table(title="Todo List")
                    table.add_column("ID", style="dim", width=5)
                    table.add_column("Status", width=8)
                    table.add_column("Description", min_width=20)
                    
                    for todo in todos:
                        status = "[green]DONE[/green]" if todo.completed else "[red]TODO[/red]"
                        description = "[strikethrough]" + todo.description if todo.completed else todo.description
                        table.add_row(str(todo.id), status, description)
                    
                    console.print(table)
                    
            elif choice == "3":
                todo_id = IntPrompt.ask("[cyan]Enter todo ID to mark as complete[/cyan]")
                completed_todo = todo_service.mark_complete(todo_id)
                console.print(f"[green]✓[/green] Marked todo [bold]{completed_todo.id}[/bold] as complete: {completed_todo.description}")
                
            elif choice == "4":
                todo_id = IntPrompt.ask("[cyan]Enter todo ID to update[/cyan]")
                new_description = Prompt.ask("[green]Enter new description[/green]")
                updated_todo = todo_service.update_todo(todo_id, new_description)
                console.print(f"[green]✓[/green] Updated todo [bold]{updated_todo.id}[/bold]: {updated_todo.description}")
                
            elif choice == "5":
                todo_id = IntPrompt.ask("[cyan]Enter todo ID to delete[/cyan]")
                todo = todo_service.get_todo(todo_id)
                from rich.prompt import Confirm
                if Confirm.ask(f"[yellow]Delete '{todo.description}'?[/yellow]"):
                    todo_service.delete_todo(todo_id)
                    console.print(f"[green]✓[/green] Deleted todo [bold]{todo_id}[/bold]")
                else:
                    console.print("[blue]Cancelled.[/blue]")
                    
            elif choice == "6":
                console.print("[cyan]Goodbye! Your todos will be lost (in-memory app).[/cyan]")
                break
                
        except Exception as e:
            console.print(f"[red]✗ Error:[/red] {e}")


def main() -> None:
    """
    Main entry point for the CLI application.

    This function parses command-line arguments, initializes the application
    services, and executes the appropriate command handler with Rich UI components.
    """
    # Create a Rich console for enhanced UI with proper encoding for Windows
    console = Console(force_terminal=True, force_interactive=True)

    # Initialize the CSV store and todo service (shared across all commands)
    # This provides persistent storage while maintaining in-memory performance
    csv_store = CsvStore("todos.csv")
    todo_service = TodoService(csv_store)

    # If no arguments provided, start interactive mode
    if len(sys.argv) == 1:
        interactive_mode(console, todo_service)
        sys.exit(0)

    # Create the argument parser
    parser = create_parser(console)

    # Parse the arguments
    args = parser.parse_args()

    # Execute the appropriate command based on the subcommand
    if args.command == 'add':
        commands.handle_add_command(args, todo_service, console)
    elif args.command == 'list':
        commands.handle_list_command(args, todo_service, console)
    elif args.command == 'update':
        commands.handle_update_command(args, todo_service, console)
    elif args.command == 'complete':
        commands.handle_complete_command(args, todo_service, console)
    elif args.command == 'delete':
        commands.handle_delete_command(args, todo_service, console)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()