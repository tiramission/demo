package me.jaign.client

import io.grpc.ManagedChannel
import me.jaign.api.GreeterGrpc
import me.jaign.api.HelloRequest

class GreetClient(private val chanel: ManagedChannel) {
    private val stub: GreeterGrpc.GreeterBlockingStub = GreeterGrpc.newBlockingStub(chanel)

    fun sayHello(name: String) {
        val result = stub.sayHello(HelloRequest.newBuilder().setName("jiang + $name").build())
        println("Response: message: ${result.message}")
    }
}
