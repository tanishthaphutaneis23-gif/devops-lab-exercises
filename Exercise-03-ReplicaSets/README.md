# Exercise 3: Scaling a Flask App with ReplicaSets

## Files
- `app.py` — flash-sale Flask app with `/`, `/buy`, and `/health` endpoints.
- `Dockerfile` — builds the `flashsale:1.0` image.
- `flashsale-replicaset.yaml` — ReplicaSet and ClusterIP Service with health probes and resource settings.

## What I did
Built `flashsale:1.0`, pushed the tagged image `tanishthaise/flashsale:1.0` to Docker Hub, started a one-node Minikube cluster, and applied the ReplicaSet manifest. I verified three Pods, scaled the ReplicaSet to five, deleted one Pod, and verified Kubernetes replaced it. `kubectl get pods -o wide` showed all five Pods on the single `minikube` node.

## Observed results
- Initial ReplicaSet: 3 desired and ready Pods.
- After scaling: 5 desired and ready Pods.
- After deleting a Pod: a replacement Pod appeared; the ReplicaSet still had 5 ready Pods.
- Node count: 1; all five Pods ran on `minikube`.

## Questions and answers

1. **What was the initial number of replicas?** 3.
2. **How many Pods ran after applying the ReplicaSet?** 3.
3. **What happened when it was scaled to 5?** Kubernetes created two more Pods to reach five.
4. **What happened when one Pod was deleted?** The ReplicaSet created a replacement Pod to maintain five.
5. **How does Kubernetes maintain the desired count?** The ReplicaSet controller continually compares actual Pods with the desired count and creates or removes Pods to match it.
6. **How many nodes were running?** 1.
7. **Where were the five Pods running?** All five were on the single `minikube` node.
