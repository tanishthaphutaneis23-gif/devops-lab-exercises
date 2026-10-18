# Exercise 7: Jenkins CI Automation

## Goal

Set up a Jenkins CI server and run a build job.

## Work

Jenkins is run locally in Docker Desktop using `jenkins-lab/compose.yaml`. The custom image adds Python and Git so the later Python pipeline can build and test projects. The Jenkins ports are bound to localhost.

## Verification

Jenkins started locally in Docker Desktop. The `Exercise-07-CI-Build` Freestyle job completed build #2 successfully, reporting Python 3.13.5 and Git 2.47.3 and parsing the tracked Python app and metrics exporter sources. Jenkins data and the initial local admin token remain outside Git.
