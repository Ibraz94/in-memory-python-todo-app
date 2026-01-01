# Data Model: Rich UI Todo Application

## Entities

### Todo
- **id**: Unique identifier (integer, auto-generated)
- **description**: Text content of the todo (string, required, max 500 characters)
- **completed**: Boolean indicating completion status (boolean, default: false)
- **created_at**: Timestamp when todo was created (datetime, auto-generated)

### TodoList
- **todos**: Collection of Todo entities (list/array)
- **total_count**: Number of todos in the list (integer, calculated)
- **completed_count**: Number of completed todos (integer, calculated)
- **pending_count**: Number of pending todos (integer, calculated)

## Relationships
- TodoList contains multiple Todo entities
- Each Todo belongs to exactly one TodoList (in-memory instance)

## Constraints
- Todo descriptions must not be empty or contain only whitespace
- Todo IDs must be unique within a single TodoList instance
- TodoList operations must maintain data consistency in memory
- No persistent storage - all data is lost when application terminates

## State Transitions
- Todo starts as incomplete (completed: false)
- Todo can transition to complete (completed: true) via mark_complete operation
- Todo can be updated with new description while maintaining completion status
- Todo can be deleted, removing it from the TodoList