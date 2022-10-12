<template>
  <div class="home">
    <h1>Dashboard</h1>

    <button @click="addItem">Add an item dynamically</button>

    <div class="grid-container">
      <grid-layout
              v-model:layout="layout"
              :col-num="12"
              :row-height="30"
              :is-draggable="true"
              :is-resizable="true"
              :is-mirrored="false"
              :vertical-compact="true"
              :margin="[10, 10, 10, 10]"
              :use-css-transforms="true">

          <grid-item v-for="item in layout"
                    :x="item.x"
                    :y="item.y"
                    :w="item.w"
                    :minW="item.minW"
                    :minH="item.minH"
                    :h="item.h"
                    :i="item.i"
                    :key="item.i">
              {{ item.i }}
              
              <BarChart v-if="item.i == '1'" :metric=this.passed_data[item.i] />

              <GaugeChart v-if="item.i == '2'" :metric=this.passed_data[item.i] />

              <AreaChart v-if="item.i == '3'" :metric=this.passed_data[item.i] :points=50 />

              <MultiGagueChart v-if="item.i == '4'" :metric=this.passed_data[item.i] />

          </grid-item>

      </grid-layout>

    </div>

  </div>
</template>

<script>
import io from 'socket.io-client';

import {GridLayout, GridItem} from "vue3-grid-layout";
// https://apexcharts.com/vue-chart-demos/radialbar-charts/stroked-gauge/
import BarChart from '../components/BarChart.vue'
import GaugeChart from '../components/GaugeChart.vue'
import AreaChart from '../components/AreaChart.vue'
import MultiGagueChart from '../components/MultiGagueChart.vue'

export default {
  components: {
    GridLayout,
    GridItem,
    BarChart,
    GaugeChart,
    AreaChart,
    MultiGagueChart,
  },
  data() {
    return {
      layout: [
                {"x":0,"y":7,"w":6,"h":9,"i":"1", "minW":6, "minH": 7},
                {"x":0,"y":0,"w":4,"h":7,"i":"2", "minW":4, "minH": 7},
                {"x":4,"y":0,"w":8,"h":7,"i":"3", "minW":6, "minH": 7},
                {"x":6,"y":7,"w":6,"h":9,"i":"4", "minW":6, "minH": 9},
            ],

      passed_data: {"2": 100, "3": {date: Date.now(), val: 100}},
      metrics: {},
      labels: {},
      socket: io(this.socket_io_server, {path: "/ws"}),
    }
  },
  created() {
    this.socket.open()

    this.socket.on("label_list", (row) => {
      this.labels = row
    });

    this.socket.on("general_update", (row) => {
      this.metrics = row
      this.passed_data["1"] = row.metrics.CPU.individual_cores
      this.passed_data["2"] = row.metrics.CPU.percent
      this.passed_data["3"] = {date: row.date, val: row.metrics.CPU.percent}
      this.passed_data["4"] = row.metrics.CPU.individual_cores
    });

    this.socket.send(JSON.stringify({
      type: "update_listener",
      content: ["asd"]
    }));

    setTimeout(() => {
      window.dispatchEvent(new Event('resize'))
    },100)
  },

  unmounted() {
    this.socket.close()
    //this.socket = null
  },

  methods: {
    addItem: function () {
            // Add a new item. It must have a unique key!
            this.layout.push({
                x: this.layout[this.layout.length - 1]["x"] + this.layout[this.layout.length - 1]["w"],
                y: 0,
                w: 2,
                h: 2,
                i: this.layout.length + 1,
            });
            // Increment the counter to ensure key is always unique.
            console.log(this.layout)
        },
  },
}
</script>

<style scoped>
.grid-container{
  height: 100%;
  width: 100%;
}

.vue-grid-item {
    background: white;
    color: black;
    transition-duration: 100ms;
    z-index: 2;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    -o-user-select: none;
    user-select: none;
    border-radius: 8px;
}

.vue-grid-layout{
    background-size: calc(calc(100% - 5px) / 12) 40px;
    background-image: linear-gradient(
            to right,
            lightgrey 1px,
            transparent 1px
    ),
    linear-gradient(to bottom, lightgrey 1px, transparent 1px);
    height: calc(100% - 5px);
    width: calc(100% - 5px);
    position: absolute;
    background-repeat: repeat;
    width: 80%;
}


</style>