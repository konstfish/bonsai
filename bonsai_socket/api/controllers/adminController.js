'use strict';

var rethink = require('../../socket/controllers/rethink')
var r = rethink.rethink

exports.getMetricAmount = function(callback){
  r.table('metrics').count().run(callback)
}

exports.purgeMetrics = function(callback){
  r.table('metrics').delete().run(callback)
}

exports.healthCheck = function(callback){
  return r.getPoolMaster()._healthy
}