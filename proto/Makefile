golang:
 	protoc --go_out=./go/ --go_opt=paths=source_relative --go-grpc_out=./go/ --go-grpc_opt=paths=source_relative bonsai.proto

python:
	/usr/bin/python3 -m grpc_tools.protoc -I. --python_out=./py/ --grpc_python_out=./py/ bonsai.proto
