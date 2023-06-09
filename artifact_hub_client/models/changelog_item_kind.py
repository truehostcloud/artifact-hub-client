from enum import Enum


class ChangelogItemKind(str, Enum):
    ADDED = "added"
    CHANGED = "changed"
    DEPRECATED = "deprecated"
    FIXED = "fixed"
    REMOVED = "removed"
    SECURITY = "security"

    def __str__(self) -> str:
        return str(self.value)
