from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_kind_id import EventKindId
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSummary")


@attr.s(auto_attribs=True)
class WebhookSummary:
    """
    Attributes:
        name (str):  Example: webhook1.
        url (str):  Example: http://url.
        active (bool):
        description (Union[Unset, str]):  Example: description.
        secret (Union[Unset, str]):  Example: 123abc.
        content_type (Union[Unset, str]):  Example: application/json.
        template (Union[Unset, str]):  Example: {"text": "Package {{ .Package.Name }} version {{ .Package.Version }}
            released! {{ .Package.URL }}"}.
        event_kinds (Union[Unset, List[EventKindId]]):
    """

    name: str
    url: str
    active: bool
    description: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    event_kinds: Union[Unset, List[EventKindId]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        url = self.url
        active = self.active
        description = self.description
        secret = self.secret
        content_type = self.content_type
        template = self.template
        event_kinds: Union[Unset, List[int]] = UNSET
        if not isinstance(self.event_kinds, Unset):
            event_kinds = []
            for event_kinds_item_data in self.event_kinds:
                event_kinds_item = event_kinds_item_data.value

                event_kinds.append(event_kinds_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
                "active": active,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if secret is not UNSET:
            field_dict["secret"] = secret
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if template is not UNSET:
            field_dict["template"] = template
        if event_kinds is not UNSET:
            field_dict["event_kinds"] = event_kinds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        url = d.pop("url")

        active = d.pop("active")

        description = d.pop("description", UNSET)

        secret = d.pop("secret", UNSET)

        content_type = d.pop("content_type", UNSET)

        template = d.pop("template", UNSET)

        event_kinds = []
        _event_kinds = d.pop("event_kinds", UNSET)
        for event_kinds_item_data in _event_kinds or []:
            event_kinds_item = EventKindId(event_kinds_item_data)

            event_kinds.append(event_kinds_item)

        webhook_summary = cls(
            name=name,
            url=url,
            active=active,
            description=description,
            secret=secret,
            content_type=content_type,
            template=template,
            event_kinds=event_kinds,
        )

        webhook_summary.additional_properties = d
        return webhook_summary

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
