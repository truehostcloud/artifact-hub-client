from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        alias (str):  Example: jdoe.
        email (str):  Example: jdoe@email.com.
        password_set (bool):
        first_name (Union[Unset, str]):  Example: John.
        last_name (Union[Unset, str]):  Example: Doe.
        profile_image_id (Union[Unset, str]):  Example: 12345abcde.
        tfa_enabled (Union[Unset, bool]):
    """

    alias: str
    email: str
    password_set: bool
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    profile_image_id: Union[Unset, str] = UNSET
    tfa_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias
        email = self.email
        password_set = self.password_set
        first_name = self.first_name
        last_name = self.last_name
        profile_image_id = self.profile_image_id
        tfa_enabled = self.tfa_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
                "email": email,
                "password_set": password_set,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if profile_image_id is not UNSET:
            field_dict["profile_image_id"] = profile_image_id
        if tfa_enabled is not UNSET:
            field_dict["tfa_enabled"] = tfa_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias = d.pop("alias")

        email = d.pop("email")

        password_set = d.pop("password_set")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        profile_image_id = d.pop("profile_image_id", UNSET)

        tfa_enabled = d.pop("tfa_enabled", UNSET)

        user = cls(
            alias=alias,
            email=email,
            password_set=password_set,
            first_name=first_name,
            last_name=last_name,
            profile_image_id=profile_image_id,
            tfa_enabled=tfa_enabled,
        )

        user.additional_properties = d
        return user

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
