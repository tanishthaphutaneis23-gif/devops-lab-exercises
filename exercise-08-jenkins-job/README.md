# Exercise 8: Jenkins Hello World Job

## Goal

Run a tracked shell script as a Jenkins job and retain the console output as evidence.

## Work

`hello-world.sh` is executable and prints the expected greeting. Jenkins runs it in the `Exercise-08-Hello-World` Freestyle project with an Execute shell build step.

## Verification

Build #1 completed with `SUCCESS`; its console output contains `Hello, Jenkins!`.
