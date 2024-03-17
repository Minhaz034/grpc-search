### Running the server container:
change the directory to /server :
```
cd server
```
Then run:
```
docker compose up --build
```

Running client 1:
```
docker run -d -p 8080:8080 --name grpc-client1 grpc-client
```
