from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.get_artifact_hub_stats_response_200_organizations import GetArtifactHubStatsResponse200Organizations
    from ..models.get_artifact_hub_stats_response_200_packages import GetArtifactHubStatsResponse200Packages
    from ..models.get_artifact_hub_stats_response_200_repositories import GetArtifactHubStatsResponse200Repositories
    from ..models.get_artifact_hub_stats_response_200_snapshots import GetArtifactHubStatsResponse200Snapshots
    from ..models.get_artifact_hub_stats_response_200_users import GetArtifactHubStatsResponse200Users


T = TypeVar("T", bound="GetArtifactHubStatsResponse200")


@attr.s(auto_attribs=True)
class GetArtifactHubStatsResponse200:
    """
    Example:
        {'generated_at': 1615980004171, 'packages': {'total': 969, 'running_total': [[1585612800000, 917],
            [1585872000000, 918], [1586736000000, 937], [1586908800000, 938], [1586995200000, 949], [1587340800000, 953],
            [1587427200000, 955], [1587513600000, 969]], 'created_monthly': [[1583020800000, 917], [1585699200000, 52]],
            'views_daily': [[1639731010000, 800], [1639644610000, 820]]}, 'snapshots': {'total': 3998, 'running_total':
            [[1585612800000, 3906], [1585699200000, 3922], [1585785600000, 3935], [1585872000000, 3948], [1586044800000,
            3951], [1586131200000, 3959], [1586217600000, 3981], [1586304000000, 3998]], 'created_monthly': [[1583020800000,
            3906], [1585699200000, 92]]}, 'repositories': {'total': 181, 'running_total': [[1585612800000, 172],
            [1585872000000, 173], [1586736000000, 176], [1586908800000, 177], [1586995200000, 181]]}, 'organizations':
            {'total': 8, 'running_total': [[1585612800000, 3], [1585785600000, 6], [1585872000000, 7], [1586217600000, 8]]},
            'users': {'total': 9, 'running_total': [[1584403200000, 3], [1584489600000, 5], [1584576000000, 6],
            [1584662400000, 8], [1584921600000, 9]]}}

    Attributes:
        generated_at (int):
        packages (GetArtifactHubStatsResponse200Packages):
        repositories (GetArtifactHubStatsResponse200Repositories):
        snapshots (GetArtifactHubStatsResponse200Snapshots):
        organizations (GetArtifactHubStatsResponse200Organizations):
        users (GetArtifactHubStatsResponse200Users):
    """

    generated_at: int
    packages: "GetArtifactHubStatsResponse200Packages"
    repositories: "GetArtifactHubStatsResponse200Repositories"
    snapshots: "GetArtifactHubStatsResponse200Snapshots"
    organizations: "GetArtifactHubStatsResponse200Organizations"
    users: "GetArtifactHubStatsResponse200Users"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generated_at = self.generated_at
        packages = self.packages.to_dict()

        repositories = self.repositories.to_dict()

        snapshots = self.snapshots.to_dict()

        organizations = self.organizations.to_dict()

        users = self.users.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generated_at": generated_at,
                "packages": packages,
                "repositories": repositories,
                "snapshots": snapshots,
                "organizations": organizations,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_artifact_hub_stats_response_200_organizations import (
            GetArtifactHubStatsResponse200Organizations,
        )
        from ..models.get_artifact_hub_stats_response_200_packages import GetArtifactHubStatsResponse200Packages
        from ..models.get_artifact_hub_stats_response_200_repositories import GetArtifactHubStatsResponse200Repositories
        from ..models.get_artifact_hub_stats_response_200_snapshots import GetArtifactHubStatsResponse200Snapshots
        from ..models.get_artifact_hub_stats_response_200_users import GetArtifactHubStatsResponse200Users

        d = src_dict.copy()
        generated_at = d.pop("generated_at")

        packages = GetArtifactHubStatsResponse200Packages.from_dict(d.pop("packages"))

        repositories = GetArtifactHubStatsResponse200Repositories.from_dict(d.pop("repositories"))

        snapshots = GetArtifactHubStatsResponse200Snapshots.from_dict(d.pop("snapshots"))

        organizations = GetArtifactHubStatsResponse200Organizations.from_dict(d.pop("organizations"))

        users = GetArtifactHubStatsResponse200Users.from_dict(d.pop("users"))

        get_artifact_hub_stats_response_200 = cls(
            generated_at=generated_at,
            packages=packages,
            repositories=repositories,
            snapshots=snapshots,
            organizations=organizations,
            users=users,
        )

        get_artifact_hub_stats_response_200.additional_properties = d
        return get_artifact_hub_stats_response_200

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
