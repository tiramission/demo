package me.jaign.server

import io.grpc.stub.StreamObserver
import me.jaign.api.Empty
import me.jaign.api.GreeterGrpc.GreeterImplBase
import me.jaign.api.HelloReply
import me.jaign.api.HelloRequest


class ServerImpl : GreeterImplBase() {
    override fun sayHello(request: HelloRequest?, responseObserver: StreamObserver<HelloReply>?) {
        responseObserver?.onNext(
            HelloReply
                .newBuilder()
                .setMessage("Hello by Kotlin, from ${request?.name}")
                .build()
        )
        responseObserver?.onCompleted()
    }

    override fun sayHelloNoParam(request: Empty?, responseObserver: StreamObserver<HelloReply>?) {
        responseObserver?.onNext(
            HelloReply
                .newBuilder()
                .setMessage("Hello by Kotlin, from No Param")
                .build()
        )
        responseObserver?.onCompleted()
    }
}