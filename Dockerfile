FROM continuumio/miniconda3

# Environment virables
ENV MLFLOW_HOME /opt/mlflow
ENV MLFLOW_VERSION 1.10.0
ENV SERVER_PORT 5000
ENV SERVER_HOST 0.0.0.0
ENV FILE_STORE ${MLFLOW_HOME}/fileStore
ENV ARTIFACT_STORE ${MLFLOW_HOME}/artifactStore

RUN apt-get update && \
# install prequired modules to support install of mlflow and related components
    apt-get install -y default-libmysqlclient-dev build-essential curl \
# cmake and protobuf-compiler required for onnx install
    cmake protobuf-compiler 

# install mflow
RUN pip install mlflow==${MLFLOW_VERSION} && \
# Working environment setup
# create related folder
    mkdir -p ${MLFLOW_HOME}/scripts && \
    mkdir -p ${FILE_STORE} && \
    mkdir -p ${ARTIFACT_STORE} 

COPY scripts/run.sh ${MLFLOW_HOME}/scripts/run.sh

EXPOSE ${SERVER_PORT}/tcp

VOLUME ["${MLFLOW_HOME}/scripts/", "${FILE_STORE}", "${ARTIFACT_STORE}"]

WORKDIR ${MLFLOW_HOME}

ENTRYPOINT ["./scripts/run.sh"]
