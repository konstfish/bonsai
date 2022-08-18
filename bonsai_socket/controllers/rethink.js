'use strict';

const rethinkhost = 'rethink'
//const rethinkhost = '10.0.1.108'

var r = require('rethinkdbdash')({
    servers: [
        {host: rethinkhost, port: 28015, db: "bonsai"},
    ]
});

exports.rethink = r;