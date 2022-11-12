// bonsai

// rethinkdb
var rethink = require('./socket/controllers/rethink')
var r = rethink.rethink

var dbController = require('./socket/controllers/dbController')
var socketController = require('./socket/controllers/socketController')

// express server
var express = require('express');
var app = express();
var server = require('http').Server(app);
var path = require('path');
var cors = require('cors');

// Socket.io
var io = require('socket.io')(server, { path: '/ws' });
global.io = io;

// express setup
app.use(express.static('public'));
app.use(cors())

// register express endpoints
app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

var routesAdmin = require('./api/routes/adminRoutes');
app.use('/api/admin', routesAdmin);

// socket.io calls
var socket_list = {}

io.sockets.on("connection", function(socket){
    console.log("connection -", socket.id)


    // socket on handlers
    /// message
    socket.on("message", (data) => {
        const packet = JSON.parse(data);
        console.log(packet)

        // static
        if(packet.type == 'get_labels'){
            // retrieve labels
            dbController.getLabels(function(res){
                socketController.brodcastMessage("label_list", res, socket)
            })
        }
        else if(packet.type == 'get_hosts'){
            // retrieve hosts
            dbController.getHosts(function(res){
                socketController.brodcastMessage("host_list", res, socket)
            })
        }
        else if(packet.type == 'get_hostnames'){
            // retrieve hosts
            dbController.getHostnames(function(res){
                socketController.brodcastMessage("hostname_list", res, socket)
            })
        }

        // listeners
        else if(packet.type == 'update_listener')
        {
            var labels = packet.content[0];
            dbController.getMetricsByLabelListener(socket, labels);
        }
        else if(packet.type == 'update_listener_metrics_host')
        {
            var host = packet.content[0];
            dbController.getMetricsByHostListener(socket, host);
        }
        else if(packet.type == 'update_listener_host')
        {
            dbController.getHostsListener(socket);
        }
        else if(packet.type == 'udpate_listener_updates')
        {
            dbController.getMetricsListener(socket);
        }
    });

    socket.on("disconnect", (reason) => {
        console.log("disconnect -", socket.id)
        delete socket_list[socket.id]
    });
})

server.listen(9000);
console.log("✨ :9000")