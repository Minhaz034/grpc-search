FROM golang:1.19 as builder

WORKDIR /app

COPY go.* ./

RUN go mod download

# Copy the rest of the application's source code
COPY . .


# Change WORKDIR to the client1 directory
WORKDIR /app/client1

RUN CGO_ENABLED=0 GOOS=linux go build -o client1 .

FROM alpine:latest  

WORKDIR /root/

COPY --from=builder /app/client1/client1 .
COPY --from=builder /app/client1/index.html .


EXPOSE 8080

# Command to run the executable
CMD ["./client1"]
