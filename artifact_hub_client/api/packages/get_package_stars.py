from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_package_stars_response_200 import GetPackageStarsResponse200
from ...types import Response


def _get_kwargs(
    package_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/packages/{packageID}/stars".format(client.base_url, packageID=package_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, GetPackageStarsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPackageStarsResponse200.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, GetPackageStarsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    package_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetPackageStarsResponse200]]:
    """Get package stars

     Get package stars

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetPackageStarsResponse200]]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    package_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetPackageStarsResponse200]]:
    """Get package stars

     Get package stars

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetPackageStarsResponse200]
    """

    return sync_detailed(
        package_id=package_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    package_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetPackageStarsResponse200]]:
    """Get package stars

     Get package stars

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetPackageStarsResponse200]]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    package_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetPackageStarsResponse200]]:
    """Get package stars

     Get package stars

    Args:
        package_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetPackageStarsResponse200]
    """

    return (
        await asyncio_detailed(
            package_id=package_id,
            client=client,
        )
    ).parsed
