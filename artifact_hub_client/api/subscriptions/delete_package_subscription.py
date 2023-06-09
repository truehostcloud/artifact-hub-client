from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_kind_id import EventKindId
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    package_id: str,
    event_kind: EventKindId,
) -> Dict[str, Any]:
    url = "{}/subscriptions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["packageID"] = package_id

    json_event_kind = event_kind.value

    params["event_kind"] = json_event_kind

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
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
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    *,
    client: AuthenticatedClient,
    package_id: str,
    event_kind: EventKindId,
) -> Response[Any]:
    """Delete subscription

     Delete subscription

    Args:
        package_id (str):
        event_kind (EventKindId): Event kind:
              * `0` - New package release
              * `1` - Security alerts
              * `2` - Repository tracking errors
              * `4` - Repository scanning errors

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        package_id=package_id,
        event_kind=event_kind,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    package_id: str,
    event_kind: EventKindId,
) -> Response[Any]:
    """Delete subscription

     Delete subscription

    Args:
        package_id (str):
        event_kind (EventKindId): Event kind:
              * `0` - New package release
              * `1` - Security alerts
              * `2` - Repository tracking errors
              * `4` - Repository scanning errors

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        package_id=package_id,
        event_kind=event_kind,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
