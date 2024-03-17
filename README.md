### Description:
The dockerfile of the containerized server is located in the 'server' directory
and the one for the client is in the example.com/grpc-client directory.
In the root directory a docker-compose.yml file is located that handles:
 - creating grpc-network in which server and the clients reside
 - running the server container
 - running the server container that depends on the server container thus running the project

### Running the project:
From the root directory, run
```
docker compose up --build
```
