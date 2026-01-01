<!--
Sync Impact Report:
- Version change: 2.0.0 → 2.1.0
- Modified principles: Added new principle for Rich library requirement (XI), shifted existing principles
- Added sections: Enhanced Terminal UI with Rich Library requirement (XI)
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
- Follow-up TODOs: Update implementation to use Rich library instead of basic print statements
-->

# Todo In-Memory Python Console Application Constitution

## Project Purpose

The Todo In-Memory Python Console Application is a terminal-based task management system that stores all todos strictly in memory. The application provides a simple, fast, and lightweight solution for personal task tracking without any persistent storage requirements. The application must run entirely in the terminal and support only the five basic features: add todo, view todos, update todo, delete todo, and mark todo as complete.

## Core Principles

### I. Spec-Driven Development (MANDATORY)
All development must follow the Claude Code and Spec-Kit Plus methodology. No manual coding is permitted outside of agent execution. All features must begin with clear specifications in the specs/ directory before any implementation work begins. Changes follow the specs/ → tasks/ → implementation pattern.

### II. AI-Assisted Development (MANDATORY)
AI assistance is required as a core development practice. All AI contributions must be properly attributed using co-author tags in commits. No manual coding outside of agent execution is permitted.

### III. Test-First Development (MANDATORY)
TDD is non-negotiable: Tests must be written first → User approved → Tests fail → Then implement; Red-Green-Refactor cycle is strictly enforced. All features must have comprehensive test coverage before acceptance.

### IV. Proper Attribution (MANDATORY)
All contributions, including AI contributions, must be properly tracked and acknowledged in CONTRIBUTORS.md and commit history. All AI-assisted changes require co-author attribution following the project's AI contribution tracking protocol.

### V. Clean Architecture (MANDATORY)
Maintain separation of concerns with clear, modular code structure. Follow SpecKit Plus standards for project organization. Application components must be properly separated with clear interfaces and minimal coupling.

### VI. Traceability (MANDATORY)
Complete traceability from specifications to implementation is required. Every code change must be linked to a specific task in tasks.md, which must be linked to a specification in spec.md. All development must be traceable through Prompt History Records (PHRs).

## Technical Constraints

### VII. Python Version (MANDATORY)
The application must use Python 3.13 or higher. No other Python versions are permitted. This constraint ensures access to the latest language features and performance improvements.

### VIII. Package Management (MANDATORY)
The application must be managed and executed using the UV Python package manager for environment setup and dependency management. No other package managers (pip, conda, etc.) are permitted for this project.

### IX. In-Memory Storage (MANDATORY)
All todos must be stored strictly in memory. No persistent storage mechanisms (files, databases, etc.) are allowed. Data will be lost when the application terminates, which is an intentional design constraint.

### X. Terminal-Only Interface (MANDATORY)
The application must run entirely in the terminal. No GUI, web interface, or other external interfaces are permitted. All user interaction must occur through command-line input and output.

### XI. Enhanced Terminal UI with Rich Library (MANDATORY)
All terminal user interactions must be implemented using the Python Rich library. This includes interactive questionnaires, menu selection, confirmation prompts, and formatted output such as tables and status indicators. Plain input()-based interactions are strictly prohibited. The Rich library provides enhanced formatting, colors, tables, progress bars, and other visual elements that improve the user experience in the terminal environment.

## Feature Scope

### XII. Minimal Feature Set (MANDATORY)
The application must support only the five basic features: add todo, view todos, update todo, delete todo, and mark todo as complete. No additional features, extensions, or functionality beyond these core features are permitted without explicit constitution amendment.

### XIII. No Manual Overrides (MANDATORY)
No manual coding outside of agent execution is permitted. All code changes must be made through Claude Code and Spec-Kit Plus workflows. Direct editing of files without agent execution is strictly prohibited.

## Quality Standards

### XIV. Clean Code (MANDATORY)
Code must be clean, well-documented, and maintainable. Follow PEP 8 standards and Python best practices. All functions, classes, and modules must include appropriate docstrings and type hints.

### XV. Error Handling (MANDATORY)
Proper error handling and input validation are required. The application must gracefully handle invalid inputs, edge cases, and unexpected conditions without crashing.

### XVI. Performance (MANDATORY)
Performance considerations for in-memory storage must be maintained. Operations should remain efficient even as the number of todos grows.

## Development Workflow

All changes must:
- Follow the specs/ → tasks/ → implementation pattern as mandated by Spec-Kit Plus
- Include proper attribution for AI contributions using co-author tags
- Maintain the history/adr/ and history/prompts/ directories
- Pass all existing tests before merging
- Include comprehensive Prompt History Records (PHRs) for all development activities
- Be traceable from specification through implementation

## Governance

This constitution supersedes all other practices. Amendments require formal documentation, approval, and migration plan. All PRs and reviews must verify compliance with these principles before acceptance.

**Version**: 2.1.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2026-01-01
