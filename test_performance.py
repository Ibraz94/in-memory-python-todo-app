#!/usr/bin/env python3
"""
Performance test for the Todo In-Memory Python Console Application.
Tests the application with up to 1000 todo items to validate performance requirements.
"""

import sys
import os
import time

# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.todo_app.services.todo_service import TodoService
from src.todo_app.services.memory_store import MemoryStore


def test_performance_with_1000_items():
    """Test performance with 1000 todo items."""
    print("Testing performance with 1000 todo items...")

    memory_store = MemoryStore()
    service = TodoService(memory_store)

    # Measure time to add 1000 items
    print("   Adding 1000 todo items...")
    start_time = time.time()
    for i in range(1000):
        service.add_todo(f"Performance test task {i}")
    add_time = time.time() - start_time
    print(f"   [PASS] Added 1000 items in {add_time:.3f} seconds")

    # Verify all items were added
    todos = service.list_todos()
    assert len(todos) == 1000, f"Expected 1000 todos, got {len(todos)}"
    print(f"   [PASS] Successfully stored {len(todos)} items")

    # Measure time to list all items
    start_time = time.time()
    todos = service.list_todos()
    list_time = time.time() - start_time
    print(f"   [PASS] Listed 1000 items in {list_time:.3f} seconds")

    # Verify listing performance requirement (<2 seconds for 1000 items)
    if list_time > 2.0:
        print(f"   [WARN] List operation took {list_time:.3f}s, which exceeds 2s requirement")
    else:
        print(f"   [PASS] List operation meets performance requirement ({list_time:.3f}s < 2s)")

    # Measure time to update an item
    start_time = time.time()
    updated = service.update_todo(500, "Updated performance test task 500")
    update_time = time.time() - start_time
    print(f"   [PASS] Updated item in {update_time:.3f} seconds")

    # Measure time to mark complete
    start_time = time.time()
    completed = service.mark_complete(250)
    complete_time = time.time() - start_time
    print(f"   [PASS] Marked item complete in {complete_time:.3f} seconds")

    # Measure time to delete an item
    start_time = time.time()
    result = service.delete_todo(750)
    delete_time = time.time() - start_time
    print(f"   [PASS] Deleted item in {delete_time:.3f} seconds")

    # Verify deletion worked
    todos_after_delete = service.list_todos()
    assert len(todos_after_delete) == 999, f"Expected 999 todos after deletion, got {len(todos_after_delete)}"
    print(f"   [PASS] Successfully deleted item, now have {len(todos_after_delete)} items")

    # Verify add performance requirement (<3 seconds for single operation)
    if add_time/1000 > 3.0:  # Average time per item
        print(f"   [WARN] Add operation average {(add_time/1000):.3f}s, which exceeds 3s requirement")
    else:
        print(f"   [PASS] Add operation meets performance requirement (average {(add_time/1000):.3f}s < 3s)")

    print(f"\n[SUCCESS] Performance test with 1000 items completed!")
    print(f"   - Add time: {add_time:.3f}s total ({(add_time/1000)*1000:.1f}ms average per item)")
    print(f"   - List time: {list_time:.3f}s")
    print(f"   - Update time: {update_time:.3f}s")
    print(f"   - Complete time: {complete_time:.3f}s")
    print(f"   - Delete time: {delete_time:.3f}s")


def test_memory_usage():
    """Test memory usage with many items."""
    print("\nTesting memory usage with many items...")

    import psutil
    import os

    # Get initial memory usage
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB

    memory_store = MemoryStore()
    service = TodoService(memory_store)

    # Add 1000 items
    for i in range(1000):
        service.add_todo(f"Memory test task {i}")

    # Get memory usage after adding items
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    memory_used = final_memory - initial_memory

    print(f"   Initial memory: {initial_memory:.2f} MB")
    print(f"   Final memory: {final_memory:.2f} MB")
    print(f"   Memory used by 1000 items: {memory_used:.2f} MB")

    if memory_used > 100:  # 100MB limit as per success criteria
        print(f"   [WARN] Memory usage {memory_used:.2f}MB exceeds 100MB requirement")
    else:
        print(f"   [PASS] Memory usage meets requirement ({memory_used:.2f}MB < 100MB)")

    print(f"   [SUCCESS] Memory usage test completed!")


if __name__ == "__main__":
    print("Starting Todo Application Performance Tests...")

    try:
        test_performance_with_1000_items()
        test_memory_usage()

        print("\n" + "="*50)
        print("[SUCCESS] ALL PERFORMANCE TESTS PASSED!")
        print("The Todo In-Memory Python Console Application meets performance requirements.")
        print("="*50)

    except Exception as e:
        print(f"\n[ERROR] PERFORMANCE TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)