import docker

PROFILE = "my-apparmor-profile"
IMAGE = "flask-apparmor"
NAME = "flask-apparmor-restriction-test"
client = docker.from_env()

try:
    client.containers.get(NAME).remove(force=True)
except docker.errors.NotFound:
    pass

container = client.containers.run(
    IMAGE,
    name=NAME,
    ports={"5000/tcp": 5000},
    security_opt=[f"apparmor={PROFILE}"],
    detach=True,
)
try:
    code, output = container.exec_run(
        ["python", "-c", "print(open('/etc/passwd').read())"]
    )
    text = output.decode(errors="replace")
    if code == 0:
        print("FAIL: reading /etc/passwd was allowed")
    else:
        print(f"PASS: reading /etc/passwd was blocked (exit {code}): {text.strip()}")

    code, output = container.exec_run(
        [
            "python",
            "-c",
            "import subprocess; subprocess.run(['/bin/bash', '-c', 'echo EXECUTED'], check=True)",
        ]
    )
    text = output.decode(errors="replace")
    if code != 0 and "PermissionError" in text:
        print(f"PASS: executing /bin/bash was blocked (exit {code}): {text.strip()}")
    else:
        print(f"FAIL: expected AppArmor to block /bin/bash (exit {code}): {text.strip()}")
finally:
    container.remove(force=True)
    print("Container removed")
