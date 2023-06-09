from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorization_policy_policy_data import AuthorizationPolicyPolicyData


T = TypeVar("T", bound="AuthorizationPolicy")


@attr.s(auto_attribs=True)
class AuthorizationPolicy:
    """
    Attributes:
        authorization_enabled (bool):
        predefined_policy (Union[Unset, str]):  Example: rbac.v1.
        custom_policy (Union[Unset, str]):  Example: package artifacthub.authz

            # By default, deny requests
            default allow = false

            # Allow the action if the user is allowed to perform it
            allow {
              # If user's role is owner
              data.roles.owner.users[_] == input.user
            }
            allow {
              # If user's role is allowed to perform this action
              allowed_actions[_] == input.action
            }

            # Get user allowed actions
            allowed_actions[action] {
              user_roles[_] == "owner"
              action := "all"
            }
            allowed_actions[action] {
              action := data.roles[role].allowed_actions[_]
              user_roles[_] == role
            }

            # Get user roles
            user_roles[role] {
              data.roles[role].users[_] == input.user
            }
            .
        policy_data (Union[Unset, AuthorizationPolicyPolicyData]):  Example: {'roles': {'owner': {'users': ['user1']},
            'customRole1': {'users': ['member1', 'member2'], 'allowed_actions': ['addOrganizationMember',
            'addOrganizationRepository']}}}.
    """

    authorization_enabled: bool
    predefined_policy: Union[Unset, str] = UNSET
    custom_policy: Union[Unset, str] = UNSET
    policy_data: Union[Unset, "AuthorizationPolicyPolicyData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_enabled = self.authorization_enabled
        predefined_policy = self.predefined_policy
        custom_policy = self.custom_policy
        policy_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.policy_data, Unset):
            policy_data = self.policy_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorization_enabled": authorization_enabled,
            }
        )
        if predefined_policy is not UNSET:
            field_dict["predefined_policy"] = predefined_policy
        if custom_policy is not UNSET:
            field_dict["custom_policy"] = custom_policy
        if policy_data is not UNSET:
            field_dict["policy_data"] = policy_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorization_policy_policy_data import AuthorizationPolicyPolicyData

        d = src_dict.copy()
        authorization_enabled = d.pop("authorization_enabled")

        predefined_policy = d.pop("predefined_policy", UNSET)

        custom_policy = d.pop("custom_policy", UNSET)

        _policy_data = d.pop("policy_data", UNSET)
        policy_data: Union[Unset, AuthorizationPolicyPolicyData]
        if isinstance(_policy_data, Unset):
            policy_data = UNSET
        else:
            policy_data = AuthorizationPolicyPolicyData.from_dict(_policy_data)

        authorization_policy = cls(
            authorization_enabled=authorization_enabled,
            predefined_policy=predefined_policy,
            custom_policy=custom_policy,
            policy_data=policy_data,
        )

        authorization_policy.additional_properties = d
        return authorization_policy

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
