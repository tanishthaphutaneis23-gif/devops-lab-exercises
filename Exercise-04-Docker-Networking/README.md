\# Exercise 4: Docker Networking with Multiple Containers



\## What I built



A Flask REST API, a MySQL container, and a Redis container connected to the `my-bridge-net` Docker bridge network.



\## Files



\- `app.py` — Flask API with a `/about` endpoint.

\- `requirements.txt` — Flask and a compatible Werkzeug version.

\- `Dockerfile` — builds the Flask image.



\## Verification



\- Created and inspected the `my-bridge-net` bridge network.

\- Started the Flask, MySQL, and Redis containers on that network.

\- `curl.exe http://localhost:5001/about` returned the API’s JSON response.

\- From inside the Flask container, `ping -c 4 mysql` and `ping -c 4 redis` each received 4 replies.

\- Stopped and removed the three containers, then removed `my-bridge-net`.



\## Questions and answers



1\. \*\*What does the `--net` flag do?\*\*  

&#x20;  It connects a container to the specified Docker network.



2\. \*\*How do containers communicate on the same network?\*\*  

&#x20;  They can reach each other by container name or IP address. Here, Flask reached `mysql` and `redis` by name.



3\. \*\*What is the difference between bridge and host networking?\*\*  

&#x20;  A bridge network gives containers an isolated network where they can communicate. Host networking shares the host’s network stack.



4\. \*\*How can you expose a container port to the host?\*\*  

&#x20;  Use `-p HOST\_PORT:CONTAINER\_PORT`. For this app, `-p 5001:5001` published container port 5001 on host port 5001.

