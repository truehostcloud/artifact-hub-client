from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.repository_kind import RepositoryKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositorySummary")


@attr.s(auto_attribs=True)
class RepositorySummary:
    """
    Attributes:
        repository_id (str):
        kind (RepositoryKind): Repository kind:
              * `0` - Helm charts
              * `1` - Falco rules
              * `2` - OPA policies
              * `3` - OLM operators
              * `4` - Tinkerbell actions
              * `5` - Krew kubectl plugins
              * `6` - Helm plugins
              * `7` - Tekton tasks
              * `8` - KEDA scalers
              * `9` - Core DNS plugins
              * `10` - Keptn integrations
              * `11` - Tekton pipelines
              * `12` - Container images
              * `13` - Kubewarden policies
              * `14` - Gatekeeper policies
              * `15` - Kyverno policies
              * `16` - Knative client plugins
              * `17` - Backstage plugins
              * `18` - Argo templates
              * `19` - KubeArmor templates
        name (str):  Example: repo1.
        url (str):  Example: http://repourl.
        verified_publisher (bool):
        official (bool):
        scanner_disabled (bool):
        display_name (Union[Unset, str]):  Example: Repository 1.
        cncf (Union[Unset, None, bool]):
        private (Union[Unset, bool]):
        user_alias (Union[Unset, str]):  Example: jdoe.
        organization_name (Union[Unset, str]):  Example: org1.
        organization_display_name (Union[Unset, str]):  Example: Organization 1.
    """

    repository_id: str
    kind: RepositoryKind
    name: str
    url: str
    verified_publisher: bool
    official: bool
    scanner_disabled: bool
    display_name: Union[Unset, str] = UNSET
    cncf: Union[Unset, None, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    user_alias: Union[Unset, str] = UNSET
    organization_name: Union[Unset, str] = UNSET
    organization_display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository_id = self.repository_id
        kind = self.kind.value

        name = self.name
        url = self.url
        verified_publisher = self.verified_publisher
        official = self.official
        scanner_disabled = self.scanner_disabled
        display_name = self.display_name
        cncf = self.cncf
        private = self.private
        user_alias = self.user_alias
        organization_name = self.organization_name
        organization_display_name = self.organization_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository_id": repository_id,
                "kind": kind,
                "name": name,
                "url": url,
                "verified_publisher": verified_publisher,
                "official": official,
                "scanner_disabled": scanner_disabled,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if cncf is not UNSET:
            field_dict["cncf"] = cncf
        if private is not UNSET:
            field_dict["private"] = private
        if user_alias is not UNSET:
            field_dict["user_alias"] = user_alias
        if organization_name is not UNSET:
            field_dict["organization_name"] = organization_name
        if organization_display_name is not UNSET:
            field_dict["organization_display_name"] = organization_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        repository_id = d.pop("repository_id")

        kind = RepositoryKind(d.pop("kind"))

        name = d.pop("name")

        url = d.pop("url")

        verified_publisher = d.pop("verified_publisher")

        official = d.pop("official")

        scanner_disabled = d.pop("scanner_disabled")

        display_name = d.pop("display_name", UNSET)

        cncf = d.pop("cncf", UNSET)

        private = d.pop("private", UNSET)

        user_alias = d.pop("user_alias", UNSET)

        organization_name = d.pop("organization_name", UNSET)

        organization_display_name = d.pop("organization_display_name", UNSET)

        repository_summary = cls(
            repository_id=repository_id,
            kind=kind,
            name=name,
            url=url,
            verified_publisher=verified_publisher,
            official=official,
            scanner_disabled=scanner_disabled,
            display_name=display_name,
            cncf=cncf,
            private=private,
            user_alias=user_alias,
            organization_name=organization_name,
            organization_display_name=organization_display_name,
        )

        repository_summary.additional_properties = d
        return repository_summary

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
