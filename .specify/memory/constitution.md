# Todo App Constitution

## Core Principles

### I. AI-Assisted Development
AI assistance is embraced as a core development practice. All AI contributions are properly attributed using co-author tags in commits.

### II. Spec-Driven Development
All features begin with clear specifications before implementation. Changes follow the specs/ → history/ pattern.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced.

### IV. Proper Attribution
All contributions, including AI contributions, are properly tracked and acknowledged in CONTRIBUTORS.md and commit history.

### V. Clean Architecture
Maintain separation of concerns with clear, modular code structure. Follow SpecKit Plus standards for project organization.

### VI. Documentation First
All features and decisions are documented before or during implementation, not after.

## Development Workflow

All changes must:
- Follow the specs/ directory structure for feature planning
- Include proper attribution for AI contributions
- Maintain the history/adr/ and history/prompts/ directories
- Pass all existing tests before merging

## Quality Standards

- Code must be clean, well-documented, and maintainable
- All AI contributions must be clearly identified
- Proper error handling and input validation required
- Performance considerations for in-memory storage

## Governance

This constitution supersedes all other practices. Amendments require documentation, approval, and migration plan.

All PRs/reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30
