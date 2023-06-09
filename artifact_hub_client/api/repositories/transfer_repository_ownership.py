from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_name: str,
    repo_name: str,
    *,
    client: AuthenticatedClient,
    org: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/org/{orgName}/{repoName}/transfer".format(
        client.base_url, orgName=org_name, repoName=repo_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["org"] = org

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
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
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
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
    org_name: str,
    repo_name: str,
    *,
    client: AuthenticatedClient,
    org: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Transfer organization's repository to a different owner

     Transfer organization's repository to a different owner

    Args:
        org_name (str):  Example: org1.
        repo_name (str):  Example: repoName.
        org (Union[Unset, None, str]):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        repo_name=repo_name,
        client=client,
        org=org,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    org_name: str,
    repo_name: str,
    *,
    client: AuthenticatedClient,
    org: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Transfer organization's repository to a different owner

     Transfer organization's repository to a different owner

    Args:
        org_name (str):  Example: org1.
        repo_name (str):  Example: repoName.
        org (Union[Unset, None, str]):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        repo_name=repo_name,
        client=client,
        org=org,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
