from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.event_kind_id import EventKindId

T = TypeVar("T", bound="GetPackageUserSubscriptionsResponse200Item")


@attr.s(auto_attribs=True)
class GetPackageUserSubscriptionsResponse200Item:
    """
    Attributes:
        event_kind (EventKindId): Event kind:
              * `0` - New package release
              * `1` - Security alerts
              * `2` - Repository tracking errors
              * `4` - Repository scanning errors
    """

    event_kind: EventKindId
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_kind = self.event_kind.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_kind": event_kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_kind = EventKindId(d.pop("event_kind"))

        get_package_user_subscriptions_response_200_item = cls(
            event_kind=event_kind,
        )

        get_package_user_subscriptions_response_200_item.additional_properties = d
        return get_package_user_subscriptions_response_200_item

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
