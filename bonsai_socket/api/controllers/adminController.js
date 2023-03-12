'use strict';

var rethink = require('../../socket/controllers/rethink')
var r = rethink.rethink

// get amount of metrics contained in DB
exports.getMetricAmount = function(callback){
  r.table('metrics').count().run(callback)
}

// purge metrics within DB
exports.purgeMetrics = function(callback){
  r.table('metrics').delete().run(callback)
}

// check if connection pool is healthy
exports.healthCheck = function(callback){
  return r.getPoolMaster()._healthy
}