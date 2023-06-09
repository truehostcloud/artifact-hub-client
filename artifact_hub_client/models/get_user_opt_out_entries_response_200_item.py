from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.event_kind_id import EventKindId

if TYPE_CHECKING:
    from ..models.repository_summary import RepositorySummary


T = TypeVar("T", bound="GetUserOptOutEntriesResponse200Item")


@attr.s(auto_attribs=True)
class GetUserOptOutEntriesResponse200Item:
    """
    Attributes:
        opt_out_id (str):
        repository (RepositorySummary):
        event_kind (EventKindId): Event kind:
              * `0` - New package release
              * `1` - Security alerts
              * `2` - Repository tracking errors
              * `4` - Repository scanning errors
    """

    opt_out_id: str
    repository: "RepositorySummary"
    event_kind: EventKindId
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opt_out_id = self.opt_out_id
        repository = self.repository.to_dict()

        event_kind = self.event_kind.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "opt_out_id": opt_out_id,
                "repository": repository,
                "event_kind": event_kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository_summary import RepositorySummary

        d = src_dict.copy()
        opt_out_id = d.pop("opt_out_id")

        repository = RepositorySummary.from_dict(d.pop("repository"))

        event_kind = EventKindId(d.pop("event_kind"))

        get_user_opt_out_entries_response_200_item = cls(
            opt_out_id=opt_out_id,
            repository=repository,
            event_kind=event_kind,
        )

        get_user_opt_out_entries_response_200_item.additional_properties = d
        return get_user_opt_out_entries_response_200_item

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
