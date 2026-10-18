"""Build and run the Flask container with the custom AppArmor profile."""

from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import docker
from docker.errors import DockerException


HERE = Path(__file__).resolve().parent
IMAGE = "flask-apparmor:latest"
PROFILE = "my-apparmor-profile"


def main():
    client = docker.from_env()
    container = None
    try:
        print(f"Building {IMAGE} from {HERE}...")
        client.images.build(path=str(HERE), tag=IMAGE)
        container = client.containers.run(
            IMAGE,
            detach=True,
            name="flask-apparmor-check",
            ports={"5000/tcp": ("127.0.0.1", 5000)},
            security_opt=[f"apparmor={PROFILE}"],
        )

        info = client.api.inspect_container(container.id)
        security_options = info["HostConfig"].get("SecurityOpt") or []
        expected_option = f"apparmor={PROFILE}"
        if expected_option not in security_options:
            raise RuntimeError(
                f"Expected {expected_option!r} in container SecurityOpt; "
                f"got {security_options!r}"
            )

        print(f"Container started: {container.short_id}")
        print(f"Docker reports the profile is attached: {security_options}")
        deadline = time.monotonic() + 20
        while True:
            try:
                with urlopen("http://127.0.0.1:5000/", timeout=2) as response:
                    body = response.read().decode("utf-8")
                    if response.status != 200:
                        raise RuntimeError(f"Home endpoint returned HTTP {response.status}")
                    print(f"Home endpoint returned HTTP {response.status}: {body}")
                break
            except URLError as exc:
                if time.monotonic() >= deadline:
                    raise RuntimeError(f"Flask did not become ready: {exc}") from exc
                time.sleep(0.5)
        try:
            with urlopen("http://127.0.0.1:5000/security-check", timeout=2) as response:
                raise RuntimeError(
                    f"The restricted write unexpectedly returned HTTP {response.status}"
                )
        except HTTPError as exc:
            if exc.code != 403:
                raise
            print("Security-check returned HTTP 403 as expected.")
    except DockerException as exc:
        raise SystemExit(
            "Docker could not build or start the container. Confirm Docker is "
            "running and the AppArmor profile is loaded on the Linux host. "
            f"Details: {exc}"
        ) from exc
    finally:
        if container is not None:
            container.stop()
            container.remove()
            print("Container stopped and removed.")
        client.close()


if __name__ == "__main__":
    main()
