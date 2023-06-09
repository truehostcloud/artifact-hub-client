from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.get_helm_chart_templates_response_200_templates_item import (
        GetHelmChartTemplatesResponse200TemplatesItem,
    )
    from ..models.get_helm_chart_templates_response_200_values import GetHelmChartTemplatesResponse200Values


T = TypeVar("T", bound="GetHelmChartTemplatesResponse200")


@attr.s(auto_attribs=True)
class GetHelmChartTemplatesResponse200:
    """
    Attributes:
        templates (List['GetHelmChartTemplatesResponse200TemplatesItem']):
        values (GetHelmChartTemplatesResponse200Values):
    """

    templates: List["GetHelmChartTemplatesResponse200TemplatesItem"]
    values: "GetHelmChartTemplatesResponse200Values"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()

            templates.append(templates_item)

        values = self.values.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templates": templates,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_helm_chart_templates_response_200_templates_item import (
            GetHelmChartTemplatesResponse200TemplatesItem,
        )
        from ..models.get_helm_chart_templates_response_200_values import GetHelmChartTemplatesResponse200Values

        d = src_dict.copy()
        templates = []
        _templates = d.pop("templates")
        for templates_item_data in _templates:
            templates_item = GetHelmChartTemplatesResponse200TemplatesItem.from_dict(templates_item_data)

            templates.append(templates_item)

        values = GetHelmChartTemplatesResponse200Values.from_dict(d.pop("values"))

        get_helm_chart_templates_response_200 = cls(
            templates=templates,
            values=values,
        )

        get_helm_chart_templates_response_200.additional_properties = d
        return get_helm_chart_templates_response_200

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
