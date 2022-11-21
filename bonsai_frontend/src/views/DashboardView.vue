<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-chart-line" /> Dashboard
      </h1>
    </div>

    <!--<button @click="addItem">Add an item dynamically</button>-->

    <v-select class="style-chooser" :options="hosts" @option:selected="update_socket_listener"></v-select>
  
    <br>
  
    <div class="grid-container">
      <grid-layout
              v-model:layout="layout"
              :col-num="12"
              :row-height="32"
              :is-draggable="true"
              :is-resizable="true"
              :is-mirrored="false"
              :vertical-compact="true"
              :margin="[10, 10]"
              :use-css-transforms="true">

          <grid-item v-for="item in layout"
                    :x="item.x"
                    :y="item.y"
                    :w="item.w"
                    :minW="item.minW"
                    :minH="item.minH"
                    :maxH="item.maxH"
                    :h="item.h"
                    :i="item.i"
                    :key="item.i">

              <span class="item-tile"><font-awesome-icon icon="fa-solid fa-chart-line" /> {{ item.i }}</span>
              
              <BarChart v-if="item.i == '1'" :metric=this.passed_data[item.i] />

              <GaugeChart v-if="item.i == '2'" :metric=this.passed_data[item.i] />

              <AreaChart v-if="item.i == '3'" :metric=this.passed_data[item.i] :points=50 />

              <MultiGagueChart v-if="item.i == '4'" :metric=this.passed_data[item.i] />

          </grid-item>

      </grid-layout>
    </div>

    <br><br><br><br><br><br><br>

  </div>
</template>

<script>
import io from 'socket.io-client';

// grid layout
import {GridLayout, GridItem} from "vue3-grid-layout";
import 'vue-select/dist/vue-select.css';

// https://apexcharts.com/vue-chart-demos/radialbar-charts/stroked-gauge/
// charts
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
                {"x":0,"y":7,"w":6,"h":7,"i":"1", "minW":6, "minH": 7, "maxH": 7, "metric_type": "single", "metric": "individual_cores"},
                {"x":0,"y":0,"w":4,"h":7,"i":"2", "minW":4, "minH": 7, "maxH": 7, "metric_type": "single", "metric": "percent"},
                {"x":4,"y":0,"w":8,"h":7,"i":"3", "minW":6, "minH": 7, "maxH": 7, "metric_type": "multiple", "metric": "percent"},
                {"x":6,"y":7,"w":6,"h":10,"i":"4", "minW":6, "minH": 9, "maxH": 12, "metric_type": "single", "metric": "individual_cores"},
                {"x":0,"y":15,"w":6,"h":10,"i":"4", "minW":6, "minH": 9, "maxH": 12, "metric_type": "single", "metric": "individual_cores"},
            ],

      passed_data: {},
      metrics: {},
      hosts: [],
      socket: io(this.socket_io_server, {path: "/ws"}),
    }
  },
  created() {
    this.socket.open()

    this.socket.send(JSON.stringify({
      type: "get_hostnames",
      content: []
    }));

    this.socket.on("hostname_list", (row) => {
      this.hosts = row
    });

    this.socket.on("metrics_general_update", (row) => {
      console.log(row)
      this.metrics = row

      this.layout.forEach((block) => {
        if(block.metric_type == "single"){
          this.passed_data[block.i] = row.metrics.CPU[block.metric]
        }else{
          this.passed_data[block.i] = {date: row.date, val: row.metrics.CPU[block.metric]}
        }
      });
      /*
      this.passed_data["1"] = row.metrics.CPU.individual_cores
      this.passed_data["2"] = row.metrics.CPU.percent
      this.passed_data["3"] = {date: row.date, val: row.metrics.CPU.percent}
      this.passed_data["4"] = row.metrics.CPU.individual_cores*/
    });

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

      update_socket_listener(event){
        this.socket.close()
        this.socket.open()
        // loop over dashboard items 
        this.passed_data = {}
        this.socket.send(JSON.stringify({
          type: "update_listener_metrics_host",
          content: [event]
        }));
        this.metrics = {}
      },
  },
}
</script>

<style scoped>
.home{
  height: auto;
}

.grid-container{
  width: 100%;
}

.style-chooser{
  width: 250px;
  background: var(--background-color-secondary) !important;
  color: var(--text-color-primary) !important;
  border-radius: 4px;
}

.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {
  background: var(--background-color-secondary);
  border: none;
  color: var(--text-color-primary);
  text-transform: lowercase;
  font-variant: small-caps;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: var(--text-color-primary);
}


.vue-grid-item {
  background: var(--background-color-secondary);
  color: var(--text-color-primary);
  transition-duration: 100ms;
  z-index: 2;
  user-select: none;

  padding: 8px;

  border-radius: var(--border-rad-primary);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
}

.vue-grid-item.vue-grid-placeholder{
  background: var(--accent-color) !important;
  border-radius: var(--border-rad-primary);
}

/*
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
}*/
</style>