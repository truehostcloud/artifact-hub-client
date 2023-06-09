from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_kind_id import EventKindId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_summary import RepositorySummary


T = TypeVar("T", bound="GetUserSubscriptionsResponse200Item")


@attr.s(auto_attribs=True)
class GetUserSubscriptionsResponse200Item:
    """
    Attributes:
        package_id (str):
        name (str):  Example: pkg1.
        normalized_name (str):  Example: pkg1.
        repository (RepositorySummary):
        event_kinds (List[EventKindId]):
        logo_image_id (Union[Unset, str]):  Example: 12345abcde.
    """

    package_id: str
    name: str
    normalized_name: str
    repository: "RepositorySummary"
    event_kinds: List[EventKindId]
    logo_image_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_id = self.package_id
        name = self.name
        normalized_name = self.normalized_name
        repository = self.repository.to_dict()

        event_kinds = []
        for event_kinds_item_data in self.event_kinds:
            event_kinds_item = event_kinds_item_data.value

            event_kinds.append(event_kinds_item)

        logo_image_id = self.logo_image_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_id": package_id,
                "name": name,
                "normalized_name": normalized_name,
                "repository": repository,
                "event_kinds": event_kinds,
            }
        )
        if logo_image_id is not UNSET:
            field_dict["logo_image_id"] = logo_image_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository_summary import RepositorySummary

        d = src_dict.copy()
        package_id = d.pop("package_id")

        name = d.pop("name")

        normalized_name = d.pop("normalized_name")

        repository = RepositorySummary.from_dict(d.pop("repository"))

        event_kinds = []
        _event_kinds = d.pop("event_kinds")
        for event_kinds_item_data in _event_kinds:
            event_kinds_item = EventKindId(event_kinds_item_data)

            event_kinds.append(event_kinds_item)

        logo_image_id = d.pop("logo_image_id", UNSET)

        get_user_subscriptions_response_200_item = cls(
            package_id=package_id,
            name=name,
            normalized_name=normalized_name,
            repository=repository,
            event_kinds=event_kinds,
            logo_image_id=logo_image_id,
        )

        get_user_subscriptions_response_200_item.additional_properties = d
        return get_user_subscriptions_response_200_item

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
