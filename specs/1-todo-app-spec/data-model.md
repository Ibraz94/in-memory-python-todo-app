# Data Model: Todo In-Memory Python Console Application

## Todo Item Entity

**Entity Name**: TodoItem

**Fields**:
- `id` (int): Unique identifier assigned when the todo is created; auto-incremented from 1
- `description` (str): The text description of the task; required field with minimum length of 1 character
- `completed` (bool): Status indicator showing whether the task is completed (True) or pending (False); defaults to False

**Validation Rules**:
- ID must be a positive integer
- Description must not be empty or contain only whitespace
- Description length must be between 1 and 1000 characters
- Completed status must be a boolean value

**State Transitions**:
- Pending (completed=False) → Completed (completed=True) when user marks item as complete
- Completed (completed=True) → Completed (completed=True) when user attempts to mark already completed item (no change)

## Todo List Collection

**Entity Name**: TodoList

**Structure**:
- Internal storage: Dictionary mapping ID (int) to TodoItem objects
- Provides O(1) lookup by ID
- Maintains insertion order for display purposes

**Operations**:
- Add: Insert new TodoItem with next available ID
- Get All: Retrieve all TodoItem objects in insertion order
- Get by ID: Retrieve specific TodoItem by its ID
- Update: Modify existing TodoItem's properties
- Delete: Remove TodoItem by its ID
- Mark Complete: Update specific TodoItem's completed status to True

## User Session Context

**Entity Name**: SessionContext

**Fields**:
- `current_id_counter` (int): Tracks the next available ID for new todo items; starts at 1 and increments with each new item
- `todos` (dict): The collection of all TodoItem objects for the current session

**Constraints**:
- The session context exists only for the duration of the application run
- All data is lost when the application terminates
- Maximum recommended number of items: 1000 (for performance considerations)