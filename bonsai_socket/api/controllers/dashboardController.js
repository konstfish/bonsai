'use strict';

var rethink = require('../../socket/controllers/rethink')
var r = rethink.rethink

exports.getDashboards = function(callback){
  r.table('dashboards').pluck('id', 'name').run(callback)
}

exports.getDashboard = function(id, callback){
  r.table('dashboards').get(id).run(callback)
}

exports.addDashboard = function(djson, callback){
  r.table('dashboards').insert(djson).run(callback)
}

exports.updateDashboard = function(djson, callback){
  r.table('dashboards').insert(djson, {conflict: "update"}).run(callback)
}