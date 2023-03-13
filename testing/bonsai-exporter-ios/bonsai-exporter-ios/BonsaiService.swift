//
//  HelloWorld.swift
//  bonsai-exporter-ios
//
//  Created by David Fischer on 12.11.22.
//

import Foundation
import GRPC
import NIOCore
import NIOPosix
import SwiftyJSON

class BonsaiService {
    var port: Int = 50051
    var host: String = "10.214.207.200"
    var name: String?
    var regkey: String = ""
    
    func register() async throws {
        let group = MultiThreadedEventLoopGroup(numberOfThreads: 1)
                defer {
            try! group.syncShutdownGracefully()
        }
        
        let channel = try GRPCChannelPool.with(
            target: .host(self.host, port: self.port),
            transportSecurity: .plaintext,
            eventLoopGroup: group
        )
        
        // Close the connection when we're done with it.
        defer {
            try! channel.close().wait()
        }
        
        // Provide the connection to the generated client.
        let bonsaiServ = Bonsai_BonsaiServiceAsyncClient(channel: channel)
        
        // Form the request with the name, if one was provided.
        let request = Bonsai_RegistrationRequest.with {
            $0.host = "iPhone"
            $0.job = "Gyro"
            $0.interval = 1
            $0.labels = ["swift", "asdf"]
            $0.scrapers = ["DEV", "GYRO"]
        }
        
        do {
            let res = try await bonsaiServ.registerClient(request)
            print("Token recieved: \(res.exporterKey)")
            self.regkey = res.exporterKey
        } catch {
            print("Greeter failed: \(error)")
        }
    }
    
    func push(x: Double, y: Double, z: Double) async throws{
        let group = MultiThreadedEventLoopGroup(numberOfThreads: 1)
                defer {
            try! group.syncShutdownGracefully()
        }
        
        let channel = try GRPCChannelPool.with(
            target: .host(self.host, port: self.port),
            transportSecurity: .plaintext,
            eventLoopGroup: group
        )
        
        // Close the connection when we're done with it.
        defer {
            try! channel.close().wait()
        }
        
        // Provide the connection to the generated client.
        let bonsaiServ = Bonsai_BonsaiServiceAsyncClient(channel: channel)
    
        let jsonb: [String: Any] = [
            "ACCEL": [
                "x": x,
                "y": y,
                "z": z
            ],
        ]
        
        let json = JSON(jsonb)
        let jsonp = try json.rawData()

        
        let request = Bonsai_MetricsRequest.with {
            $0.exporterKey = self.regkey
            $0.metrics = jsonp
        }
        
        do {
            let res = try await bonsaiServ.pushMetrics(request)
            print("Code: \(res.code)")
        } catch {
            print("Greeter failed: \(error)")
        }
    }
}
