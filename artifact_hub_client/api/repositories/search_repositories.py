from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.repository import Repository
from ...models.repository_kind import RepositoryKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["limit"] = limit

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

    params["name"] = name

    params["url"] = url_query

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, List["Repository"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Repository.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, List["Repository"]]]:
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
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["Repository"]]]:
    """Search repositories that meet the provided criteria

     Search repositories that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        kind (Union[Unset, None, List[RepositoryKind]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        name (Union[Unset, None, str]):  Example: repo-name.
        url_query (Union[Unset, None, str]):  Example: https://repo2.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Repository']]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        kind=kind,
        user=user,
        org=org,
        name=name,
        url_query=url_query,
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
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["Repository"]]]:
    """Search repositories that meet the provided criteria

     Search repositories that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        kind (Union[Unset, None, List[RepositoryKind]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        name (Union[Unset, None, str]):  Example: repo-name.
        url_query (Union[Unset, None, str]):  Example: https://repo2.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Repository']]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        kind=kind,
        user=user,
        org=org,
        name=name,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["Repository"]]]:
    """Search repositories that meet the provided criteria

     Search repositories that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        kind (Union[Unset, None, List[RepositoryKind]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        name (Union[Unset, None, str]):  Example: repo-name.
        url_query (Union[Unset, None, str]):  Example: https://repo2.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Repository']]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        kind=kind,
        user=user,
        org=org,
        name=name,
        url_query=url_query,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
    kind: Union[Unset, None, List[RepositoryKind]] = UNSET,
    user: Union[Unset, None, List[str]] = UNSET,
    org: Union[Unset, None, List[str]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    url_query: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["Repository"]]]:
    """Search repositories that meet the provided criteria

     Search repositories that meet the provided criteria

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.
        kind (Union[Unset, None, List[RepositoryKind]]):
        user (Union[Unset, None, List[str]]):  Example: ['user1', 'user2'].
        org (Union[Unset, None, List[str]]):  Example: ['org1', 'org2'].
        name (Union[Unset, None, str]):  Example: repo-name.
        url_query (Union[Unset, None, str]):  Example: https://repo2.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Repository']]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            kind=kind,
            user=user,
            org=org,
            name=name,
            url_query=url_query,
        )
    ).parsed
