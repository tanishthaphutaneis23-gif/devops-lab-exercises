# Exercise 5: Docker Security with AppArmor

## Goal

Run the Flask container under an AppArmor profile and verify that restricted actions are denied.

## Work

The Flask app, Dockerfile, named AppArmor profile, and Docker SDK scripts are included. The `/security-check` endpoint attempts to write under `/etc`; it returns HTTP 403 if the profile blocks the write and HTTP 500 if the write unexpectedly succeeds. The profile also denies reads of `/etc/passwd` and `/etc/shadow`, and execution from `/bin` and `/usr/bin`.

AppArmor profiles must be loaded by a Linux host kernel before Docker can apply them. On Ubuntu, from this directory:

```bash
sudo apt-get update
sudo apt-get install -y apparmor-utils
sudo aa-status
docker build -t flask-apparmor .
sudo install -m 0644 my-apparmor-profile /etc/apparmor.d/my-apparmor-profile
sudo apparmor_parser -r -W /etc/apparmor.d/my-apparmor-profile
docker run --rm -d --name flask-apparmor --security-opt apparmor=my-apparmor-profile -p 127.0.0.1:5000:5000 flask-apparmor
curl -i http://127.0.0.1:5000/
curl -i http://127.0.0.1:5000/security-check
docker rm -f flask-apparmor
python3 -m pip install -r requirements.txt
python3 apply_apparmor.py
python3 test_restricted_actions.py
sudo dmesg | grep apparmor
```

The Docker SDK script builds and starts a container with the loaded profile, inspects the container's `HostConfig.SecurityOpt`, checks the HTTP endpoint, then stops and removes the container. The restricted-action script checks that reading `/etc/passwd` and executing `/bin/bash` fail.

## Environment result

This workstation is macOS with Docker Desktop. Its host-side AppArmor profile workflow is not available to this Mac CLI, so run the commands above on an AppArmor-enabled Ubuntu host; no enforcement result is claimed until that check succeeds there.
