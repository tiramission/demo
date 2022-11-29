package main

import (
	"google.golang.org/grpc"
	"grpc-demo/server"
	"grpc-demo/service"
	"log"
	"net"
)

func main() {
	lis, err := net.Listen("tcp", "localhost:7777")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	service.RegisterGreeterServer(grpcServer, &server.ApiServer{})
	err = grpcServer.Serve(lis)
	if err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
