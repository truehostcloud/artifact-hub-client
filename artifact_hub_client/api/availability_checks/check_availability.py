from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.resource_kind_name import ResourceKindName
from ...types import UNSET, Response


def _get_kwargs(
    resource_kind: ResourceKindName,
    *,
    client: Client,
    v: str,
) -> Dict[str, Any]:
    url = "{}/check-availability/{resourceKind}".format(client.base_url, resourceKind=resource_kind)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["v"] = v

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "head",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_kind: ResourceKindName,
    *,
    client: Client,
    v: str,
) -> Response[Any]:
    """Check the availability of a given value for the provided resource kind

     Check the availability of a given value for the provided resource kind

    Args:
        resource_kind (ResourceKindName): Resource kind name:
              * `repositoryName` - Repository name
              * `repositoryURL` - Repository URL
              * `organizationName` - Organization name
              * `userAlias` - User alias
        v (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        resource_kind=resource_kind,
        client=client,
        v=v,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    resource_kind: ResourceKindName,
    *,
    client: Client,
    v: str,
) -> Response[Any]:
    """Check the availability of a given value for the provided resource kind

     Check the availability of a given value for the provided resource kind

    Args:
        resource_kind (ResourceKindName): Resource kind name:
              * `repositoryName` - Repository name
              * `repositoryURL` - Repository URL
              * `organizationName` - Organization name
              * `userAlias` - User alias
        v (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        resource_kind=resource_kind,
        client=client,
        v=v,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
