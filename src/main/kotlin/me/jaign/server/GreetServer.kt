package me.jaign.server

import io.grpc.Server
import io.grpc.ServerBuilder

class GreetServer(private val port: Int) {

    private val server: Server = ServerBuilder
        .forPort(port)
        .addService(ServerImpl())
        .build()

    fun start() {
        server.start()
        println("Server staring with port: $port")
        println("Listening")
        Runtime.getRuntime().addShutdownHook(Thread {
            println("*** shutting down grpc server since jvm is shutting down")
            this@GreetServer.stop()
        })
        this@GreetServer.blockUntilShutdown()
    }

    private fun blockUntilShutdown() {
        server.awaitTermination()
    }

    private fun stop(): Server = server.shutdown()
}