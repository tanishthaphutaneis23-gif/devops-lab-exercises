# Exercise 2: Deploy a Flask App on Minikube

## Files
- `app.py` — Flask page returning `Hello from Flask on Kubernetes!` on port 15000.
- `Dockerfile` — builds the Flask container image.
- `flask-deployment.yaml` — Kubernetes Deployment and NodePort Service.

## What I did
Built the `flask-app` image, loaded it into Minikube, applied the YAML, checked the Deployment and running Pod, inspected the Deployment and logs, and exposed the app with `flask-app-service`.

## Result
`minikube service flask-app-service --url` returned a local URL. Curling that URL returned:

```text
Hello from Flask on Kubernetes!
```

## Questions and answers

1. **What is the purpose of `minikube service flask-app-service --url`?**
   It provides a URL for accessing the service running in Minikube.

2. **What happens when you run that command?**
   Minikube checks the service, generates an access URL, and displays it.

3. **Why is `targetPort` used in a Kubernetes Service?**
   It specifies the port on which the application is listening inside the container.

4. **What is the difference between `port` and `targetPort`?**
   `port` is the Service port; `targetPort` is the container port receiving the traffic.

5. **How do you access a Flask app running in Minikube?**
   Run `minikube service flask-app-service --url` and open the returned URL, or send a request to it with curl.

6. **Why may the terminal need to remain open when using the Docker driver?**
   Minikube’s service tunnel runs through that terminal session.

7. **What is the benefit of the `--url` flag?**
   It prints the service URL so you can access it without constructing the URL yourself.

8. **What command can expose an app as a Kubernetes Service?**
   `kubectl expose`, or a Service resource applied with `kubectl apply -f`.

9. **How does Minikube help with local Kubernetes testing?**
   It runs a Kubernetes cluster locally, allowing deployments to be tested without a remote cluster.

10. **What is `kubectl` used for?**
    It is the command-line tool for creating, inspecting, and managing Kubernetes resources.
