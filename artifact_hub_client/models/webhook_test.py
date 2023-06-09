from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_kind_id import EventKindId
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookTest")


@attr.s(auto_attribs=True)
class WebhookTest:
    """
    Attributes:
        url (str):  Example: http://url.
        event_kinds (List[EventKindId]):  Example: [0].
        content_type (Union[Unset, str]):  Example: application/json.
        template (Union[Unset, str]):  Example: {"text": "Package {{ .Package.Name }} version {{ .Package.Version }}
            released! {{ .Package.URL }}"}.
    """

    url: str
    event_kinds: List[EventKindId]
    content_type: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        event_kinds = []
        for event_kinds_item_data in self.event_kinds:
            event_kinds_item = event_kinds_item_data.value

            event_kinds.append(event_kinds_item)

        content_type = self.content_type
        template = self.template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "event_kinds": event_kinds,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        event_kinds = []
        _event_kinds = d.pop("event_kinds")
        for event_kinds_item_data in _event_kinds:
            event_kinds_item = EventKindId(event_kinds_item_data)

            event_kinds.append(event_kinds_item)

        content_type = d.pop("content_type", UNSET)

        template = d.pop("template", UNSET)

        webhook_test = cls(
            url=url,
            event_kinds=event_kinds,
            content_type=content_type,
            template=template,
        )

        webhook_test.additional_properties = d
        return webhook_test

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
