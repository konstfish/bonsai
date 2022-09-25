'use strict';

const rethinkhost = 'rethink'
//const rethinkhost = '127.0.0.1'

var r = require('rethinkdbdash')({
    servers: [
        {host: rethinkhost, port: 28015, db: "bonsai"},
    ]
});

exports.rethink = r;