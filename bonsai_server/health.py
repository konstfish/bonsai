import grpc
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

request = health_pb2.HealthCheckRequest(service="bonsai.BonsaiService")

with grpc.insecure_channel("localhost:50051") as channel:
    stub = health_pb2_grpc.HealthStub(channel)
    response = stub.Check(request)
    #print(response)
    #print(response.status)
    if(response.status == 1):
        exit(0)

exit(1)