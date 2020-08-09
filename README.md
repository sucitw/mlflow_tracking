# mlflow_tracking
Artefacts to deploy and use MLFLow Tracking Server  


> Build a docker image
Working dir = root folder of this code repo
```
docker build --no-cache -t suci/mlflow-tracking .
```

> Launch MLFlow Tracking server in Docker
```
docker run -d -p 5000:5000 \
    --name mlflow-tracking-server suci/mlflow-tracking```
```

