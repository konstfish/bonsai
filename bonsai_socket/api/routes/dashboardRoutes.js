'use strict';
var controller = require('../controllers/dashboardController');
var express = require('express');
var router = express.Router();

router.post('/add', (req, res) => {
  try{
    console.log(req.body)

    controller.addDashboard({name: "Untitled Dashboard", layout: []}, (err, task) => {
      if(err) throw err;
      console.log(task);
      res.status(200).json({"status": 200, "task": task});
    })
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

router.post('/update', (req, res) => {
  try{
    const djson = {
      id: req.body.id,
      name: req.body.name,
      layout: req.body.layout
    }

    controller.updateDashboard(djson, (err, task) => {
      if(err) throw err;
      res.json({"status": 200, "task": task});
    })
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

router.post('/get', (req, res) => {
  try{
    const id = req.body.id;
    console.log(req.body)
    controller.getDashboard(id, (err, task) => {
      if(err) throw err;
      res.status(200).json({"status": 200, "return": task});
    })
    //}else{
    //  res.status(400).json({success: false, msg: 'S4YERR_MALFORMED'})
    //}
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

router.get('/list', (req, res) => {
  try{
    //const team_id = req.body.team_id;
    controller.getDashboards((err, task) => {
      if(err) throw err;
      res.status(200).json({"status": 200, "return": task});
    })
    //}else{
    //  res.status(400).json({success: false, msg: 'S4YERR_MALFORMED'})
    //}
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

router.post('/remove', (req, res) => {
  try{
    const id = req.body.id;
    console.log(req.body)
    controller.removeDashboard(id, (err, task) => {
      if(err) throw err;
      res.status(200).json({"status": 200, "return": task});
    })
    //}else{
    //  res.status(400).json({success: false, msg: 'S4YERR_MALFORMED'})
    //}
  }catch(e){
    console.log(e)
    res.status(400).json({success: false, msg: 'GENERAL'})
  }
})

module.exports = router;
