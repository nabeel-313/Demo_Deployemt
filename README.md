# Demo_Deployemt
This repo all about demo of deployment on ECS, EKS

## Run code quality checks
```
pylint app.py test_maths_ops.py
mypy app.py test_maths_ops.py
```

## Configured github action to deploy on ECR
```
cmd for deployment of image you find in ECR after creating repo
after that create cluster on ECS, create task defination and add the task
```
## Configure inbound and outbound rule
```
In ECS container to go networking -->> Security group ID -->> Update Inbound and Outbund rule
```



