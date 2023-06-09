from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WebhookSummaryWithPackagesPackagesItem")


@attr.s(auto_attribs=True)
class WebhookSummaryWithPackagesPackagesItem:
    """
    Attributes:
        package_id (str):
    """

    package_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_id = self.package_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_id": package_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package_id = d.pop("package_id")

        webhook_summary_with_packages_packages_item = cls(
            package_id=package_id,
        )

        webhook_summary_with_packages_packages_item.additional_properties = d
        return webhook_summary_with_packages_packages_item

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
