from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Maintainer")


@attr.s(auto_attribs=True)
class Maintainer:
    """
    Attributes:
        name (str):  Example: maintainer1.
        email (str):  Example: maintainer@email.com.
        maintainer_id (Union[Unset, str]):
    """

    name: str
    email: str
    maintainer_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        maintainer_id = self.maintainer_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
            }
        )
        if maintainer_id is not UNSET:
            field_dict["maintainer_id"] = maintainer_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        email = d.pop("email")

        maintainer_id = d.pop("maintainer_id", UNSET)

        maintainer = cls(
            name=name,
            email=email,
            maintainer_id=maintainer_id,
        )

        maintainer.additional_properties = d
        return maintainer

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
