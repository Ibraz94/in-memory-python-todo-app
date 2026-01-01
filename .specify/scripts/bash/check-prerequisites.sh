#!/bin/bash

# Check prerequisites script with tasks requirement
FEATURE_DIR="specs/1-todo-app-spec"
AVAILABLE_DOCS="plan.md spec.md research.md data-model.md quickstart.md contracts/todo_operations.json tasks.md"

# Check if tasks.md exists
if [ ! -f "$FEATURE_DIR/tasks.md" ]; then
    echo "Error: tasks.md not found in $FEATURE_DIR" >&2
    exit 1
fi

# Output JSON with required information
cat << EOF
{
    "FEATURE_DIR": "$FEATURE_DIR",
    "AVAILABLE_DOCS": [
        "plan.md",
        "spec.md",
        "research.md",
        "data-model.md",
        "quickstart.md",
        "contracts/todo_operations.json",
        "tasks.md"
    ]
}
EOF