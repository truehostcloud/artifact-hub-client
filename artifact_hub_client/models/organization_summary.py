from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationSummary")


@attr.s(auto_attribs=True)
class OrganizationSummary:
    """
    Attributes:
        name (str):  Example: org1.
        display_name (Union[Unset, str]):  Example: Organization 1.
        description (Union[Unset, str]):  Example: description.
        home_url (Union[Unset, str]):  Example: http://url.
        logo_image_id (Union[Unset, str]):  Example: 12345abcde.
    """

    name: str
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    home_url: Union[Unset, str] = UNSET
    logo_image_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        description = self.description
        home_url = self.home_url
        logo_image_id = self.logo_image_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if home_url is not UNSET:
            field_dict["home_url"] = home_url
        if logo_image_id is not UNSET:
            field_dict["logo_image_id"] = logo_image_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        home_url = d.pop("home_url", UNSET)

        logo_image_id = d.pop("logo_image_id", UNSET)

        organization_summary = cls(
            name=name,
            display_name=display_name,
            description=description,
            home_url=home_url,
            logo_image_id=logo_image_id,
        )

        organization_summary.additional_properties = d
        return organization_summary

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
