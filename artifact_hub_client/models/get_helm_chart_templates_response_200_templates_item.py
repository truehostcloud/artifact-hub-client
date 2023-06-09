from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetHelmChartTemplatesResponse200TemplatesItem")


@attr.s(auto_attribs=True)
class GetHelmChartTemplatesResponse200TemplatesItem:
    """
    Attributes:
        name (str):
        data (str):
    """

    name: str
    data: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        data = d.pop("data")

        get_helm_chart_templates_response_200_templates_item = cls(
            name=name,
            data=data,
        )

        get_helm_chart_templates_response_200_templates_item.additional_properties = d
        return get_helm_chart_templates_response_200_templates_item

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
