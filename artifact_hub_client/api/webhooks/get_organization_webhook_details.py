from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook import Webhook
from ...types import Response


def _get_kwargs(
    org_name: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/webhooks/org/{orgName}/{webhookID}".format(client.base_url, orgName=org_name, webhookID=webhook_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Webhook]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Webhook.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Webhook]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_name: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Webhook]]:
    """Get organization's webhook

     Get organization's webhook

    Args:
        org_name (str):  Example: org1.
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Webhook]]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        webhook_id=webhook_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_name: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Webhook]]:
    """Get organization's webhook

     Get organization's webhook

    Args:
        org_name (str):  Example: org1.
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Webhook]
    """

    return sync_detailed(
        org_name=org_name,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_name: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Webhook]]:
    """Get organization's webhook

     Get organization's webhook

    Args:
        org_name (str):  Example: org1.
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Webhook]]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        webhook_id=webhook_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_name: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Webhook]]:
    """Get organization's webhook

     Get organization's webhook

    Args:
        org_name (str):  Example: org1.
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Webhook]
    """

    return (
        await asyncio_detailed(
            org_name=org_name,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
