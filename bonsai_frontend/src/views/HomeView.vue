<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-house" /> Home
      </h1>
    </div>

    <div class="node-list">
        <div class="node" v-for="host in this.hosts" v-bind:key="host">
            <div class="hostname">
              <font-awesome-icon icon="fa-solid fa-server" />
              {{ host.host }}
            </div>

            <div class="job">{{host.job}}</div>
            <div class="labels">
              <span class="label" v-for="label in host.labels" v-bind:key="label">{{ label }}</span>
            </div>

            <div class="metrics">
              <span class="metric" v-for="scraper in host.scrapers" v-bind:key="scraper">{{ scraper }}</span>
            </div>

            <!--<div class="intervals">{{host.interval}} Seconds</div>-->

            <div class="registered"><time-since :date="new Date(host.registration_date)" /></div>

            <div class="update-stripe" :id="host.id"></div>
            <div class="live-circle" :id="'live-circle-'+hosts_status[host.id].status"></div>
      </div>
    </div>
  </div>
</template>

<script>
import TimeSince from '@/components/TimeSince';
import io from 'socket.io-client';
import 'vue-select/dist/vue-select.css';

export default {
    components: {
      TimeSince
    },
    data() {
        return {
            hosts: {},
            hosts_status: {},
            count: 0,
            //socket: io('', {path: "/ws"}),
            socket: io(this.socket_io_server, {path: "/ws"}),
        }
    },
    created() {
      //this.socket = io(this.socket_io_server, {path: "/ws"})
      this.socket.open()

      this.socket.on("hosts_general_update", (row) => {
         this.hosts_status[row.id] = {status: 'down'}
        this.hosts[row.id] = row
      });

      this.socket.on("hosts_deletion_update", (row) => {
        console.log(row)
        delete this.hosts[row.id]
      });

      this.socket.on("metric_update", (row) => {
        this.blink(row.id);

        this.update_status(row);
      })

      this.socket.send(JSON.stringify({
          type: "update_listener_host",
          content: []
      }));

      this.socket.send(JSON.stringify({
        type: "udpate_listener_updates",
        content: []
      }));
    },

    unmounted() {
      this.socket.close()
      //this.socket = null
    },

    methods: {
      update_socket_listener(event){
        this.socket.close()
        this.socket.open()

        this.metrics = {}
        this.hosts = {}
        
        this.socket.send(JSON.stringify({
          type: "update_listener_host",
          content: [event]
        }));

        this.socket.send(JSON.stringify({
          type: "update_listener",
          content: [event]
        }));
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

      blink(id){
        if(document.getElementById(id) != null){
          document.getElementById(id).style.backgroundColor = 'var(--accent-color)'
          setTimeout(()=>{
            document.getElementById(id).style.backgroundColor = 'var(--text-color-secondary)'
          },250)
        }
      },

      update_status(row){
        let diff = Date.parse(row.date) - Date.parse(this.hosts_status[row.id].date)
        let status = 'fluc'

        if(diff < (this.hosts[row.id].interval * 1000) + 250){
          status = 'up'
        }

        this.hosts_status[row.id] = {status: status, date: row.date}

        setTimeout(()=>{
          if(this.hosts_status[row.id].date == row.date){
            this.hosts_status[row.id] = {status: 'down', date: row.date}
          }
        },(this.hosts[row.id].interval * 1000 * 3))
      }
    },
}
</script>

<style scoped>
/* tmp updtime */
#live-circle-up{
  background-color: var(--accent-color);
}

#live-circle-fluc{
  background-color: var(--accent4-color);
}

#live-circle-down{
  background-color: var(--accent3-color);
}

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