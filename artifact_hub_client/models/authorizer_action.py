from enum import Enum


class AuthorizerAction(str, Enum):
    ADDORGANIZATIONMEMBER = "addOrganizationMember"
    ADDORGANIZATIONREPOSITORY = "addOrganizationRepository"
    ALL = "all"
    DELETEORGANIZATION = "deleteOrganization"
    DELETEORGANIZATIONMEMBER = "deleteOrganizationMember"
    DELETEORGANIZATIONREPOSITORY = "deleteOrganizationRepository"
    GETAUTHORIZATIONPOLICY = "getAuthorizationPolicy"
    TRANSFERORGANIZATIONREPOSITORY = "transferOrganizationRepository"
    UPDATEAUTHORIZATIONPOLICY = "updateAuthorizationPolicy"
    UPDATEORGANIZATION = "updateOrganization"
    UPDATEORGANIZATIONREPOSITORY = "updateOrganizationRepository"

    def __str__(self) -> str:
        return str(self.value)
