from enum import Enum


class SearchPackagesSort(str, Enum):
    RELEVANCE = "relevance"
    STARS = "stars"

    def __str__(self) -> str:
        return str(self.value)
