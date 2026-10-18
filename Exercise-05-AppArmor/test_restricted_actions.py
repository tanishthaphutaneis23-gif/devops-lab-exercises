"""Check that the custom AppArmor profile blocks sensitive reads and shell use."""

from pathlib import Path

import docker
from docker.errors import APIError, DockerException


HERE = Path(__file__).resolve().parent
IMAGE = "flask-apparmor:latest"
PROFILE = "my-apparmor-profile"


def main():
    client = docker.from_env()
    container = None
    try:
        client.images.build(path=str(HERE), tag=IMAGE)
        container = client.containers.run(
            IMAGE,
            detach=True,
            name="flask-apparmor-restriction-test",
            security_opt=[f"apparmor={PROFILE}"],
        )

        commands = (
            ["/usr/local/bin/python", "-c", "open('/etc/passwd').read()"],
            ["/bin/bash", "-c", "echo should-not-run"],
        )
        for command in commands:
            try:
                result = container.exec_run(command)
                denied = result.exit_code != 0
                output = result.output.decode("utf-8", errors="replace").strip()
            except APIError as exc:
                denied = True
                output = str(exc)

            print(f"$ {' '.join(command)}")
            print(f"  blocked={denied}; output={output or '(no output)'}")
            if not denied:
                raise SystemExit(
                    f"AppArmor did not block the restricted action: {' '.join(command)}"
                )

        print("Both restricted actions were denied.")
    except DockerException as exc:
        raise SystemExit(
            "Docker could not run the test container. Confirm Docker is running "
            "and the AppArmor profile is loaded on the Linux host. "
            f"Details: {exc}"
        ) from exc
    finally:
        if container is not None:
            container.stop()
            container.remove()
        client.close()


if __name__ == "__main__":
    main()
