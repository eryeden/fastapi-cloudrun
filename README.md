# fastapi-cloudrun

## Background

## Key features


## Prerequisites
- python 3.11
- poetry
- google-cloud-cli; to install, refer to [here](https://cloud.google.com/sdk/docs/install?hl=ja#deb).

## References


## Project memo

- Virtual environment set up
```bash
pyenv local 3.11.3
python -m venv .venv
poetry init
poetry shell
```

- FastAPI set up
```bash
poetry add fastapi[all]
```

## Fastapi deployment to docker

```bash
poetry export -f requirements.txt --output requirements.txt
```

Create dockerfile for fastapi and save it on the repository root.
```dockerfile
# Dockerfile
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup. Here we use the uvicorn.
CMD exec uvicorn helloworld.main:app --reload --host 0.0.0.0 --port $PORT
```

Deployment to the Cloud Run:
```bash
gcloud run deploy
```
Executing this command may result in the following error:
```bash
ERROR: (gcloud.run.deploy) INVALID_ARGUMENT: could not resolve source: googleapi: Error 403: *****@cloudbuild.gserviceaccount.com does not have storage.objects.get access to the Google Cloud Storage object. Permission 'storage.objects.get' denied on resource (or it may not exist)., forbidden
```
To resolve this issue, please refer to the [Google Cloud Build Troubleshooting Guide](https://cloud.google.com/build/docs/troubleshooting?hl=ja).




