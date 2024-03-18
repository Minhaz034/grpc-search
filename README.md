### Description:
The dockerfile of the containerized server is located in the 'server' directory.
Three separately containerized clients are implemented namely:
- client 1
- client 2
- client 3 
.They can be found in the example.com/grpc-client directory.

In the root directory a docker-compose.yml file is located that handles:
 - creating grpc-network in which server and the clients reside
 - running the server container
 - running the client containers that depend on the server container thus running the project

### Running the project:
From the root directory, run
```
docker compose up --build
```

