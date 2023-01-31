'use strict';
var controller = require('../controllers/adminController');
var express = require('express');
const e = require('express');
var router = express.Router();

router.get('/amount', (req, res) => {
  try{
    //const team_id = req.body.team_id;
    controller.getMetricAmount((err, task) => {
      if(err) throw err;
      res.json({"status": 200, "amount": task});
    })
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

router.get('/purge', (req, res) => {
  try{
    //const team_id = req.body.team_id;
    controller.purgeMetrics((err, task) => {
      if(err) throw err;
      res.json({"status": 200, "return": task});
    })
    //}else{
    //  res.status(400).json({success: false, msg: 'S4YERR_MALFORMED'})
    //}
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

router.get('/health', (req, res) => {
   if(controller.healthCheck()){
    res.json({"status": 200})
    return
   }
   res.status(400).json({"status": 400})
})

module.exports = router;
