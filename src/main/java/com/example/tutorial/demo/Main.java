package com.example.tutorial.demo;


import com.example.tutorial.Api;
import com.example.tutorial.GreeterGrpc;
import io.grpc.ManagedChannelBuilder;

public class Main {
    public static void main(String[] args) {
        var channel = ManagedChannelBuilder
                .forAddress("localhost", 7777)
                .usePlaintext()
                .build();
        var stub = GreeterGrpc.newBlockingStub(channel);
        Api.HelloReply reply = stub.sayHello(Api.HelloRequest.newBuilder().setName("Jiang From Java").build());
        System.out.println("Response: message: " + reply.getMessage());
    }
}
