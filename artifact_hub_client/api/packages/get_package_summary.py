from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.package_summary import PackageSummary
from ...models.repository_kind_param import RepositoryKindParam
from ...types import Response


def _get_kwargs(
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/packages/{repoKindParam}/{repoName}/{packageName}/summary".format(
        client.base_url, repoKindParam=repo_kind_param, repoName=repo_name, packageName=package_name
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, PackageSummary]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PackageSummary.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, PackageSummary]]:
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
    *,
    client: Client,
) -> Response[Union[Any, PackageSummary]]:
    """Get package summary details

     Get package summary details

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PackageSummary]]
    """

    kwargs = _get_kwargs(
        repo_kind_param=repo_kind_param,
        repo_name=repo_name,
        package_name=package_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, PackageSummary]]:
    """Get package summary details

     Get package summary details

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PackageSummary]
    """

    return sync_detailed(
        repo_kind_param=repo_kind_param,
        repo_name=repo_name,
        package_name=package_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    *,
    client: Client,
) -> Response[Union[Any, PackageSummary]]:
    """Get package summary details

     Get package summary details

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PackageSummary]]
    """

    kwargs = _get_kwargs(
        repo_kind_param=repo_kind_param,
        repo_name=repo_name,
        package_name=package_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repo_kind_param: RepositoryKindParam,
    repo_name: str,
    package_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, PackageSummary]]:
    """Get package summary details

     Get package summary details

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PackageSummary]
    """

    return (
        await asyncio_detailed(
            repo_kind_param=repo_kind_param,
            repo_name=repo_name,
            package_name=package_name,
            client=client,
        )
    ).parsed
