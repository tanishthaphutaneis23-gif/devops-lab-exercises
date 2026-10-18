# Exercise 1: Hello Pod

## Goal
Run an Nginx container as a Kubernetes Pod and open its welcome page.

## Commands run

```powershell
minikube start --driver=docker
kubectl run hello-k8s --image=nginx --port=80
kubectl get pods
kubectl expose pod hello-k8s --type=NodePort --port=80
minikube service hello-k8s
```

## Result
The Pod reached `Running`, the `hello-k8s` NodePort Service was created, and the browser displayed the Nginx welcome page.

## Reusable manifest
`hello-k8s.yaml` contains an equivalent Pod and Service definition for recreating the result. The original exercise was run with the `kubectl run` and `kubectl expose` commands above; this manifest was not used for that original run.
