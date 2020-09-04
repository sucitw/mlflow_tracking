import os
import mlflow
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts

if __name__ == "__main__":
    # Setup & Initialize MLflow experiment
    experiment_name = "Tracking api demo"
    tracking_server = "http://localhost:5000"

    mlflow.set_tracking_uri(tracking_server)
    mlflow.set_experiment(experiment_name)

    # Useful for multiple runs (only doing one run in this sample notebook)   
    with mlflow.start_run() as run:
        print("Running the '{}' script ...".format(experiment_name))

        # Log a parameter (key-value pair)
        log_param("param1", randint(0, 100))

        # Log a metric; metrics can be updated throughout the run
        log_metric("metricsA", random())
        log_metric("metricsA", random() + 1)
        log_metric("metricsA", random() + 2)
        log_metric("metricsB", random() + 2)

        # Log an artifact (output file)
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open("outputs/test.txt", "w") as f:
            f.write("hello world! Run info:{}".format(mlflow.active_run().info))
        log_artifacts("outputs")
        print("Save to: {}".format(mlflow.get_artifact_uri()))