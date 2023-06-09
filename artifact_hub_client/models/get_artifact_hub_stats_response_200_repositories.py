from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetArtifactHubStatsResponse200Repositories")


@attr.s(auto_attribs=True)
class GetArtifactHubStatsResponse200Repositories:
    """
    Attributes:
        total (int):
        running_total (Union[Unset, List[List[int]]]):
        created_monthly (Union[Unset, List[List[int]]]):
    """

    total: int
    running_total: Union[Unset, List[List[int]]] = UNSET
    created_monthly: Union[Unset, List[List[int]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        running_total: Union[Unset, List[List[int]]] = UNSET
        if not isinstance(self.running_total, Unset):
            running_total = []
            for running_total_item_data in self.running_total:
                running_total_item = running_total_item_data

                running_total.append(running_total_item)

        created_monthly: Union[Unset, List[List[int]]] = UNSET
        if not isinstance(self.created_monthly, Unset):
            created_monthly = []
            for created_monthly_item_data in self.created_monthly:
                created_monthly_item = created_monthly_item_data

                created_monthly.append(created_monthly_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
            }
        )
        if running_total is not UNSET:
            field_dict["running_total"] = running_total
        if created_monthly is not UNSET:
            field_dict["created_monthly"] = created_monthly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total")

        running_total = []
        _running_total = d.pop("running_total", UNSET)
        for running_total_item_data in _running_total or []:
            running_total_item = cast(List[int], running_total_item_data)

            running_total.append(running_total_item)

        created_monthly = []
        _created_monthly = d.pop("created_monthly", UNSET)
        for created_monthly_item_data in _created_monthly or []:
            created_monthly_item = cast(List[int], created_monthly_item_data)

            created_monthly.append(created_monthly_item)

        get_artifact_hub_stats_response_200_repositories = cls(
            total=total,
            running_total=running_total,
            created_monthly=created_monthly,
        )

        get_artifact_hub_stats_response_200_repositories.additional_properties = d
        return get_artifact_hub_stats_response_200_repositories

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
