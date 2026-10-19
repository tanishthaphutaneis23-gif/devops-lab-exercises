# Exercise 5: Docker Security with AppArmor

## Objective

Build a Flask container and use a custom AppArmor profile to restrict access to sensitive files and prevent execution of selected binaries. Use the Docker SDK for Python to apply and verify the profile, then test the restrictions.

## Files

- `app.py` — Flask application on port 5000.
- `Dockerfile` — builds the `flask-apparmor` image.
- `my-apparmor-profile` — AppArmor policy for the container process.
- `apply_apparmor.py` — builds the image, starts a container with the profile, verifies the active profile, and removes the container.
- `test_restricted_actions.py` — checks that the confined process cannot read `/etc/passwd` or launch `/bin/bash`.
- `requirements.txt` — Python Docker SDK dependency.

## Environment and setup

This exercise was run in Ubuntu 26.04 on WSL 2 with AppArmor enabled and Docker Engine installed inside the Ubuntu distribution. Docker Desktop's WSL integration runs its engine in a separate `docker-desktop` distribution, so the profile loaded in Ubuntu was not enforced by that engine. The checks below were therefore run against the Ubuntu-local Docker Engine.

Enable AppArmor in WSL by adding this to the Windows file `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
kernelCommandLine=apparmor=1 security=apparmor
```

After saving, run `wsl --shutdown` in PowerShell and reopen Ubuntu. In Ubuntu, install the AppArmor tools and Python virtual-environment support, and install Docker Engine using Docker's official Ubuntu instructions. Then prepare the project environment:

```bash
sudo apt update
sudo apt install -y apparmor-utils python3-venv
cd /mnt/c/Users/Admin/devops-exercise-5
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Load the profile and run the scripts from the project directory:

```bash
sudo install -m 0644 my-apparmor-profile /etc/apparmor.d/my-apparmor-profile
sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
sudo .venv/bin/python apply_apparmor.py
sudo .venv/bin/python test_restricted_actions.py
```

The profile includes a signal receive rule for unconfined processes so the Docker daemon can stop the confined container during cleanup.

## Verification results

- `apply_apparmor.py` confirmed `AppArmor profile applied: ['apparmor=my-apparmor-profile']` and `Active AppArmor profile: my-apparmor-profile`.
- The test script reported `PASS` for blocking reads of `/etc/passwd` and execution of `/bin/bash` from within the confined Python process.
- The test container was removed after the checks.

## Questions and answers

1. **What is the purpose of using AppArmor with Docker containers?**  
   AppArmor adds a host-kernel security policy that confines what a container process can access or do.

2. **How do AppArmor profiles help secure a Docker container?**  
   Profiles define rules for file access, network use, capabilities, and program execution. The kernel enforces those rules for processes using the profile.

3. **Why restrict access to `/etc/` and `/var/`?**  
   These directories can contain system configuration, service data, and logs. Limiting access reduces the chance that a compromised process reads or changes sensitive files.

4. **What other capabilities can AppArmor restrict?**  
   AppArmor can restrict network operations, files and directories, program execution, mounts, and Linux capabilities such as `sys_admin`.

5. **How can you verify that a profile is applied?**  
   Inspect the container's `HostConfig.SecurityOpt` and `AppArmorProfile` through the Docker SDK or Docker CLI. Also check that the profile is loaded in enforce mode with `sudo aa-status`, and verify the restrictions with controlled tests.
