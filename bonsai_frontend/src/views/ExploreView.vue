<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-compass-drafting" /> Explore
      </h1>
    </div>

    <div class="header-bar">
      <v-select class="style-chooser" :options="hosts" @option:selected="update_socket_listener"></v-select>

      <div class="header-buttons">
        
      </div>
    </div>
    
    <json-viewer  :value="metrics"
                  :expand-depth=3
                  :copyable="true"
                  theme="nordjson"
    ></json-viewer>


  </div>
</template>

<script>
/*import TimeSince from '@/components/TimeSince';*/
import io from 'socket.io-client';
import 'vue-select/dist/vue-select.css';

export default {
    components: {
      /*TimeSince*/
    },
    data() {
        return {
            hosts: [],
            metrics: {},
            //socket: io('', {path: "/ws"}),
            socket: io(this.socket_io_server, {path: "/ws"}),
        }
    },
    created() {
      //this.socket = io(this.socket_io_server, {path: "/ws"})
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
    });
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

      remove_socket_listener(event){
        console.log(event)
        this.socket.close()
        this.socket.open()
        this.metrics = {}

        this.socket.send(JSON.stringify({
          type: "remove_listener",
          content: [event]
        }));
      },
    },
}
</script>

<style>
.jv-container{
  margin-left: 12px;
  padding: 0px !important;
}

.nordjson {
  background: var(--background-color-primary);
  color: var(--text-color-primary);
  white-space: nowrap;
  font-size: 14px;
  font-family: Consolas, Menlo, Courier, monospace;
}
.nordjson .jv-ellipsis {
  background-color: var(--background-color-primary);
  color: var(--text-color-secondary);
  display: inline-block;
  line-height: 0.9;
  font-size: 0.9em;
  padding: 0px 4px 2px 4px;
  border-radius: 3px;
  vertical-align: 2px;
  cursor: pointer;
  user-select: none;
}
.nordjson .jv-button {
  color: #49b3ff;
}
.nordjson .jv-key {
  color: var(--text-color-primary);
}
.nordjson .jv-item.jv-array {
  color: var(--text-color-secondary);
}
.nordjson .jv-item.jv-boolean {
  color: var(--accent3-color);
}
.nordjson .jv-item.jv-function {
  color: #067bca;
}
.nordjson .jv-item.jv-number {
  color: var(--accent3-color);
}
.nordjson .jv-item.jv-number-float {
  color: var(--accent3-color);
}
.nordjson .jv-item.jv-number-integer {
  color: var(--accent3-color);
}
.nordjson .jv-item.jv-object {
  color: var(--text-color-secondary);
}
.nordjson .jv-item.jv-undefined {
  color: var(--accent5-color);
}
.jv-string {
  color: var(--accent-color) !important;
  word-break: break-word;
  white-space: normal;
}
.nordjson .jv-code .jv-toggle:before {
  padding: 0px 2px;
  border-radius: 2px;
}
.nordjson .jv-code .jv-toggle:hover:before {
  background: #eee;
}
</style>

<style scoped>

.node-list{
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;

    justify-content: space-between;

    gap: 12px;

    margin: 12px;
}

.node{
  width: calc(33% - 36px);

  height: 140px;
  padding: 12px;

  text-align: left;
    
  background: var(--background-color-secondary);
  color: var(--text-color-primary);
  user-select: none;
  border-radius: var(--border-rad-primary);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
}

.node {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 0.1fr; 
  grid-template-rows: 0.75fr 0.75fr 0.75fr 0.75fr 0.5fr; 
  gap: 0px 0px; 
  grid-template-areas: 
    "hostname hostname hostname update-stripe"
    "job job job update-stripe"
    "labels labels labels update-stripe"
    "exporters exporters exporters update-stripe"
    "registered registered registered live-circle"; 
}

@media only screen and (max-width: 1200px){
  .node{
    width: calc(50% - 32px);
  }
}

@media only screen and (max-width: 800px){
  .node{
    width: 100%;
  }
}

/* grid.layoutit.com?id=l1asNBh */

.update-stripe { grid-area: update-stripe; }
.hostname { grid-area: hostname; }
.job { grid-area: job; }
.labels { grid-area: labels; }
.exporters { grid-area: exporters; }
.registered { grid-area: registered; }
.live-circle { grid-area: live-circle; }

.hostname{
  font-size: 16px;
  font-weight: bold;
}

.update-stripe{
  transition: 0.2s;

  border-radius: 24px;
  height: 100%;
  width: 8px;

  background-color: var(--text-color-secondary);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
}

.live-circle{
  margin-top: 8px;
  width: 8px;
  height: 8px;

  border-radius: 24px;
  background-color: var(--accent3-color);

  /*
  --accent3-color: #bf616a;
  --accent4-color: #ebcb8b;
   */
}

.label{
    /*var(--accent5-color)*/
    background-color: rgba(208, 135, 112, 0.7);
    border-radius: var(--border-rad-secondary);
    padding: 3px;
    padding-top: 2px;
    padding-bottom: 2px;
    margin-right: 4px;
}

.metric{
  /*var(--accent3-color)*/
    background-color: rgba(191, 97, 106, 0.7);

    border-radius: var(--border-rad-secondary);
    padding: 3px;
    padding-top: 2px;
    padding-bottom: 2px;
    margin-right: 4px;
}

.metric-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    flex-grow: 1;
    align-items: flex-start;
}

.metric-card{
    padding: 12px;
    margin: 12px;
    border-radius: var(--border-rad-secondary);
    text-decoration: none;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,.4),0 6px 20px 0 rgba(0,0,0,.3);
}

</style>