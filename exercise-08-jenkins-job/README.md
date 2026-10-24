# Exercise 08 — Jenkins Hello World job

1. Commit `hello-world.sh` and `Jenkinsfile` to a Git repository you control.
2. In Jenkins, choose **New Item → Pipeline**.
3. Under Pipeline, choose **Pipeline script from SCM**, select Git, and provide your repository URL and credentials if private.
4. Save and click **Build Now**. Inspect **Console Output** for the script output.

The repository must be reachable by the Jenkins controller/agent. Do not commit a GitHub personal access token; use Jenkins credentials for private repositories.
