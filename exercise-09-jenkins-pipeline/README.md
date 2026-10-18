# Exercise 9: Jenkins Multi-Stage Pipeline

## Goal

Run Build, Test, and Deploy stages for a small Flask application.

## Work

`Jenkinsfile` copies the tracked project into the Jenkins workspace, builds a Python virtual environment, installs requirements, runs the unit test, and copies the app files into a mock deployment directory.

## Verification

The `Exercise-09-Multi-Stage-Pipeline` Jenkins Pipeline completed build #1 with `SUCCESS`. The Build stage installed Flask into a virtual environment, the Test stage passed `test_home`, and the Deploy stage copied `app.py` and `requirements.txt` into the mock deployment directory.
