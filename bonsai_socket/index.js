var express = require('express');
var app = express();
var server = require('http').Server(app);
var path = require('path');
var cors = require('cors')

// Socket.io
var io = require('socket.io')(server, {
  path: '/ws'
});

// Rethinkdb
var r = require('rethinkdb');

app.use(express.static('public'));
app.use(cors())

app.get('*', function(req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});

const rethinkhost = 'rethink'
//const rethinkhost = '10.0.1.108'

rethink = r.connect({host: rethinkhost, 
                    port: 28015, 
                    db: "bonsai"})


rethink.then(function(connection) {
    r.table('metrics').changes().run(connection, function(err, cursor) {
        if (err) throw err;
        cursor.each(function(err, row) {
            if (err) throw err;

            console.log(Array.from(io.sockets.sockets.keys()))
            
            if(Array.from(io.sockets.sockets.keys()).length > 0){
                if(row.new_val != null){
                    console.log("general_update")
                    io.emit("general_update", row.new_val)
                } else {
                    console.log("deletion_update")
                    io.emit("deletion_update", row.old_val)
                }
            }
        });
    });


    io.sockets.on("connection", function(socket){
        console.log("connection")
        console.log(socket.id)
        
        r.table('metrics').run(connection, function(err, cursor) {
            if (err) throw err;
            cursor.each(function(err, row) {
                if (err) throw err;
                // console.log(JSON.stringify(row, null, 2));
                socket.emit("general_update", row)
            });
        });

        socket.on("disconnect", (reason) => {
            console.log("disconnect")
        });
    })

})
.error(function(error) {
    console.log('Error connecting to RethinkDB!');
    console.log(error);
});

server.listen(9000);
console.log("✨ :9000")