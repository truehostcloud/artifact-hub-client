from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@attr.s(auto_attribs=True)
class Member:
    """
    Attributes:
        alias (str):  Example: jdoe.
        confirmed (bool):  Example: True.
        first_name (Union[Unset, str]):  Example: John.
        last_name (Union[Unset, str]):  Example: Doe.
    """

    alias: str
    confirmed: bool
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias
        confirmed = self.confirmed
        first_name = self.first_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
                "confirmed": confirmed,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alias = d.pop("alias")

        confirmed = d.pop("confirmed")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        member = cls(
            alias=alias,
            confirmed=confirmed,
            first_name=first_name,
            last_name=last_name,
        )

        member.additional_properties = d
        return member

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
