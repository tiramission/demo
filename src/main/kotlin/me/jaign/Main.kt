package me.jaign

import io.grpc.ManagedChannelBuilder
import me.jaign.client.GreetClient
import me.jaign.server.GreetServer

fun main() {
//    val port = 5555
//    val server = GreetServer(port)
//    server.start()
    val channel = ManagedChannelBuilder.forAddress("localhost", 7777).usePlaintext().build()
    val sendRequest = GreetClient(channel)
    sendRequest.sayHello("are you ok?")
}