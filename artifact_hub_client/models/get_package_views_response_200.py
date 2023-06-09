from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetPackageViewsResponse200")


@attr.s(auto_attribs=True)
class GetPackageViewsResponse200:
    """
    Example:
        {'1.0.1': {'2021-12-09': 12, '2021-12-08': 30}, '1.0.0': {'2021-12-09': 2, '2021-12-08': 5}}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_package_views_response_200 = cls()

        get_package_views_response_200.additional_properties = d
        return get_package_views_response_200

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
