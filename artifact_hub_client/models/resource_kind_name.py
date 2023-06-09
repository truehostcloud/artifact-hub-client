from enum import Enum


class ResourceKindName(str, Enum):
    ORGANIZATIONNAME = "organizationName"
    REPOSITORYNAME = "repositoryName"
    REPOSITORYURL = "repositoryURL"
    USERALIAS = "userAlias"

    def __str__(self) -> str:
        return str(self.value)
