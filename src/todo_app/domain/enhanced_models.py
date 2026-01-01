"""
Enhanced domain models with priority and tags support.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class EnhancedTodoItem:
    """
    Enhanced todo item with priority and tags.
    """
    id: int
    description: str
    completed: bool = False
    priority: str = "MEDIUM"  # HIGH, MEDIUM, LOW
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validate priority."""
        if self.priority not in ["HIGH", "MEDIUM", "LOW"]:
            self.priority = "MEDIUM"
