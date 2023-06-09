from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPackageStarsResponse200")


@attr.s(auto_attribs=True)
class GetPackageStarsResponse200:
    """
    Attributes:
        stars (Union[Unset, int]):
        starred_by_user (Union[Unset, bool]):
    """

    stars: Union[Unset, int] = UNSET
    starred_by_user: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stars = self.stars
        starred_by_user = self.starred_by_user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stars is not UNSET:
            field_dict["stars"] = stars
        if starred_by_user is not UNSET:
            field_dict["starred_by_user"] = starred_by_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stars = d.pop("stars", UNSET)

        starred_by_user = d.pop("starred_by_user", UNSET)

        get_package_stars_response_200 = cls(
            stars=stars,
            starred_by_user=starred_by_user,
        )

        get_package_stars_response_200.additional_properties = d
        return get_package_stars_response_200

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
