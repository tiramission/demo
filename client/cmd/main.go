package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"grpc-demo/service"
	"log"
)

var ctx = context.Background()

func main() {
	conn, err := grpc.Dial("localhost:7777", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("failed to dial: %v", err)
	}
	defer func(conn *grpc.ClientConn) {
		_ = conn.Close()
	}(conn)

	cli := service.NewGreeterClient(conn)
	reply, err := cli.SayHelloNoParam(ctx, &service.Empty{})
	fmt.Printf("reply: %+v\nerr: %+v\n", reply, err)

}
