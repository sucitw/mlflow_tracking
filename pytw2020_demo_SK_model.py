import os
import numpy as np
import mlflow
from sklearn.linear_model import LogisticRegression
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts, sklearn


if __name__ == "__main__":
    # Setup & Initialize MLflow experiment
    experiment_name = "Sklearn demo"
    tracking_server = "http://localhost:5000"

    mlflow.set_tracking_uri(tracking_server)
    mlflow.set_experiment(experiment_name)

    # Useful for multiple runs (only doing one run in this sample notebook)   
    with mlflow.start_run() as run:
        print("Running the '{}' script ...".format(experiment_name))

        # Log a parameter (key-value pair)
        X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
        y = np.array([0, 0, 1, 1, 1, 0])
        lr = LogisticRegression()
        lr.fit(X, y)
        score = lr.score(X, y)
        print("Score: %s" % score)
        mlflow.log_metric("score", score)
        mlflow.sklearn.log_model(lr, "model")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)