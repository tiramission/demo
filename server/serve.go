package server

import (
	"context"
	"grpc-demo/service"
)

type ApiServer struct {
	service.UnimplementedGreeterServer
}

func (a *ApiServer) SayHello(ctx context.Context, request *service.HelloRequest) (*service.HelloReply, error) {
	return &service.HelloReply{Message: request.Name}, nil
}

func (a *ApiServer) SayHelloNoParam(context.Context, *service.Empty) (*service.HelloReply, error) {
	return &service.HelloReply{Message: "No Param"}, nil
}
