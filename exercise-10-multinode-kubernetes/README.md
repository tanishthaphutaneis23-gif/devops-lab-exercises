# Exercise 10: Multi-Node, Multi-App Minikube Deployment

## Goal

Deploy a product catalog with two replicas and a shopping cart with three replicas across a three-node Minikube cluster.

## Work

The two Flask apps, Dockerfiles, and Kubernetes manifests are included. All resources use the `default` namespace consistently, correcting the namespace mismatch in the lab's sample. Required pod anti-affinity spreads replicas of each app across distinct nodes.

## Verification

- Started the `devops-multinode` profile with three nodes; all three reached `Ready`.
- Loaded the two locally built images into the Minikube profile.
- The Product Catalog Deployment reached 2/2 Ready and its Pods ran on m02 and m03.
- The Shopping Cart Deployment reached 3/3 Ready and its Pods ran across the control-plane node, m02, and m03.
- Both services exposed NodePorts. Port-forward checks returned the three product records and confirmed the cart GET/POST/GET flow.

All manifests consistently use the `default` namespace, addressing the namespace mismatch in the upstream sample.
