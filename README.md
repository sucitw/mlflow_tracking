# MLflow_Tracking
Artefacts to deploy and use MLfLow Tracking Server  


> Build a docker image
Working dir = root folder of this code repo
```
docker build --no-cache -t suci/mlflow-tracking .
```

> Launch MLflow Tracking server in Docker
```
docker run -d -p 5000:5000 \
    -v /tmp/mlflow/artifactStore:/tmp/mlflow/artifactStore \
    --name mlflow-tracking-server suci/mlflow-tracking
```
