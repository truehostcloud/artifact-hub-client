from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.facets_options_item import FacetsOptionsItem


T = TypeVar("T", bound="Facets")


@attr.s(auto_attribs=True)
class Facets:
    """
    Example:
        {'title': 'Publisher', 'filter_key': 'publisher', 'options': [{'id': 'f41e7480-8d5c-40d3-9ba6-65ac0da8fc9c',
            'name': 'Helm', 'total': 292, 'filter_key': 'org'}, {'id': 'b771c9a8-0076-444c-ad5e-927abe14173d', 'name':
            'Artifact Hub', 'total': 1, 'filter_key': 'org'}, {'id': 'a70u69a8-0326-324c-fd3e-0iu87e14173d', 'name':
            'user1', 'total': 3, 'filter_key': 'user'}]}

    Attributes:
        filter_key (str):
        title (str):
        options (List['FacetsOptionsItem']):
    """

    filter_key: str
    title: str
    options: List["FacetsOptionsItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_key = self.filter_key
        title = self.title
        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()

            options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_key": filter_key,
                "title": title,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.facets_options_item import FacetsOptionsItem

        d = src_dict.copy()
        filter_key = d.pop("filter_key")

        title = d.pop("title")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = FacetsOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        facets = cls(
            filter_key=filter_key,
            title=title,
            options=options,
        )

        facets.additional_properties = d
        return facets

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
