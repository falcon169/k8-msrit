# hello-python
Very simple hello world python Flask application.

cd hello-python/app
docker build -f ../docker/Dockerfile -t hello-python:latest .
kubectl apply -f ../kubernetes/deployment.yaml
kubectl get services/hello-python-service -o go-template='{{(index .spec.ports 0).nodePort}}'

curl $(minikube ip):nodePort
