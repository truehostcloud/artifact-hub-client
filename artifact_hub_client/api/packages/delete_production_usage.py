from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.repository_kind_param import RepositoryKindParam
from ...types import Response


def _get_kwargs(
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    org_name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/packages/{repoKindParam}/{repoName}/{packageName}/production-usage/${orgName}".format(
        client.base_url, repoKindParam=repo_kind_param, repoName=repo_name, packageName=package_name, orgName=org_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
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
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    org_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete organization from package's production usage list

     Delete organization from package's production usage list

    Args:
        repo_kind_param (RepositoryKindParam): Repository kind name:
            * `helm` - Helm charts
            * `falco` - Falco rules
            * `opa` - OPA policies
            * `olm` - OLM operators
            * `tbaction` - Tinkerbell actions
            * `krew` - Krew kubectl plugins
            * `helm-plugin` - Helm plugins
            * `tekton` - Tekton tasks
            * `keda-scaler` - KEDA scalers
            * `coredns` - Core DNS plugins
            * `keptn` - Keptn integrations
            * `tekton-pipeline` - Tekton pipelines
            * `container` - Container images
            * `kubewarden` - Kubewarden policies
            * `gatekeeper` - Gatekeeper policies
            * `kyverno` - Kyverno policies
            * `knative-client-plugin` - Knative client plugins
            * `backstage` - Backstage plugins
            * `argo-template` - Argo templates
            * `kubearmor` - KubeArmor policies
        repo_name (str):  Example: repoName.
        package_name (str):  Example: pkg1.
        org_name (str):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        repo_kind_param=repo_kind_param,
        repo_name=repo_name,
        package_name=package_name,
        org_name=org_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    org_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete organization from package's production usage list

     Delete organization from package's production usage list

    Args:
        repo_kind_param (RepositoryKindParam): Repository kind name:
            * `helm` - Helm charts
            * `falco` - Falco rules
            * `opa` - OPA policies
            * `olm` - OLM operators
            * `tbaction` - Tinkerbell actions
            * `krew` - Krew kubectl plugins
            * `helm-plugin` - Helm plugins
            * `tekton` - Tekton tasks
            * `keda-scaler` - KEDA scalers
            * `coredns` - Core DNS plugins
            * `keptn` - Keptn integrations
            * `tekton-pipeline` - Tekton pipelines
            * `container` - Container images
            * `kubewarden` - Kubewarden policies
            * `gatekeeper` - Gatekeeper policies
            * `kyverno` - Kyverno policies
            * `knative-client-plugin` - Knative client plugins
            * `backstage` - Backstage plugins
            * `argo-template` - Argo templates
            * `kubearmor` - KubeArmor policies
        repo_name (str):  Example: repoName.
        package_name (str):  Example: pkg1.
        org_name (str):  Example: org1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        repo_kind_param=repo_kind_param,
        repo_name=repo_name,
        package_name=package_name,
        org_name=org_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
