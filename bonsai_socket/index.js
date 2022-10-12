// bonsai

// rethinkdb
var rethink = require('./socket/controllers/rethink')
var r = rethink.rethink

var dbController = require('./socket/controllers/dbController')

// etc

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

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

var routesAdmin = require('./api/routes/adminRoutes');
app.use('/api/admin', routesAdmin);

// socket.io calls
var socket_list = {}
var socket_filter = {}

//r.table('metrics').row({'labels.type': ['test', 'asdf']}).run(function(err, cursor){
//    console.log(cursor)
//})


io.sockets.on("connection", function(socket){
    console.log("connection -", socket.id)

    // retrieve labels
    r.table('metrics').getField('labels').run(function(err, cursor){
        // convert concatenated list to set to remove duplicates
        var uSet = new Set([].concat.apply([], cursor));
        var result = [...uSet];

        // emit result as label_list
        global.io.to(socket.id).emit("label_list", result)
    });

    socket.on("message", (data) => {
        const packet = JSON.parse(data);

        //socket_list[socket.id] = r.table('metrics').changes({"includeInitial": true}).run(
        //    function(err, cursor) {
        //       dbController.new_row(err, cursor, socket)
        //    }
        //);

        console.log(packet)

        if(packet.type == 'update_listener')
        {
            console.log("closing")
            delete socket_list[socket.id]

            console.log("opening")
            console.log(packet.content[0])
            socket_list[socket.id] = r.table('metrics')
                                                .filter(r.row('labels').contains(packet.content[0]))
                                                .changes({"includeInitial": true})
                                                .run(
                                                    function(err, cursor) {
                                                    dbController.new_row(err, cursor, socket)
                                                    }
                                                );
        }
        else if(packet.type == 'remove_listener')
        {
            console.log("asdfs")
            delete socket_list[socket.id]
        }
    });

    socket.on("disconnect", (reason) => {
        console.log("disconnect -", socket.id)
        delete socket_list[socket.id]
    });
})

server.listen(9000);
console.log("✨ :9000")