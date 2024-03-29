// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.25.0
// source: bonsai.proto

package io_grpc_konstfish_bonsai

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	BonsaiService_RegisterClient_FullMethodName = "/bonsai.BonsaiService/RegisterClient"
	BonsaiService_PushMetrics_FullMethodName    = "/bonsai.BonsaiService/PushMetrics"
)

// BonsaiServiceClient is the client API for BonsaiService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type BonsaiServiceClient interface {
	// Sends a greeting
	RegisterClient(ctx context.Context, in *RegistrationRequest, opts ...grpc.CallOption) (*RegistrationConfirmation, error)
	PushMetrics(ctx context.Context, in *MetricsRequest, opts ...grpc.CallOption) (*MetricsConfirmation, error)
}

type bonsaiServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewBonsaiServiceClient(cc grpc.ClientConnInterface) BonsaiServiceClient {
	return &bonsaiServiceClient{cc}
}

func (c *bonsaiServiceClient) RegisterClient(ctx context.Context, in *RegistrationRequest, opts ...grpc.CallOption) (*RegistrationConfirmation, error) {
	out := new(RegistrationConfirmation)
	err := c.cc.Invoke(ctx, BonsaiService_RegisterClient_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *bonsaiServiceClient) PushMetrics(ctx context.Context, in *MetricsRequest, opts ...grpc.CallOption) (*MetricsConfirmation, error) {
	out := new(MetricsConfirmation)
	err := c.cc.Invoke(ctx, BonsaiService_PushMetrics_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// BonsaiServiceServer is the server API for BonsaiService service.
// All implementations must embed UnimplementedBonsaiServiceServer
// for forward compatibility
type BonsaiServiceServer interface {
	// Sends a greeting
	RegisterClient(context.Context, *RegistrationRequest) (*RegistrationConfirmation, error)
	PushMetrics(context.Context, *MetricsRequest) (*MetricsConfirmation, error)
	mustEmbedUnimplementedBonsaiServiceServer()
}

// UnimplementedBonsaiServiceServer must be embedded to have forward compatible implementations.
type UnimplementedBonsaiServiceServer struct {
}

func (UnimplementedBonsaiServiceServer) RegisterClient(context.Context, *RegistrationRequest) (*RegistrationConfirmation, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RegisterClient not implemented")
}
func (UnimplementedBonsaiServiceServer) PushMetrics(context.Context, *MetricsRequest) (*MetricsConfirmation, error) {
	return nil, status.Errorf(codes.Unimplemented, "method PushMetrics not implemented")
}
func (UnimplementedBonsaiServiceServer) mustEmbedUnimplementedBonsaiServiceServer() {}

// UnsafeBonsaiServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to BonsaiServiceServer will
// result in compilation errors.
type UnsafeBonsaiServiceServer interface {
	mustEmbedUnimplementedBonsaiServiceServer()
}

func RegisterBonsaiServiceServer(s grpc.ServiceRegistrar, srv BonsaiServiceServer) {
	s.RegisterService(&BonsaiService_ServiceDesc, srv)
}

func _BonsaiService_RegisterClient_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RegistrationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BonsaiServiceServer).RegisterClient(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: BonsaiService_RegisterClient_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BonsaiServiceServer).RegisterClient(ctx, req.(*RegistrationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _BonsaiService_PushMetrics_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MetricsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BonsaiServiceServer).PushMetrics(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: BonsaiService_PushMetrics_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BonsaiServiceServer).PushMetrics(ctx, req.(*MetricsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// BonsaiService_ServiceDesc is the grpc.ServiceDesc for BonsaiService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var BonsaiService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "bonsai.BonsaiService",
	HandlerType: (*BonsaiServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "RegisterClient",
			Handler:    _BonsaiService_RegisterClient_Handler,
		},
		{
			MethodName: "PushMetrics",
			Handler:    _BonsaiService_PushMetrics_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "bonsai.proto",
}
