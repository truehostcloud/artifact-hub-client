from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPackageStatsResponse200")


@attr.s(auto_attribs=True)
class GetPackageStatsResponse200:
    """
    Attributes:
        packages (Union[Unset, int]):
        releases (Union[Unset, int]):
    """

    packages: Union[Unset, int] = UNSET
    releases: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        packages = self.packages
        releases = self.releases

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if packages is not UNSET:
            field_dict["packages"] = packages
        if releases is not UNSET:
            field_dict["releases"] = releases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        packages = d.pop("packages", UNSET)

        releases = d.pop("releases", UNSET)

        get_package_stats_response_200 = cls(
            packages=packages,
            releases=releases,
        )

        get_package_stats_response_200.additional_properties = d
        return get_package_stats_response_200

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
