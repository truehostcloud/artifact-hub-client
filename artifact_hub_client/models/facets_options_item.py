from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FacetsOptionsItem")


@attr.s(auto_attribs=True)
class FacetsOptionsItem:
    """
    Attributes:
        id (str):
        name (str):
        total (int):
        filter_key (Union[Unset, str]):
    """

    id: str
    name: str
    total: int
    filter_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        total = self.total
        filter_key = self.filter_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "total": total,
            }
        )
        if filter_key is not UNSET:
            field_dict["filter_key"] = filter_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        total = d.pop("total")

        filter_key = d.pop("filter_key", UNSET)

        facets_options_item = cls(
            id=id,
            name=name,
            total=total,
            filter_key=filter_key,
        )

        facets_options_item.additional_properties = d
        return facets_options_item

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
