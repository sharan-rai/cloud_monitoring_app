GitHub

# Cloud Monitoring App on Kubernetes
This project effectively monitors the cloud resources with a containerized Python app in Docker, stored in AWS ECR, and deployed seamlessly via AWS EKS.
![cloud monitoring architecture (1)](https://github.com/sharan-rai/cloud_monitoring_app/assets/81572115/5b4372f1-3a78-40d0-9ab6-e0b515456031)

## Overview
This resource monitoring Python solution offers a graphical depiction of CPU and memory utilization, with notification when resource usage exceeds 80%. Containerized in Docker via Dockerfile, setup is simplified, with dependencies and configurations encapsulated for seamless deployment. Leveraging the boto3 Python library, the application is securely stored in AWS Elastic Container Registry (ECR), ensuring reliable image management and versioning. Deployment through AWS Elastic Kubernetes Service (EKS) facilitates efficient scaling and management on Kubernetes infrastructure, enabling seamless orchestration of resources.

## Prerequisites
* AWS account to use ECR (Elastic Container Registry) and EKS (Elastic Kubernetes Service).
* Programmatic access and AWS configured with CLI.
* Python3.
* Docker and Kubectl.

## Setup
1. Clone the Repository
 ```bash
  git clone https://github.com/sharan-rai/cloud_monitoring_app.git
 ```
2. Dockerizing the Flask App
* Build the Docker image using the Docker file from the repository.
 ```bash
 docker build -t <image_name> .
 ```
* Run the Docker container.
  - Flask application will be accesible from the local browser using http://localhost:5000.
 ```bash
  docker run -p 5000:5000 <image_name>
 ```
3. Push Docker image to AWS ECR
* Run the ecr.py file to create an ECR repository.
 ```bash
python3 ecr.py
 ```
* Push the Docker Image to the repository
 ```bash
docker push <ecr_repo_uri>:<tag>
 ```
4. Creating an AWS EKS cluster and deploying the app
* Create an EKS cluster using AWS console and add a node group.
* Edit the name of the image  along with your image Uri in eks.py file
* Run the eks.py file from the repository to create deployment and service in EKS programmatically using boto3 library.
 ```bash
python3 eks.py
 ```
* Check the pod staus and Deployment and Service in Kubernetes
 ```bash
 kubectl get pods -n default
 kubectl get deployment -n default
 kubectl get service -n default 
```
* Once the pod is in running state, run the port forward to expose the service
```bash
kubectl port-forward service/<service_name> 5000:5000
```






