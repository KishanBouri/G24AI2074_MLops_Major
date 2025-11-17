# G24AI2074_MLops_Major
 # Project Overview

This project implements a complete MLOps pipeline for training, testing, containerizing, and deploying a machine learning model using:

1.Python + Scikit-learn

2.GitHub Branching Strategy (main, dev, docker_cicd)

3.GitHub Actions CI/CD

4.Docker & Docker Hub

5.Kubernetes Deployment (3 replicas)


# Repository Structure
G24AI2074_MLops_Major/
│
├── README.md
├── .gitignore
│
├── src/
│   ├── train.py
│   └── test.py
│
├── model/
│   └── savedmodel.pth
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── upload.html
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
└── .github/
    └── workflows/
        ├── ci.yml
        └── docker-ci.yml


# Branching Strategy

The repository strictly follows:

# 1. main branch

Contains only README.md and .gitignore

No model, no Docker files

Stable production reference branch

# 2. dev branch

Contains:

train.py

test.py

ci.yml

CI runs automatically on push

# 3. docker_cicd branch

Contains:

Flask app (app/)

Dockerfile

Kubernetes deployment + service files

docker-ci.yml (GitHub Actions for building/pushing Docker images)

# Model

Dataset: Olivetti Faces (sklearn)

Model: DecisionTreeClassifier

Train/test split: 70/30

Model is saved as model/savedmodel.pth

# CI/CD Workflows
 # ci.yml

Runs on main + dev + docker_cicd

Installs dependencies

Runs train.py

Runs test.py

Logs accuracy

# docker-ci.yml

Runs on docker_cicd

Builds Docker image

Pushes to:
docker.io/kishan2074/mlops-app:latest

GitHub Secrets used:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

# Docker:
  #Build: docker build -t mlops-app:latest .
  #Run: docker run -p 5000:5000 mlops-app:latest

  App opens at:
    http://localhost:5000/
  
# Kubernetes Deployment
  #Apply: kubectl apply -f k8s/deployment.yaml
          kubectl apply -f k8s/service.yaml

 #Get pods: kubectl get pods
 
Should show 3 replicas running.

#Get service: kubectl get svc

App exposed at:
 http://localhost:30007/


# Live URLs
 GitHub Repository

https://github.com/KishanBouri/G24AI2074_MLops_Major

 Docker Hub Repository

https://hub.docker.com/r/kishan2074/mlops-app

 # Conclusion

This project successfully demonstrates:

End-to-end MLOps workflow

CI/CD automation

Containerization

Cloud-native deployment with Kubernetes

The entire assignment requirements are completed and validated.


  


