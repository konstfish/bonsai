<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-chart-line" /> {{ dashboardName }}
      </h1>
    </div>

    <!--<button @click="addItem">Add an item dynamically</button>-->

    <div class="header-bar">
      <v-select class="style-chooser" :options="hosts" @option:selected="update_socket_listener"></v-select>

      <div class="header-buttons">
        <button @click="showPanelModal">Add Panel</button>
        <button @click="showDashboardModal">Save Dashboard</button>
      </div>
    </div>

    <Modal  v-model:visible="isVisible.panelModal" 
            modalClass="modalDialog"
            title="Add Panel"
            :closable="false"
            :cancelButton="{text: 'Cancel', onclick: null}"
            :okButton="{text: 'Ok', onclick: () => {addPanel()}, loading: true}"
    >
        <div>
          <label for="pname">Panel Name</label><br>
          <input type="text" id="pname" v-model="panelTemplating.name" placeholder="Dashboard Name" name="pname">
          <br>
          <label for="pmetric">Metric Point</label><br>
          <input type="text" id="pmetric" v-model="panelTemplating.metric" placeholder="Metric" name="pmetric">
          <br>
          <label for="ptype">Panel Type</label><br>
          <select id="ptype" name="ptype" v-model="panelTemplating.type">
            <option value="singlegauge">Single Gauge</option>
            <option value="multigauge">Multi Gauge</option>
            <option value="areachart">Area Chart</option>
            <option value="barchart">Bar Chart</option>
          </select>
          <br>
        </div>
    </Modal>

    <Modal  v-model:visible="isVisible.dashboardModal" 
            modalClass="modalDialog"
            title="Save Dashboard"
            :closable="false"
            :cancelButton="{text: 'Cancel', onclick: null}"
            :okButton="{text: 'Ok', onclick: () => {saveDashboard()}, loading: true}"
    >
        <div>
          <label for="dname">Dashboard Name</label><br>
          <input type="text" id="dname" v-model="dashboardName" placeholder="Dashboard Name" name="fname">
          <br>
        </div>
    </Modal>
  
  
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

              <span class="item-title"><font-awesome-icon icon="fa-solid fa-chart-line" /> {{ item.name }}</span>
              
              <BarChart v-if="item.type == 'barchart'" :metric=this.passed_data[item.i] />

              <GaugeChart v-if="item.type == 'singlegauge'" :metric=this.passed_data[item.i] />

              <AreaChart v-if="item.type == 'areachart'" :metric=this.passed_data[item.i] :points=50 />

              <MultiGagueChart v-if="item.type == 'multigauge'" :metric=this.passed_data[item.i] />

          </grid-item>

      </grid-layout>
    </div>

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

import { ref } from 'vue';
import { Modal } from 'usemodal-vue3';

