# hello-python-service
#service, deployment, NodePort, ClusterIP, PodIP
Very simple hello world python Flask application.

cd k8-msrit/app
docker build -f ../docker/Dockerfile -t hello-python:latest .
kubectl apply -f ../kubernetes/deployment.yaml
NodePort=$(kubectl get services/hello-python-service -o go-template='{{(index .spec.ports 0).nodePort}}')
#External Access
curl $(minikube ip):$NodePort

#Internal ClusterIP Access 
kubectl exec -it hello-python-6c7b478cf5-blhcv -- bash
root@hello-python-6c7b478cf5-blhcv:/# curl hello-python-service.default.svc:6000

#Internal Pod Access
kubectl exec -it hello-python-6c7b478cf5-blhcv -- curl $(hostname -i):5000
