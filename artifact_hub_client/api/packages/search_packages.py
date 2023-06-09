from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.repository_kind import RepositoryKind
from ...models.search_packages_category_item import SearchPackagesCategoryItem
from ...models.search_packages_response_200 import SearchPackagesResponse200
from ...models.search_packages_sort import SearchPackagesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    facets: bool = False,
    ts_query_web: Union[Unset, None, str] = UNSET,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    category: Union[Unset, None, List[SearchPackagesCategoryItem]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    repo: Union[Unset, None, List[str]] = UNSET,
    license_: Union[Unset, None, List[str]] = UNSET,
    capabilities: Union[Unset, None, List[str]] = UNSET,
    deprecated: Union[Unset, None, bool] = False,
    operators: Union[Unset, None, bool] = UNSET,
    verified_publisher: Union[Unset, None, bool] = UNSET,
    official: Union[Unset, None, bool] = UNSET,
    cncf: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, SearchPackagesSort] = UNSET,
) -> Dict[str, Any]:
    url = "{}/packages/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["limit"] = limit

    params["facets"] = facets

    params["ts_query_web"] = ts_query_web

    json_kind: Union[Unset, None, List[int]] = UNSET
    if not isinstance(kind, Unset):
        if kind is None:
            json_kind = None
        else:
            json_kind = []
            for kind_item_data in kind:
                kind_item = kind_item_data.value

                json_kind.append(kind_item)

    params["kind"] = json_kind

    json_category: Union[Unset, None, List[int]] = UNSET
    if not isinstance(category, Unset):
        if category is None:
            json_category = None
        else:
            json_category = []
            for category_item_data in category:
                category_item = category_item_data.value

                json_category.append(category_item)

    params["category"] = json_category

    json_user: Union[Unset, None, List[str]] = UNSET
    if not isinstance(user, Unset):
        if user is None:
            json_user = None
        else:
            json_user = user

    params["user"] = json_user

    json_org: Union[Unset, None, List[str]] = UNSET
    if not isinstance(org, Unset):
        if org is None:
            json_org = None
        else:
            json_org = org

    params["org"] = json_org

    json_repo: Union[Unset, None, List[str]] = UNSET
    if not isinstance(repo, Unset):
        if repo is None:
            json_repo = None
        else:
            json_repo = repo

    params["repo"] = json_repo

    json_license_: Union[Unset, None, List[str]] = UNSET
    if not isinstance(license_, Unset):
        if license_ is None:
            json_license_ = None
        else:
            json_license_ = license_

    params["license"] = json_license_

    json_capabilities: Union[Unset, None, List[str]] = UNSET
    if not isinstance(capabilities, Unset):
        if capabilities is None:
            json_capabilities = None
        else:
            json_capabilities = capabilities

    params["capabilities"] = json_capabilities

    params["deprecated"] = deprecated

    params["operators"] = operators

    params["verified_publisher"] = verified_publisher

    params["official"] = official

    params["cncf"] = cncf

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, SearchPackagesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchPackagesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, SearchPackagesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    facets: bool = False,
    ts_query_web: Union[Unset, None, str] = UNSET,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    category: Union[Unset, None, List[SearchPackagesCategoryItem]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    repo: Union[Unset, None, List[str]] = UNSET,
    license_: Union[Unset, None, List[str]] = UNSET,
    capabilities: Union[Unset, None, List[str]] = UNSET,
    deprecated: Union[Unset, None, bool] = False,
    operators: Union[Unset, None, bool] = UNSET,
    verified_publisher: Union[Unset, None, bool] = UNSET,
    official: Union[Unset, None, bool] = UNSET,
    cncf: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, SearchPackagesSort] = UNSET,
) -> Response[Union[Any, SearchPackagesResponse200]]:
    """Search packages that meet the provided criteria

     Search packages that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        facets (bool):
        ts_query_web (Union[Unset, None, str]):  Example: database.
        kind (Union[Unset, None, List[RepositoryKind]]):
        category (Union[Unset, None, List[SearchPackagesCategoryItem]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        repo (Union[Unset, None, List[str]]):  Example: ['repo1', 'repo2'].
        license_ (Union[Unset, None, List[str]]):  Example: ['MIT', 'Apache-2.0'].
        capabilities (Union[Unset, None, List[str]]):  Example: ['basic install', 'seamless
            upgrades', 'full lifecycle', 'deep insights', 'auto pilot'].
        deprecated (Union[Unset, None, bool]):
        operators (Union[Unset, None, bool]):
        verified_publisher (Union[Unset, None, bool]):
        official (Union[Unset, None, bool]):
        cncf (Union[Unset, None, bool]):
        sort (Union[Unset, None, SearchPackagesSort]):  Example: relevance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchPackagesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        facets=facets,
        ts_query_web=ts_query_web,
        kind=kind,
        category=category,
        user=user,
        org=org,
        repo=repo,
        license_=license_,
        capabilities=capabilities,
        deprecated=deprecated,
        operators=operators,
        verified_publisher=verified_publisher,
        official=official,
        cncf=cncf,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    facets: bool = False,
    ts_query_web: Union[Unset, None, str] = UNSET,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    category: Union[Unset, None, List[SearchPackagesCategoryItem]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    repo: Union[Unset, None, List[str]] = UNSET,
    license_: Union[Unset, None, List[str]] = UNSET,
    capabilities: Union[Unset, None, List[str]] = UNSET,
    deprecated: Union[Unset, None, bool] = False,
    operators: Union[Unset, None, bool] = UNSET,
    verified_publisher: Union[Unset, None, bool] = UNSET,
    official: Union[Unset, None, bool] = UNSET,
    cncf: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, SearchPackagesSort] = UNSET,
) -> Optional[Union[Any, SearchPackagesResponse200]]:
    """Search packages that meet the provided criteria

     Search packages that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        facets (bool):
        ts_query_web (Union[Unset, None, str]):  Example: database.
        kind (Union[Unset, None, List[RepositoryKind]]):
        category (Union[Unset, None, List[SearchPackagesCategoryItem]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        repo (Union[Unset, None, List[str]]):  Example: ['repo1', 'repo2'].
        license_ (Union[Unset, None, List[str]]):  Example: ['MIT', 'Apache-2.0'].
        capabilities (Union[Unset, None, List[str]]):  Example: ['basic install', 'seamless
            upgrades', 'full lifecycle', 'deep insights', 'auto pilot'].
        deprecated (Union[Unset, None, bool]):
        operators (Union[Unset, None, bool]):
        verified_publisher (Union[Unset, None, bool]):
        official (Union[Unset, None, bool]):
        cncf (Union[Unset, None, bool]):
        sort (Union[Unset, None, SearchPackagesSort]):  Example: relevance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchPackagesResponse200]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        facets=facets,
        ts_query_web=ts_query_web,
        kind=kind,
        category=category,
        user=user,
        org=org,
        repo=repo,
        license_=license_,
        capabilities=capabilities,
        deprecated=deprecated,
        operators=operators,
        verified_publisher=verified_publisher,
        official=official,
        cncf=cncf,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    facets: bool = False,
    ts_query_web: Union[Unset, None, str] = UNSET,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    category: Union[Unset, None, List[SearchPackagesCategoryItem]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    repo: Union[Unset, None, List[str]] = UNSET,
    license_: Union[Unset, None, List[str]] = UNSET,
    capabilities: Union[Unset, None, List[str]] = UNSET,
    deprecated: Union[Unset, None, bool] = False,
    operators: Union[Unset, None, bool] = UNSET,
    verified_publisher: Union[Unset, None, bool] = UNSET,
    official: Union[Unset, None, bool] = UNSET,
    cncf: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, SearchPackagesSort] = UNSET,
) -> Response[Union[Any, SearchPackagesResponse200]]:
    """Search packages that meet the provided criteria

     Search packages that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        facets (bool):
        ts_query_web (Union[Unset, None, str]):  Example: database.
        kind (Union[Unset, None, List[RepositoryKind]]):
        category (Union[Unset, None, List[SearchPackagesCategoryItem]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        repo (Union[Unset, None, List[str]]):  Example: ['repo1', 'repo2'].
        license_ (Union[Unset, None, List[str]]):  Example: ['MIT', 'Apache-2.0'].
        capabilities (Union[Unset, None, List[str]]):  Example: ['basic install', 'seamless
            upgrades', 'full lifecycle', 'deep insights', 'auto pilot'].
        deprecated (Union[Unset, None, bool]):
        operators (Union[Unset, None, bool]):
        verified_publisher (Union[Unset, None, bool]):
        official (Union[Unset, None, bool]):
        cncf (Union[Unset, None, bool]):
        sort (Union[Unset, None, SearchPackagesSort]):  Example: relevance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchPackagesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        facets=facets,
        ts_query_web=ts_query_web,
        kind=kind,
        category=category,
        user=user,
        org=org,
        repo=repo,
        license_=license_,
        capabilities=capabilities,
        deprecated=deprecated,
        operators=operators,
        verified_publisher=verified_publisher,
        official=official,
        cncf=cncf,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    facets: bool = False,
    ts_query_web: Union[Unset, None, str] = UNSET,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    category: Union[Unset, None, List[SearchPackagesCategoryItem]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    repo: Union[Unset, None, List[str]] = UNSET,
    license_: Union[Unset, None, List[str]] = UNSET,
    capabilities: Union[Unset, None, List[str]] = UNSET,
    deprecated: Union[Unset, None, bool] = False,
    operators: Union[Unset, None, bool] = UNSET,
    verified_publisher: Union[Unset, None, bool] = UNSET,
    official: Union[Unset, None, bool] = UNSET,
    cncf: Union[Unset, None, bool] = UNSET,
    sort: Union[Unset, None, SearchPackagesSort] = UNSET,
) -> Optional[Union[Any, SearchPackagesResponse200]]:
    """Search packages that meet the provided criteria

     Search packages that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        facets (bool):
        ts_query_web (Union[Unset, None, str]):  Example: database.
        kind (Union[Unset, None, List[RepositoryKind]]):
        category (Union[Unset, None, List[SearchPackagesCategoryItem]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        repo (Union[Unset, None, List[str]]):  Example: ['repo1', 'repo2'].
        license_ (Union[Unset, None, List[str]]):  Example: ['MIT', 'Apache-2.0'].
        capabilities (Union[Unset, None, List[str]]):  Example: ['basic install', 'seamless
            upgrades', 'full lifecycle', 'deep insights', 'auto pilot'].
        deprecated (Union[Unset, None, bool]):
        operators (Union[Unset, None, bool]):
        verified_publisher (Union[Unset, None, bool]):
        official (Union[Unset, None, bool]):
        cncf (Union[Unset, None, bool]):
        sort (Union[Unset, None, SearchPackagesSort]):  Example: relevance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchPackagesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            facets=facets,
            ts_query_web=ts_query_web,
            kind=kind,
            category=category,
            user=user,
            org=org,
            repo=repo,
            license_=license_,
            capabilities=capabilities,
            deprecated=deprecated,
            operators=operators,
            verified_publisher=verified_publisher,
            official=official,
            cncf=cncf,
            sort=sort,
        )
    ).parsed
