# MLflow_Tracking
Artifacts to deploy and use MLfLow Tracking Server  


## Build a docker image

Working dir = the root folder of this code repo
```
docker build --no-cache -t suci/mlflow-tracking .
```

## Launch MLflow Tracking server in Docker

```
docker run -d -p 5000:5000 \
    -v /tmp/mlflow/artifactStore:/tmp/mlflow/artifactStore \
    --name mlflow-tracking-server suci/mlflow-tracking
```

## Run sample code

Directly run demo code after checking environment variables 

- pycontw2020_demo.py

## Check results

Connect to MLflow server (default:"http://localhost:5000")