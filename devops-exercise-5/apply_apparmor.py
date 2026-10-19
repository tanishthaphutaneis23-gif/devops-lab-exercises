import docker

PROFILE = "my-apparmor-profile"
IMAGE = "flask-apparmor"
client = docker.from_env()

client.images.build(path=".", tag=IMAGE)
container = client.containers.run(
    IMAGE,
    ports={"5000/tcp": 5000},
    security_opt=[f"apparmor={PROFILE}"],
    detach=True,
)
try:
    info = client.api.inspect_container(container.id)
    print(f"Container started: {container.short_id}")
    print(f"AppArmor profile applied: {info['HostConfig']['SecurityOpt']}")
    print(f"Active AppArmor profile: {info['AppArmorProfile']}")
    if info["AppArmorProfile"] != PROFILE:
        raise RuntimeError(f"Expected {PROFILE}, got {info['AppArmorProfile']!r}")
finally:
    container.remove(force=True)