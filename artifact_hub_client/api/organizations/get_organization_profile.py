from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.organization_summary import OrganizationSummary
from ...types import Response


def _get_kwargs(
    org_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{orgName}".format(client.base_url, orgName=org_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, OrganizationSummary]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrganizationSummary.from_dict(response.json())

        return response_200
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, OrganizationSummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_name: str,
    *,
    client: Client,
) -> Response[Union[Any, OrganizationSummary]]:
    """Get organization profile

     Get organization profile

    Args:
        org_name (str):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrganizationSummary]]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, OrganizationSummary]]:
    """Get organization profile

     Get organization profile

    Args:
        org_name (str):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OrganizationSummary]
    """

    return sync_detailed(
        org_name=org_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_name: str,
    *,
    client: Client,
) -> Response[Union[Any, OrganizationSummary]]:
    """Get organization profile

     Get organization profile

    Args:
        org_name (str):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrganizationSummary]]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, OrganizationSummary]]:
    """Get organization profile

     Get organization profile

    Args:
        org_name (str):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OrganizationSummary]
    """

    return (
        await asyncio_detailed(
            org_name=org_name,
            client=client,
        )
    ).parsed
