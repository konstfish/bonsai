package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "bonsai_exporter/io_grpc_konstfish_bonsai"

	"github.com/mackerelio/go-osstat/cpu"
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
	c := pb.NewBonsaiServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second*5)
	defer cancel()

	req := pb.RegistrationRequest{
		Job:      "test",
		Host:     "localhost",
		Interval: 1,
	}

	req.Labels = append(req.Labels, "Hello")
	req.Labels = append(req.Labels, "World")

	req.Scrapers = append(req.Scrapers, "test")

	r, err := c.RegisterClient(ctx, &req)
	if err != nil {
		log.Fatalf("could not register: %v", err)
	}
	ekey := r.ExporterKey

	for true {
		loopCtx, loopCancel := context.WithTimeout(context.Background(), time.Second*5)

		mreq := pb.MetricsRequest{
			ExporterKey: ekey,
		}

		stats, _ := cpu.Get()

		// create json from stats variable
		stats_json := fmt.Sprintf(`{"user":%v,"system":%v,"idle":%v,"nice":%v}`,
			stats.User,
			stats.System,
			stats.Idle,
			stats.Nice)

		statsJSON := []byte(stats_json)

		mreq.Metrics = append(mreq.Metrics, statsJSON...)

		fmt.Printf("CPU: %v\n", mreq)

		_, err := c.PushMetrics(loopCtx, &mreq)
		if err != nil {
			log.Fatalf("could not push metrics: %v", err)
		}

		loopCancel()

		time.Sleep(1 * time.Second)
	}
}
