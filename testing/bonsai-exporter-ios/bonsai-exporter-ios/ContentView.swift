//
//  ContentView.swift
//  bonsai-exporter-ios
//
//  Created by David Fischer on 12.11.22.
//

import CoreMotion
import SwiftUI

struct ContentView: View {
    let bs = BonsaiService()
    
    let manager = CMMotionManager()
    
    @State var target = "10.214.207.200"
    @State var interval = "1"
    
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
             
            TextField("Server:", text: $target)
                .textFieldStyle(.roundedBorder)
                .disableAutocorrection(true)
            
            TextField("Interval:", text: $interval)
                .textFieldStyle(.roundedBorder)
                .disableAutocorrection(true)
            
            Button("Register"){
                print("Register")
                Task {
                    do {
                        bs.host = self.target
                        try await bs.register()
                    } catch {
                        print(error)
                    }
                }
                
                manager.startDeviceMotionUpdates()
                
                Timer.scheduledTimer(withTimeInterval: Double(self.interval) ?? 1, repeats: true) { _ in
                    if let data = self.manager.deviceMotion {
                        let x = data.attitude.roll
                        let y = data.attitude.pitch
                        let z = data.attitude.yaw
                        
                        Task {
                        do {
                                try await bs.push(x: x, y: y, z: z)
                            } catch {
                                print(error)
                            }
                        }
                    }
                }
                
            }
            
            Button("Push"){
                print("Push")
                Task {
                do {
                        // try await bs.push()
                        print("asdf")
                    } catch {
                        print(error)
                    }
                }
            }
        }
        .padding()
    }
    
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
