from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.facets import Facets
    from ..models.package_summary import PackageSummary


T = TypeVar("T", bound="SearchPackagesResponse200")


@attr.s(auto_attribs=True)
class SearchPackagesResponse200:
    """
    Attributes:
        packages (Union[Unset, List['PackageSummary']]):
        facets (Union[Unset, List['Facets']]):
    """

    packages: Union[Unset, List["PackageSummary"]] = UNSET
    facets: Union[Unset, List["Facets"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        packages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()

                packages.append(packages_item)

        facets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.facets, Unset):
            facets = []
            for facets_item_data in self.facets:
                facets_item = facets_item_data.to_dict()

                facets.append(facets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if packages is not UNSET:
            field_dict["packages"] = packages
        if facets is not UNSET:
            field_dict["facets"] = facets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.facets import Facets
        from ..models.package_summary import PackageSummary

        d = src_dict.copy()
        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = PackageSummary.from_dict(packages_item_data)

            packages.append(packages_item)

        facets = []
        _facets = d.pop("facets", UNSET)
        for facets_item_data in _facets or []:
            facets_item = Facets.from_dict(facets_item_data)

            facets.append(facets_item)

        search_packages_response_200 = cls(
            packages=packages,
            facets=facets,
        )

        search_packages_response_200.additional_properties = d
        return search_packages_response_200

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
