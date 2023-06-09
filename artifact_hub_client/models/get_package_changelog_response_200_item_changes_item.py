from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.changelog_item_kind import ChangelogItemKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_package_changelog_response_200_item_changes_item_links_item import (
        GetPackageChangelogResponse200ItemChangesItemLinksItem,
    )


T = TypeVar("T", bound="GetPackageChangelogResponse200ItemChangesItem")


@attr.s(auto_attribs=True)
class GetPackageChangelogResponse200ItemChangesItem:
    """
    Attributes:
        description (str):
        kind (Union[Unset, ChangelogItemKind]): Types of changes:
              * `added` - New features
              * `changed` - Changes in existing functionality
              * `deprecated` - Soon-to-be removed features
              * `removed` - Removed features
              * `fixed` - Any bug fixed
              * `security` - In case of vulnerabilities
        links (Union[Unset, List['GetPackageChangelogResponse200ItemChangesItemLinksItem']]):
    """

    description: str
    kind: Union[Unset, ChangelogItemKind] = UNSET
    links: Union[Unset, List["GetPackageChangelogResponse200ItemChangesItemLinksItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_package_changelog_response_200_item_changes_item_links_item import (
            GetPackageChangelogResponse200ItemChangesItemLinksItem,
        )

        d = src_dict.copy()
        description = d.pop("description")

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ChangelogItemKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ChangelogItemKind(_kind)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = GetPackageChangelogResponse200ItemChangesItemLinksItem.from_dict(links_item_data)

            links.append(links_item)

        get_package_changelog_response_200_item_changes_item = cls(
            description=description,
            kind=kind,
            links=links,
        )

        get_package_changelog_response_200_item_changes_item.additional_properties = d
        return get_package_changelog_response_200_item_changes_item

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
