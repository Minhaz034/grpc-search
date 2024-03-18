# FROM golang:1.19 as builder

# WORKDIR /app

# COPY go.* ./

# RUN go mod download

# # Copy the rest of the application's source code
# COPY . .


# # Change WORKDIR to the client1 directory
# WORKDIR /app/client1

# RUN CGO_ENABLED=0 GOOS=linux go build -o client1 .

# FROM alpine:latest  

# WORKDIR /root/

# COPY --from=builder /app/client1/client1 .
# COPY --from=builder /app/client1/index.html .


# EXPOSE 8080

# # Command to run the executable
# CMD ["./client1"]






FROM golang:1.19 as builder

WORKDIR /app

ARG CLIENT_DIR=client1

COPY go.* ./
COPY image_search*.pb.go ./


RUN go mod download

COPY ${CLIENT_DIR}/ ./client


WORKDIR /app/client

# Build the client application.
RUN CGO_ENABLED=0 GOOS=linux go build -o client .

# Start a new stage from scratch for a smaller final image.
FROM alpine:latest  

WORKDIR /root/

# Copy the built binary and the HTML file from the build stage to the final image.
COPY --from=builder /app/client/client .
COPY --from=builder /app/client/index.html .

# Expose port 8080 for the client service.
EXPOSE 8080

# Specify the command to run the client application.
CMD ["./client"]
