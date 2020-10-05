![](images/MLflow.jpg)
# MLflow_Tracking

Artifacts to deploy and use MLfLow Tracking Server  
The docker file and demo codes have been tested in Mac OS successfully. For Win env, some configurations may be changed.

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

Install requirement libraries accordingly

Run demo code after checking environment variables

- pytw2020_demo.py
- pytw2020_demo_SK_model.py
- pytw2020_demo_autologging.py

## Check results

Connect to MLflow server (default:"http://localhost:5000")