from enum import Enum


class PackageBaseSignaturesItem(str, Enum):
    COSIGN = "cosign"
    PROV = "prov"

    def __str__(self) -> str:
        return str(self.value)
