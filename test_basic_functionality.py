#!/usr/bin/env python3
"""
Basic test script to verify the Todo In-Memory Python Console Application functionality.
"""

import sys
import os

# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.todo_app.services.todo_service import TodoService
from src.todo_app.services.memory_store import MemoryStore


def test_basic_functionality():
    """Test the basic functionality of the todo application."""
    print("Testing basic functionality...")

    # Create a fresh memory store and service
    memory_store = MemoryStore()
    service = TodoService(memory_store)

    # Test 1: Add a todo item
    print("\n1. Testing add functionality...")
    todo1 = service.add_todo("Buy groceries")
    print(f"   Added todo: ID={todo1.id}, Description='{todo1.description}', Completed={todo1.completed}")
    assert todo1.id == 1, f"Expected ID 1, got {todo1.id}"
    assert todo1.description == "Buy groceries", f"Expected 'Buy groceries', got '{todo1.description}'"
    assert todo1.completed == False, f"Expected False, got {todo1.completed}"
    print("   [PASS] Add functionality works correctly")

    # Test 2: Add another todo item
    print("\n2. Testing add second item...")
    todo2 = service.add_todo("Walk the dog")
    print(f"   Added todo: ID={todo2.id}, Description='{todo2.description}', Completed={todo2.completed}")
    assert todo2.id == 2, f"Expected ID 2, got {todo2.id}"
    assert todo2.description == "Walk the dog", f"Expected 'Walk the dog', got '{todo2.description}'"
    print("   [PASS] Second item added with correct ID")

    # Test 3: List all todos
    print("\n3. Testing list functionality...")
    todos = service.list_todos()
    print(f"   Found {len(todos)} todos")
    assert len(todos) == 2, f"Expected 2 todos, got {len(todos)}"
    assert todos[0].id == 1 and todos[0].description == "Buy groceries"
    assert todos[1].id == 2 and todos[1].description == "Walk the dog"
    print("   [PASS] List functionality works correctly")

    # Test 4: Mark a todo as complete
    print("\n4. Testing mark complete functionality...")
    completed_todo = service.mark_complete(1)
    print(f"   Marked todo as complete: ID={completed_todo.id}, Completed={completed_todo.completed}")
    assert completed_todo.completed == True, f"Expected True, got {completed_todo.completed}"
    print("   [PASS] Mark complete functionality works correctly")

    # Test 5: Update a todo description
    print("\n5. Testing update functionality...")
    updated_todo = service.update_todo(2, "Walk the cat instead")
    print(f"   Updated todo: ID={updated_todo.id}, Description='{updated_todo.description}'")
    assert updated_todo.description == "Walk the cat instead", f"Expected 'Walk the cat instead', got '{updated_todo.description}'"
    print("   [PASS] Update functionality works correctly")

    # Test 6: Delete a todo
    print("\n6. Testing delete functionality...")
    delete_result = service.delete_todo(1)
    print(f"   Delete result: {delete_result}")
    assert delete_result == True, f"Expected True, got {delete_result}"

    # Verify it's gone
    remaining_todos = service.list_todos()
    print(f"   Remaining todos after deletion: {len(remaining_todos)}")
    assert len(remaining_todos) == 1, f"Expected 1 todo after deletion, got {len(remaining_todos)}"
    assert remaining_todos[0].id == 2, f"Expected remaining todo ID to be 2, got {remaining_todos[0].id}"
    print("   [PASS] Delete functionality works correctly")

    # Test 7: Try to delete a non-existent todo
    print("\n7. Testing delete non-existent todo...")
    delete_result = service.delete_todo(999)
    print(f"   Delete result for non-existent todo: {delete_result}")
    assert delete_result == False, f"Expected False for non-existent todo, got {delete_result}"
    print("   [PASS] Non-existent todo deletion handled correctly")

    print("\n[SUCCESS] All basic functionality tests passed!")


def test_error_handling():
    """Test error handling functionality."""
    print("\n\nTesting error handling...")

    memory_store = MemoryStore()
    service = TodoService(memory_store)

    # Test 1: Add empty todo description
    print("\n1. Testing empty description validation...")
    try:
        service.add_todo("")
        assert False, "Expected ValueError for empty description"
    except ValueError as e:
        print(f"   Correctly caught error: {e}")
        print("   [PASS] Empty description validation works")

    # Test 2: Add whitespace-only description
    print("\n2. Testing whitespace-only description validation...")
    try:
        service.add_todo("   ")
        assert False, "Expected ValueError for whitespace-only description"
    except ValueError as e:
        print(f"   Correctly caught error: {e}")
        print("   [PASS] Whitespace-only description validation works")

    # Test 3: Update with empty description
    print("\n3. Testing update with empty description...")
    todo = service.add_todo("Test item")
    try:
        service.update_todo(todo.id, "")
        assert False, "Expected ValueError for empty update description"
    except ValueError as e:
        print(f"   Correctly caught error: {e}")
        print("   [PASS] Empty update description validation works")

    # Test 4: Try to get non-existent todo
    print("\n4. Testing retrieval of non-existent todo...")
    try:
        service.get_todo(999)
        assert False, "Expected TodoNotFoundError for non-existent todo"
    except Exception as e:
        print(f"   Correctly caught error: {type(e).__name__}")
        print("   [PASS] Non-existent todo retrieval handled correctly")

    print("\n[SUCCESS] All error handling tests passed!")


if __name__ == "__main__":
    print("Starting Todo Application Tests...")

    try:
        test_basic_functionality()
        test_error_handling()

        print("\n" + "="*50)
        print("[SUCCESS] ALL TESTS PASSED!")
        print("The Todo In-Memory Python Console Application is working correctly.")
        print("="*50)

    except Exception as e:
        print(f"\n[ERROR] TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)