export default {
  components: {
    GridLayout,
    GridItem,
    BarChart,
    GaugeChart,
    AreaChart,
    MultiGagueChart,
    Modal
  },
  data() {
    return {
      layout: [],
      colNum: 12,
      passed_data: {},
      metrics: {},
      metrics_flattened: [],
      hosts: [],
      socket: io(this.socket_io_server, {path: "/ws"}),
      isVisible: ref({dashboardModal: false, panelModal: false}),
      dashboardName: "",
      panelTemplating: {},
      panelTemplatingDefaults: {
        "barchart": {
          "metric_type": "multiple",
          "minW":6,
          "minH": 7,
          "maxH": 7,
        },
        "areachart": {
          "metric_type": "multiple",
          "minW":6, 
          "minH": 7, 
          "maxH": 7,
        },
        "singlegauge": {
          "metric_type": "single",
          "minW":4, 
          "minH": 7, 
          "maxH": 7,
        },
        "multigauge": {
          "metric_type": "multiple",
          "minW":6, 
          "minH": 9, 
          "maxH": 12
        }
      }
    }
  },
  created() {
    console.log(this.$route.params.id)
    this.clearPanelSettings()

    this.axios.post(this.api_server + "/api/dashboards/get", {id: this.$route.params.id}).then((response) => {
      console.log(response)
      this.dashboardName = response.data.return.name
      this.layout = response.data.return.layout
    })

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

      let flattened = this.flattenDict(row["metrics"])
      console.log("Flattened")
      console.log(flattened)

      this.layout.forEach((block) => {
        if(block.metric_type == "single"){
          this.passed_data[block.i] = row.metrics["CPU"][block.metric]
        }else{
          this.passed_data[block.i] = {date: row.date, val: row.metrics["CPU"][block.metric]}
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

      showDashboardModal(){
        this.isVisible.dashboardModal = true
      },

      saveDashboard(){
        console.log(this.layout)
        console.log(this.dashboardName)

        const request = {
          id: this.$route.params.id,
          name: this.dashboardName,
          layout: this.layout
        }

        /*this.axios.post(this.api_server + "/api/dashboards/add", request).then((response) => {
          console.log(response.data)
        })*/

        this.axios.post(this.api_server + "/api/dashboards/update", request, {
          headers: {"Content-Type": "application/json"}
        }).then(response => {
            console.log(response.data);
        });

        this.isVisible.dashboardModal = false
      },

      showPanelModal(){
        console.log(this.layout)
        this.isVisible.panelModal = true
      },

      addPanel(){
        let x = 0
        let y = 0

        if(this.layout.length > 0){
          console.log(this.layout[this.layout.length - 1])
          x = this.layout[this.layout.length - 1]["x"] + this.layout[this.layout.length - 1]["w"]
          y = this.layout[this.layout.length - 1]["y"] + this.layout[this.layout.length - 1]["h"]
        }

        this.layout.push({
            x: x,
            y: y, 
            w: this.panelTemplatingDefaults[this.panelTemplating.type]["minW"],
            h: this.panelTemplatingDefaults[this.panelTemplating.type]["minH"],
            minW: this.panelTemplatingDefaults[this.panelTemplating.type]["minW"],
            minH: this.panelTemplatingDefaults[this.panelTemplating.type]["minH"],
            maxH: this.panelTemplatingDefaults[this.panelTemplating.type]["maxH"],
            i: this.layout.length + 1,
            name: this.panelTemplating.name,
            type: this.panelTemplating.type,
            metric: this.panelTemplating.metric,
            metric_type: this.panelTemplatingDefaults[this.panelTemplating.type]["metric_type"],
        });

        this.isVisible.panelModal = false
        this.clearPanelSettings()
      },

      clearPanelSettings(){
        this.panelTemplating = {
          name: "",
          type: "",
          metric: ""
        }
      },

      flattenDict(ob) {
        var toReturn = {};

        for (var i in ob) {
            if (!Object.prototype.hasOwnProperty.call(ob, i)) continue;
            

            if ((typeof ob[i]) == 'object' && ob[i] !== null) {
                var flatObject = this.flattenDict(ob[i]);
                for (var x in flatObject) {
                    if (!Object.prototype.hasOwnProperty.call(flatObject, x)) continue;
                    toReturn[i + '.' + x] = flatObject[x];
                }
            } else {
                toReturn[i] = ob[i];
            }
        }
        return toReturn;
    }
  },
}
</script>

<style>
button{
  padding: 12px;
  margin-left: 12px;
  border: none;

  background: var(--background-color-secondary) !important;
  color: var(--text-color-primary) !important;
  border-radius: 4px;
}

label{
  font-size: 12px;
}

input{
  padding: 8px;
  border: none;

  background: var(--background-color-secondary) !important;
  color: var(--text-color-primary) !important;
  border-radius: 4px;
}
.header-bar{
  padding: 12px;

  display: flex;
  flex-wrap: wrap;
  flex-grow: unset;
  justify-content: space-between;
}

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
  padding: 4px;
}

.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu,
.vs__selected {
  background: var(--background-color-secondary);
  border: none;
  color: var(--text-color-primary);
  text-transform: lowercase;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: var(--text-color-primary);
}

tspan{
  color: var(--text-color-primary);
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
  opacity: 75%;
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

.modal-vue3-content {
  color: var(--text-color-primary) !important;
  background-color: var(--background-color-primary) !important;
  border-radius: var(--border-rad-primary) !important;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1) !important;
  border: none;
}

</style>