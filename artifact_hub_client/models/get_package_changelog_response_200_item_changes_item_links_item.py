from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetPackageChangelogResponse200ItemChangesItemLinksItem")


@attr.s(auto_attribs=True)
class GetPackageChangelogResponse200ItemChangesItemLinksItem:
    """
    Attributes:
        name (str):
        url (str):
    """

    name: str
    url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        url = d.pop("url")

        get_package_changelog_response_200_item_changes_item_links_item = cls(
            name=name,
            url=url,
        )

        get_package_changelog_response_200_item_changes_item_links_item.additional_properties = d
        return get_package_changelog_response_200_item_changes_item_links_item

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
