var express = require('express');
var app = express();
var server = require('http').Server(app);
var path = require('path');

// Socket.io
var io = require('socket.io')(server);

// Rethinkdb
var r = require('rethinkdb');

app.use(express.static('public'));

app.get('*', function(req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

r.connect({host: 'localhost', port: 28015, db: "bonsai"})
    .then(function(connection) {
        r.table('metrics').changes().run(connection, function(err, cursor) {
            if (err) throw err;
            cursor.each(function(err, row) {
                if (err) throw err;
                // console.log(JSON.stringify(row, null, 2));
                io.emit("test", row.new_val)
            });
        });

        server.listen(9000);

        io.sockets.on("connection", function(socket){
            console.log("connection")
            
            r.table('metrics').run(connection, function(err, cursor) {
                if (err) throw err;
                cursor.each(function(err, row) {
                    if (err) throw err;
                    // console.log(JSON.stringify(row, null, 2));
                    socket.emit("test", row)
                });
            });
        })
    })
    .error(function(error) {
        console.log('Error connecting to RethinkDB!');
        console.log(error);
    });
