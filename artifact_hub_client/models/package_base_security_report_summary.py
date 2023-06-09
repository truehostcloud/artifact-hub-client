from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageBaseSecurityReportSummary")


@attr.s(auto_attribs=True)
class PackageBaseSecurityReportSummary:
    """
    Attributes:
        critical (Union[Unset, float]):
        high (Union[Unset, float]):
        medium (Union[Unset, float]):
        low (Union[Unset, float]):
        unknown (Union[Unset, float]):
    """

    critical: Union[Unset, float] = UNSET
    high: Union[Unset, float] = UNSET
    medium: Union[Unset, float] = UNSET
    low: Union[Unset, float] = UNSET
    unknown: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        critical = self.critical
        high = self.high
        medium = self.medium
        low = self.low
        unknown = self.unknown

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if high is not UNSET:
            field_dict["high"] = high
        if medium is not UNSET:
            field_dict["medium"] = medium
        if low is not UNSET:
            field_dict["low"] = low
        if unknown is not UNSET:
            field_dict["unknown"] = unknown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        critical = d.pop("critical", UNSET)

        high = d.pop("high", UNSET)

        medium = d.pop("medium", UNSET)

        low = d.pop("low", UNSET)

        unknown = d.pop("unknown", UNSET)

        package_base_security_report_summary = cls(
            critical=critical,
            high=high,
            medium=medium,
            low=low,
            unknown=unknown,
        )

        package_base_security_report_summary.additional_properties = d
        return package_base_security_report_summary

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
