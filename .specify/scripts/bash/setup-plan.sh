#!/bin/bash

# Setup plan script for bash
FEATURE_SPEC="specs/1-todo-app-spec/spec.md"
IMPL_PLAN="specs/1-todo-app-spec/plan.md"
SPECS_DIR="specs/1-todo-app-spec"
BRANCH="1-todo-app-spec"

# Output JSON with required information
cat << EOF
{
    "FEATURE_SPEC": "$FEATURE_SPEC",
    "IMPL_PLAN": "$IMPL_PLAN",
    "SPECS_DIR": "$SPECS_DIR",
    "BRANCH": "$BRANCH"
}
EOF