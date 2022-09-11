// bonsai

// rethinkdb
var rethink = require('./socket/controllers/rethink')
var r = rethink.rethink

var dbController = require('./socket/controllers/dbController')

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

io.sockets.on("connection", function(socket){
    console.log("connection -", socket.id)

    socket_list[socket.id] = r.table('metrics').changes({"includeInitial": true}).run(
        function(err, cursor) {
            dbController.new_row(err, cursor, socket)
        }
    );

    socket.on("disconnect", (reason) => {
        console.log("disconnect -", socket.id)
        delete socket_list[socket.id]
    });
})

server.listen(9000);
console.log("✨ :9000")