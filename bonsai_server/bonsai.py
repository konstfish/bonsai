import signal
import time
import controllers

import proto
import asyncio
import grpc
import bonsai_pb2_grpc
from BonsaiServer import BonsaiServer

import helper
from BonsaiHelper import BonsaiHelper

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

async def serve() -> None:
    server = grpc.aio.server()
    bonsai_pb2_grpc.add_BonsaiServiceServicer_to_server(BonsaiServer(), server)
    listen_addr = '[::]:50051'
    listen_addr_tls = '[::]:50052'
    
    server.add_insecure_port(listen_addr)
    logger.info("Starting server on %s", listen_addr)

    server.add_secure_port(listen_addr_tls, credentials)
    logger.info("Starting server (tls) on %s", listen_addr_tls)

    await server.start()

    async def server_graceful_shutdown():
        logger.info("Starting graceful shutdown...")
        await server.stop(3)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()

if __name__ == '__main__':
    #asyncio.run(serve())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()