# Exercise 5: Docker Security with AppArmor

## Goal

Run the Flask container under an AppArmor profile and verify that restricted actions are denied.

## Work

The Flask app, Dockerfile, and example profile are included. The `/security-check` endpoint attempts a write under `/etc`; it returns HTTP 403 only when the profile blocks that write, and HTTP 500 if the write unexpectedly succeeds. AppArmor profiles must be loaded by a Linux host kernel before Docker can apply them.

On a supported Ubuntu host, build the image, load the profile with `sudo apparmor_parser -r -W my-apparmor-profile`, and run the container with `--security-opt apparmor=/usr/local/bin/python`. Then verify `/` returns HTTP 200 and `/security-check` returns HTTP 403. Confirm the denied operation in `sudo dmesg | grep apparmor`.

## Environment result

This workstation is macOS with Docker Desktop's Linux VM. The profile must be tested on a Linux host that exposes AppArmor support to Docker. No AppArmor enforcement result is claimed until that check is run in a supported Linux environment.
