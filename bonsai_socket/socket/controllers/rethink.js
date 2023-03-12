'use strict';

// check what rethinkdb should be used
var rethinkhost = '127.0.0.1'
if(process.env.IN_DOCKER_CONTAINER == 1){
    var rethinkhost = 'rethink'
}

// create connection pool
var r = require('rethinkdbdash')({
    servers: [
        {host: rethinkhost, port: 28015, db: "bonsai"},
    ]
});

exports.rethink = r;