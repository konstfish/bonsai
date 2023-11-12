package main

import (
	"context"
	"encoding/json"
	"flag"
	"log"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "bonsai_exporter/io_grpc_konstfish_bonsai"
)

const (
	defaultName = "world"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
	name = flag.String("name", defaultName, "Name to greet")
)

func main() {
	flag.Parse()
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewServerClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	myJsonString := `{"some":"json"}`
	var myStoredVariable []byte
	json.Unmarshal([]byte(myJsonString), &myStoredVariable)
	var test = []byte(myJsonString)

	req := pb.MetricsRequest{Host: "test", Id: "asdf", Job: "test", Metrics: test}
	req.Labels = append(req.Labels, "Hello")
	req.Labels = append(req.Labels, "World")

	r, err := c.PushMetrics(ctx, &req)
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %n", r.GetCode())
}
