from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_package_changelog_response_200_item_changes_item import (
        GetPackageChangelogResponse200ItemChangesItem,
    )


T = TypeVar("T", bound="GetPackageChangelogResponse200Item")


@attr.s(auto_attribs=True)
class GetPackageChangelogResponse200Item:
    """
    Attributes:
        version (str):
        ts (int):
        contains_security_updates (bool):
        prerelease (bool):
        changes (Union[Unset, List['GetPackageChangelogResponse200ItemChangesItem']]):
    """

    version: str
    ts: int
    contains_security_updates: bool
    prerelease: bool
    changes: Union[Unset, List["GetPackageChangelogResponse200ItemChangesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        ts = self.ts
        contains_security_updates = self.contains_security_updates
        prerelease = self.prerelease
        changes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()

                changes.append(changes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "ts": ts,
                "contains_security_updates": contains_security_updates,
                "prerelease": prerelease,
            }
        )
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_package_changelog_response_200_item_changes_item import (
            GetPackageChangelogResponse200ItemChangesItem,
        )

        d = src_dict.copy()
        version = d.pop("version")

        ts = d.pop("ts")

        contains_security_updates = d.pop("contains_security_updates")

        prerelease = d.pop("prerelease")

        changes = []
        _changes = d.pop("changes", UNSET)
        for changes_item_data in _changes or []:
            changes_item = GetPackageChangelogResponse200ItemChangesItem.from_dict(changes_item_data)

            changes.append(changes_item)

        get_package_changelog_response_200_item = cls(
            version=version,
            ts=ts,
            contains_security_updates=contains_security_updates,
            prerelease=prerelease,
            changes=changes,
        )

        get_package_changelog_response_200_item.additional_properties = d
        return get_package_changelog_response_200_item

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
