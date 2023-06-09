from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.repository_kind import RepositoryKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_data import RepositoryData


T = TypeVar("T", bound="Repository")


@attr.s(auto_attribs=True)
class Repository:
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
        digest (str):
        last_tracking_ts (int):
        last_scanning_ts (int):
        disabled (bool):
        display_name (Union[Unset, str]):  Example: Repository 1.
        cncf (Union[Unset, None, bool]):
        private (Union[Unset, bool]):
        user_alias (Union[Unset, str]):  Example: jdoe.
        organization_name (Union[Unset, str]):  Example: org1.
        organization_display_name (Union[Unset, str]):  Example: Organization 1.
        last_tracking_errors (Union[Unset, str]):  Example: Error.
        last_scanning_errors (Union[Unset, str]):  Example: Error.
        branch (Union[Unset, str]):
        data (Union[Unset, RepositoryData]):
    """

    repository_id: str
    kind: RepositoryKind
    name: str
    url: str
    verified_publisher: bool
    official: bool
    scanner_disabled: bool
    digest: str
    last_tracking_ts: int
    last_scanning_ts: int
    disabled: bool
    display_name: Union[Unset, str] = UNSET
    cncf: Union[Unset, None, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    user_alias: Union[Unset, str] = UNSET
    organization_name: Union[Unset, str] = UNSET
    organization_display_name: Union[Unset, str] = UNSET
    last_tracking_errors: Union[Unset, str] = UNSET
    last_scanning_errors: Union[Unset, str] = UNSET
    branch: Union[Unset, str] = UNSET
    data: Union[Unset, "RepositoryData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository_id = self.repository_id
        kind = self.kind.value

        name = self.name
        url = self.url
        verified_publisher = self.verified_publisher
        official = self.official
        scanner_disabled = self.scanner_disabled
        digest = self.digest
        last_tracking_ts = self.last_tracking_ts
        last_scanning_ts = self.last_scanning_ts
        disabled = self.disabled
        display_name = self.display_name
        cncf = self.cncf
        private = self.private
        user_alias = self.user_alias
        organization_name = self.organization_name
        organization_display_name = self.organization_display_name
        last_tracking_errors = self.last_tracking_errors
        last_scanning_errors = self.last_scanning_errors
        branch = self.branch
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
                "digest": digest,
                "last_tracking_ts": last_tracking_ts,
                "last_scanning_ts": last_scanning_ts,
                "disabled": disabled,
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
        if last_tracking_errors is not UNSET:
            field_dict["last_tracking_errors"] = last_tracking_errors
        if last_scanning_errors is not UNSET:
            field_dict["last_scanning_errors"] = last_scanning_errors
        if branch is not UNSET:
            field_dict["branch"] = branch
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.repository_data import RepositoryData

        d = src_dict.copy()
        repository_id = d.pop("repository_id")

        kind = RepositoryKind(d.pop("kind"))

        name = d.pop("name")

        url = d.pop("url")

        verified_publisher = d.pop("verified_publisher")

        official = d.pop("official")

        scanner_disabled = d.pop("scanner_disabled")

        digest = d.pop("digest")

        last_tracking_ts = d.pop("last_tracking_ts")

        last_scanning_ts = d.pop("last_scanning_ts")

        disabled = d.pop("disabled")

        display_name = d.pop("display_name", UNSET)

        cncf = d.pop("cncf", UNSET)

        private = d.pop("private", UNSET)

        user_alias = d.pop("user_alias", UNSET)

        organization_name = d.pop("organization_name", UNSET)

        organization_display_name = d.pop("organization_display_name", UNSET)

        last_tracking_errors = d.pop("last_tracking_errors", UNSET)

        last_scanning_errors = d.pop("last_scanning_errors", UNSET)

        branch = d.pop("branch", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, RepositoryData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RepositoryData.from_dict(_data)

        repository = cls(
            repository_id=repository_id,
            kind=kind,
            name=name,
            url=url,
            verified_publisher=verified_publisher,
            official=official,
            scanner_disabled=scanner_disabled,
            digest=digest,
            last_tracking_ts=last_tracking_ts,
            last_scanning_ts=last_scanning_ts,
            disabled=disabled,
            display_name=display_name,
            cncf=cncf,
            private=private,
            user_alias=user_alias,
            organization_name=organization_name,
            organization_display_name=organization_display_name,
            last_tracking_errors=last_tracking_errors,
            last_scanning_errors=last_scanning_errors,
            branch=branch,
            data=data,
        )

        repository.additional_properties = d
        return repository

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
