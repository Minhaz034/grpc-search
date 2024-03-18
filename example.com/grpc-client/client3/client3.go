package main

import (
	"context"
	"log"
	"net/http"
	"text/template"
	"time"

	pb "example.com/grpc-client"
	"google.golang.org/grpc"
)

// func main() {
// 	// Set up a connection to the server.
// 	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
// 	if err != nil {
// 		log.Fatalf("did not connect: %v", err)
// 	}
// 	defer conn.Close()
// 	c := pb.NewImageSearchServiceClient(conn)

// 	// Contact the server and print out its response.
// 	keyword := "cat"
// 	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
// 	defer cancel()
// 	r, err := c.SearchImage(ctx, &pb.SearchRequest{Keyword: keyword})
// 	if err != nil {
// 		log.Fatalf("could not search: %v", err)
// 	}
// 	log.Printf("Image Data: %s", r)
// }

var tpl = template.Must(template.ParseFiles("index.html"))

func searchHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		tpl.Execute(w, nil)
		return
	}

	keyword := r.FormValue("keyword")
	// Set up a connection to the server.
	conn, err := grpc.Dial("grpc-server:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewImageSearchServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	res, err := c.SearchImage(ctx, &pb.SearchRequest{Keyword: keyword})
	if err != nil {
		log.Fatalf("could not search: %v", err)
	}

	tpl.Execute(w, map[string]interface{}{
		"Image": res.GetImageStr(), // Ensure this matches the protobuf response field
	})
}

func main() {
	http.HandleFunc("/", searchHandler)
	log.Println("Client1 started on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
