import controllers

import proto
import asyncio
import grpc
import bonsai_pb2_grpc
from BonsaiServer import BonsaiServer

import logging
logger = logging.getLogger('bonsai')

# mdbc = pymongo.MongoClient('mongodb://database:27017/')
# r.db("test").table_create("authors").run())

async def serve() -> None:
    server = grpc.aio.server()
    bonsai_pb2_grpc.add_ServerServicer_to_server(BonsaiServer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())