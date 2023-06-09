from enum import Enum


class RepositoryKindParam(str, Enum):
    ARGO_TEMPLATE = "argo-template"
    BACKSTAGE = "backstage"
    CONTAINER = "container"
    COREDNS = "coredns"
    FALCO = "falco"
    GATEKEEPER = "gatekeeper"
    HELM = "helm"
    HELM_PLUGIN = "helm-plugin"
    KEDA_SCALER = "keda-scaler"
    KEPTN = "keptn"
    KNATIVE_CLIENT_PLUGIN = "knative-client-plugin"
    KREW = "krew"
    KUBEARMOR = "kubearmor"
    KUBEWARDEN = "kubewarden"
    KYVERNO = "kyverno"
    OLM = "olm"
    OPA = "opa"
    TBACTION = "tbaction"
    TEKTON_PIPELINE = "tekton-pipeline"
    TEKTON_TASK = "tekton-task"

    def __str__(self) -> str:
        return str(self.value)
