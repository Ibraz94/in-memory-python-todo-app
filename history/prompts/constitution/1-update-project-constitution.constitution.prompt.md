---
id: 1
title: "Update Project Constitution"
stage: constitution
date_iso: 2025-12-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["governance", "constitution", "spec-driven-development"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - .specify/memory/constitution.md
tests_yaml: []
---

# Constitution Update Prompt

## User Input
```
You are acting as a spec-driven software architect using an agentic development workflow. Create a Project Constitution for a Todo In-Memory Python Console Application. The constitution must define immutable rules governing the entire project, including the project purpose, development methodology, technical constraints, quality standards, and review criteria. Explicitly mandate spec-driven development using Claude Code and Spec-Kit Plus, and clearly prohibit manual coding outside of agent execution. Specify that the application must use Python 3.13 or higher and must be managed and executed using the UV Python package manager for environment setup and dependency management. The application must run entirely in the terminal, store all todos strictly in memory, and support only the five basic features: add todo, view todos, update todo, delete todo, and mark todo as complete. Include rules for clean code, proper project structure, separation of concerns, and traceability from specifications to implementation.
```

## Response Summary
Updated the project constitution to version 2.0.0 with comprehensive rules for the Todo In-Memory Python Console Application. The new constitution includes:

- Project purpose defining the terminal-based in-memory todo application
- Core principles mandating spec-driven development, AI-assisted development, test-first approach, proper attribution, clean architecture, and traceability
- Technical constraints specifying Python 3.13+, UV package manager, in-memory storage, and terminal-only interface
- Feature scope limiting to the five basic todo operations
- Quality standards for clean code, error handling, and performance
- Development workflow requirements
- Governance procedures

The constitution explicitly prohibits manual coding outside of agent execution and mandates Claude Code and Spec-Kit Plus methodologies.

## Outcome
Successfully updated the project constitution at `.specify/memory/constitution.md` to version 2.0.0, incorporating all specified requirements for the Todo In-Memory Python Console Application.