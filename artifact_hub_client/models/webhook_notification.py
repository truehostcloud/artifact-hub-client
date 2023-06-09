from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookNotification")


@attr.s(auto_attribs=True)
class WebhookNotification:
    """
    Attributes:
        notification_id (str):
        created_at (int):
        processed (bool):
        processed_at (int):
        error (Union[Unset, str]):  Example: error.
    """

    notification_id: str
    created_at: int
    processed: bool
    processed_at: int
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notification_id = self.notification_id
        created_at = self.created_at
        processed = self.processed
        processed_at = self.processed_at
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification_id": notification_id,
                "created_at": created_at,
                "processed": processed,
                "processed_at": processed_at,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notification_id = d.pop("notification_id")

        created_at = d.pop("created_at")

        processed = d.pop("processed")

        processed_at = d.pop("processed_at")

        error = d.pop("error", UNSET)

        webhook_notification = cls(
            notification_id=notification_id,
            created_at=created_at,
            processed=processed,
            processed_at=processed_at,
            error=error,
        )

        webhook_notification.additional_properties = d
        return webhook_notification

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
