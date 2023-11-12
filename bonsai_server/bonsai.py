import signal
import time
import controllers

import sys, getopt

import proto
import asyncio
import grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

import bonsai_pb2
import bonsai_pb2_grpc
from BonsaiServer import BonsaiServer

import time

import logging
logger = logging.getLogger('bonsai')

import sched

"""
class gRPCSigHandler():
    def __init__(self, server):
        self.server = server
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGINT, self.exit_gracefully)
    
    def exit_gracefully(self, *args):
        print("asdf")
        asyncio.run(self.close_server())

    async def close_server(self):
        await self.server.stop()
"""

keyfile = 'certs/cert.key'
certfile = 'certs/cert.pem'

private_key = open(keyfile, 'rb').read()
certificate_chain = open(certfile, 'rb').read()

credentials = grpc.ssl_server_credentials(
    [(private_key, certificate_chain)]
)

_cleanup_coroutines = []

async def serve(server_key) -> None:
    # create gRPC server
    server = grpc.aio.server()

    # add BonsaiService to gRPC server
    bonsai_pb2_grpc.add_BonsaiServiceServicer_to_server(BonsaiServer(server_key), server)

    # add HealthServicer to gRPC server
    health_servicer = health.HealthServicer()
    services = tuple(
        service.full_name
        for service in bonsai_pb2.DESCRIPTOR.services_by_name.values()) + (
            reflection.SERVICE_NAME, health.SERVICE_NAME)

    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    for service in services:
        health_servicer.set(service, health_pb2.HealthCheckResponse.SERVING)
    reflection.enable_server_reflection(services, server)

    # define listen address
    listen_addr = '[::]:50051'
    listen_addr_tls = '[::]:50052'
    
    # add plain port
    server.add_insecure_port(listen_addr)
    logger.info("Starting server on %s", listen_addr)

    # add tls port
    server.add_secure_port(listen_addr_tls, credentials)
    logger.info("Starting server (tls) on %s", listen_addr_tls)

    # start server
    await server.start()

    async def server_graceful_shutdown():
        logger.info("Starting graceful shutdown...")
        await server.stop(3)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()

if __name__ == '__main__':
    #asyncio.run(serve())

    # read system arguments
    server_key = None
    opts, args = getopt.getopt(sys.argv[1:],"hc:",["help","config="])
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print ('bonsai.py --config <key>')
            sys.exit()
        elif opt in ("-c", "--config"):
            server_key = arg

    # create loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve(server_key))
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()