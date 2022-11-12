'use strict';

var socketController = require('./socketController')

var rethink = require('../../socket/controllers/rethink')
var r = rethink.rethink

function concatList(list){
    // convert concatenated list to set to remove duplicates
    var uSet = new Set([].concat.apply([], list));
    var result = [...uSet];

    return result
}

// get labels, return to callback function
exports.getLabels = function(callback){
    r.table('hosts').getField('labels').run(function(err, cursor){
        if (err) throw err;

        var res = concatList(cursor)
        callback(res)
    });
}

// get hostnames, return to callback function
exports.getHostnames = function(callback){
    r.table('hosts').getField('host').run(function(err, cursor){
        if (err) throw err;

        callback(cursor)
    });
}

// get hosts, return to callback function
exports.getHosts = function(callback){
    r.table('hosts').run(function(err, cursor){
        if (err) throw err;

        callback(cursor)
    });
}

// get hostnames by label, return to callback function
exports.getHostsByLabel = function(labels, callback){
    r.table('hosts')
        .filter(r.row('labels').contains(labels))
        .getField('id')
        .run(function(err, cursor){
            if (err) throw err;

            callback(cursor)
        });
}

// get hostnames by label, return to callback function
exports.getHostsById = function(host, callback){
    r.table('hosts')
        .filter({'host': host})
        .getField('id')
        .run(function(err, cursor){
            if (err) throw err;

            callback(cursor[0])
        });
}

// listener > hosts
exports.getHostsListener = function(socket){
    r.table('hosts')
        .changes({"includeInitial": true})
        .run(function(err, cursor){
            if (err) throw err;
            
            module.exports.pushMetricChanges(cursor, "hosts", socket)
    });
}

// listener > all metrics
exports.getMetricsListener = function(socket){
    r.table('metrics')
    .changes({"includeInitial": true})
    .run(function(err, cursor) {
        if (err) throw err;

        module.exports.pushMetricUpdate(cursor, socket);
    });
}

// listener > metrics by labels
exports.getMetricsByLabelListener = function(socket, labels){
    module.exports.getHostsByLabel(labels, function(labels){
        console.log(labels)

        r.table('metrics')
            .getAll(...labels)
            .changes({"includeInitial": true})
            .run(function(err, cursor) {
                if (err) throw err;

                module.exports.pushMetricChanges(cursor, "metrics", socket);
            });
    });
}

// listener > metrics by hostname
exports.getMetricsByHostListener = function(socket, host){
    console.log("entering")
    module.exports.getHostsById(host, function(host_id){
        console.log(host_id)
        r.table('metrics')
            .filter({'id': host_id})
            .changes({"includeInitial": true})
            .run(function(err, cursor){
                if (err) throw err;
                
                module.exports.pushMetricChanges(cursor, "metrics", socket)
            });
    });
}

exports.pushMetricChanges = function(cursor, type, socket){
    cursor.each(function(err, row) {
        if (err) console.log(err);

        if(socketController.checkIfSocket(socket)){
            if(row.new_val != null){
                console.log((type + "_general_update"), " - ", socket.id)
                socketController.brodcastMessage((type + "_general_update"), row.new_val, socket)
            } else {
                console.log((type + "_deletion_update"), " - ", socket.id)
                socketController.brodcastMessage((type + "_deletion_update"), row.old_val, socket)
            }
        }else{
            console.log("closing ----------------------------")
            cursor.close()
        }
    });
}

exports.pushMetricUpdate = function(cursor, socket){
    cursor.each(function(err, row) {
        if (err) console.log(err);

        if(socketController.checkIfSocket(socket)){
            console.log(("metric_update"), " - ", socket.id)
            socketController.brodcastMessage("metric_update", row.new_val.id, socket)
        }else{
            console.log("closing ----------------------------")
            cursor.close()
        }
    });
}