'use strict';

var rethink = require('../../socket/controllers/rethink')
var r = rethink.rethink

// returns list of dashboards
exports.getDashboards = function(callback){
  r.table('dashboards').pluck('id', 'name').run(callback)
}

// returns content of specific dashboard by id
exports.getDashboard = function(id, callback){
  r.table('dashboards').get(id).run(callback)
}

// add dashboard using provided json
exports.addDashboard = function(djson, callback){
  r.table('dashboards').insert(djson).run(callback)
}

// update dashboard using proviced json
exports.updateDashboard = function(djson, callback){
  r.table('dashboards').insert(djson, {conflict: "update"}).run(callback)
}

// delete dashboard by id
exports.removeDashboard = function(id, callback){
  r.table('dashboards').get(id).delete().run(callback)
}