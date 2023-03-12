'use strict';
var controller = require('../controllers/adminController');
var express = require('express');
const e = require('express');
var router = express.Router();

// returns amount of metrics in DB
router.get('/amount', (req, res) => {
  try{
    controller.getMetricAmount((err, task) => {
      if(err) throw err;
      res.json({"status": 200, "amount": task});
    })
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

// purge route, that removes metrics from DB
router.get('/purge', (req, res) => {
  try{
    controller.purgeMetrics((err, task) => {
      if(err) throw err;
      res.json({"status": 200, "return": task});
    })
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

// health check route
router.get('/health', (req, res) => {
   if(controller.healthCheck()){
    res.json({"status": 200})
    return
   }
   res.status(400).json({"status": 400})
})

// export router with created functions
module.exports = router;
