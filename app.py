from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello, this is a secure Flask application running inside a Docker container!"


@app.get("/security-check")
def security_check():
    try:
        with open("/etc/apparmor-exercise-denied", "w", encoding="utf-8") as protected_file:
            protected_file.write("This write should be blocked by AppArmor.\n")
    except PermissionError:
        return "AppArmor blocked the protected-file write.\n", 403
    return "The protected-file write was unexpectedly allowed.\n", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
