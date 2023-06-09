from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.package_base_signatures_item import PackageBaseSignaturesItem
from ..models.package_category_id import PackageCategoryId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_base_security_report_summary import PackageBaseSecurityReportSummary
    from ..models.repository_summary import RepositorySummary


T = TypeVar("T", bound="PackageSummary")


@attr.s(auto_attribs=True)
class PackageSummary:
    """
    Attributes:
        package_id (str):
        name (str):  Example: pkg1.
        normalized_name (str):  Example: pkg1.
        version (str):  Example: 1.0.0.
        ts (int):
        repository (RepositorySummary):
        logo_image_id (Union[Unset, str]):  Example: 12345abcde.
        display_name (Union[Unset, str]):  Example: Package 1.
        description (Union[Unset, str]):  Example: This is a package sample.
        app_version (Union[Unset, str]):  Example: 0.1.0.
        license_ (Union[Unset, str]):  Example: MIT.
        deprecated (Union[Unset, bool]):
        signed (Union[Unset, bool]):
        signatures (Union[Unset, List[PackageBaseSignaturesItem]]):
        official (Union[Unset, bool]):
        cncf (Union[Unset, None, bool]):
        security_report_summary (Union[Unset, PackageBaseSecurityReportSummary]):
        all_containers_images_whitelisted (Union[Unset, bool]):
        production_organizations_count (Union[Unset, float]):
        category (Union[Unset, PackageCategoryId]): Package category:
              * `1` - AI / Machine learning
              * `2` - Database
              * `3` - Integration and delivery
              * `4` - Monitoring and logging
              * `5` - Networking
              * `6` - Security
              * `7` - Storage
              * `8` - Streaming and messaging
        stars (Union[Unset, int]):  Example: 3.
    """

    package_id: str
    name: str
    normalized_name: str
    version: str
    ts: int
    repository: "RepositorySummary"
    logo_image_id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    app_version: Union[Unset, str] = UNSET
    license_: Union[Unset, str] = UNSET
    deprecated: Union[Unset, bool] = UNSET
    signed: Union[Unset, bool] = UNSET
    signatures: Union[Unset, List[PackageBaseSignaturesItem]] = UNSET
    official: Union[Unset, bool] = UNSET
    cncf: Union[Unset, None, bool] = UNSET
    security_report_summary: Union[Unset, "PackageBaseSecurityReportSummary"] = UNSET
    all_containers_images_whitelisted: Union[Unset, bool] = UNSET
    production_organizations_count: Union[Unset, float] = UNSET
    category: Union[Unset, PackageCategoryId] = UNSET
    stars: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_id = self.package_id
        name = self.name
        normalized_name = self.normalized_name
        version = self.version
        ts = self.ts
        repository = self.repository.to_dict()

        logo_image_id = self.logo_image_id
        display_name = self.display_name
        description = self.description
        app_version = self.app_version
        license_ = self.license_
        deprecated = self.deprecated
        signed = self.signed
        signatures: Union[Unset, List[str]] = UNSET
        if not isinstance(self.signatures, Unset):
            signatures = []
            for signatures_item_data in self.signatures:
                signatures_item = signatures_item_data.value

                signatures.append(signatures_item)

        official = self.official
        cncf = self.cncf
        security_report_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.security_report_summary, Unset):
            security_report_summary = self.security_report_summary.to_dict()

        all_containers_images_whitelisted = self.all_containers_images_whitelisted
        production_organizations_count = self.production_organizations_count
        category: Union[Unset, int] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        stars = self.stars

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_id": package_id,
                "name": name,
                "normalized_name": normalized_name,
                "version": version,
                "ts": ts,
                "repository": repository,
            }
        )
        if logo_image_id is not UNSET:
            field_dict["logo_image_id"] = logo_image_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if app_version is not UNSET:
            field_dict["app_version"] = app_version
        if license_ is not UNSET:
            field_dict["license"] = license_
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if signed is not UNSET:
            field_dict["signed"] = signed
        if signatures is not UNSET:
            field_dict["signatures"] = signatures
        if official is not UNSET:
            field_dict["official"] = official
        if cncf is not UNSET:
            field_dict["cncf"] = cncf
        if security_report_summary is not UNSET:
            field_dict["security_report_summary"] = security_report_summary
        if all_containers_images_whitelisted is not UNSET:
            field_dict["all_containers_images_whitelisted"] = all_containers_images_whitelisted
        if production_organizations_count is not UNSET:
            field_dict["production_organizations_count"] = production_organizations_count
        if category is not UNSET:
            field_dict["category"] = category
        if stars is not UNSET:
            field_dict["stars"] = stars

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_base_security_report_summary import PackageBaseSecurityReportSummary
        from ..models.repository_summary import RepositorySummary

        d = src_dict.copy()
        package_id = d.pop("package_id")

        name = d.pop("name")

        normalized_name = d.pop("normalized_name")

        version = d.pop("version")

        ts = d.pop("ts")

        repository = RepositorySummary.from_dict(d.pop("repository"))

        logo_image_id = d.pop("logo_image_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        app_version = d.pop("app_version", UNSET)

        license_ = d.pop("license", UNSET)

        deprecated = d.pop("deprecated", UNSET)

        signed = d.pop("signed", UNSET)

        signatures = []
        _signatures = d.pop("signatures", UNSET)
        for signatures_item_data in _signatures or []:
            signatures_item = PackageBaseSignaturesItem(signatures_item_data)

            signatures.append(signatures_item)

        official = d.pop("official", UNSET)

        cncf = d.pop("cncf", UNSET)

        _security_report_summary = d.pop("security_report_summary", UNSET)
        security_report_summary: Union[Unset, PackageBaseSecurityReportSummary]
        if isinstance(_security_report_summary, Unset):
            security_report_summary = UNSET
        else:
            security_report_summary = PackageBaseSecurityReportSummary.from_dict(_security_report_summary)

        all_containers_images_whitelisted = d.pop("all_containers_images_whitelisted", UNSET)

        production_organizations_count = d.pop("production_organizations_count", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PackageCategoryId]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PackageCategoryId(_category)

        stars = d.pop("stars", UNSET)

        package_summary = cls(
            package_id=package_id,
            name=name,
            normalized_name=normalized_name,
            version=version,
            ts=ts,
            repository=repository,
            logo_image_id=logo_image_id,
            display_name=display_name,
            description=description,
            app_version=app_version,
            license_=license_,
            deprecated=deprecated,
            signed=signed,
            signatures=signatures,
            official=official,
            cncf=cncf,
            security_report_summary=security_report_summary,
            all_containers_images_whitelisted=all_containers_images_whitelisted,
            production_organizations_count=production_organizations_count,
            category=category,
            stars=stars,
        )

        package_summary.additional_properties = d
        return package_summary

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
