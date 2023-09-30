# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml (file where all the columns of the data are mentioned, including their data types: for data validation)
3. Update params.yaml (paramaters used throughout the project: for model training)

---- THESE STEPS WILL BE DIFFERENT IN EACH STAGE OF THE PIPELINE ----

4. Update the entity folder
5. Update the configuration manager in src config folder
6. Update the components (data ingestion, validation, transformation, etc.)

---- THESE STEPS WILL BE DIFFERENT IN EACH STAGE OF THE PIPELINE ----

7. Update the pipeline folder (two separate pipelines for training and prediction)
8. Update the main.py
9. Update the app.py (UI related functionality) 



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/miguelhermar/MLflow-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/miguelangel.hermar410/MLflow-Project.mlflow \
MLFLOW_TRACKING_USERNAME=miguelangel.hermar410 \
MLFLOW_TRACKING_PASSWORD=838058e049ff14335ccc9b935c026e41b1001293 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/miguelangel.hermar410/MLflow-Project.mlflow

export MLFLOW_TRACKING_USERNAME=miguelangel.hermar410

export MLFLOW_TRACKING_PASSWORD=838058e049ff14335ccc9b935c026e41b1001293

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policies for IAM User:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	# Security Credentials for IAM User:
	security credentials>create access key (CLI)

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 714501908979.dkr.ecr.us-east-2.amazonaws.com/mlflow_proj

	
## 4. Create EC2 machine (Ubuntu, Select Instance Type, Select Key pair to access VM from any 3r)party) 
Allow HTTP and HTTPS, also config size 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optimal

	sudo apt-get update -y # apt-get is a utility for installing, updating, and removing packages on Debian-based Linux systems. It's a command-line tool to manage software on the system.

	sudo apt-get upgrade # upgrade all installed packages to their latest versions.
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh # install docker on VM

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

	docker --version (verify that docker is installed)
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

	A self-hosted runner is a server that hosts the runner application which listens for available jobs in GitHub Actions or other CI/CD (Continuous Integration/Continuous Deployment) systems. When a job becomes available, the runner application on the server picks it up and runs the job on that server.


# 7. Setup github secrets:

	secrets and variables>actions>new repository secret

    AWS_ACCESS_KEY_ID=<from AWS account (csv file)>

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-2b

    AWS_ECR_LOGIN_URI = demo>>  714501908979.dkr.ecr.us-east-2.amazonaws.com

    ECR_REPOSITORY_NAME = mlflow_proj

# 8. Check Github Actions Workflows

# 9. Provide port number in AWS EC2 instance
	security>security groups>edit inbound rules>add rules>port 8080, host 0.0.0.0

# 10. Test Public IPv4 address and add port number



## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


