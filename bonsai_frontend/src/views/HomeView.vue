<template>
  <div class="home">
    <h1>Metric Overview</h1>
    
    {{labels}}
    {{count}}
    <v-select :options="labels" @option:deselected="count++" @option:selected="update_socket_listener"></v-select>


    <div class="metric-container">
      <div class="metric-card" v-for="metric in this.metrics" v-bind:key="metric">
        <h4>{{ metric.job }}</h4>
        <h5>{{ metric.host }}</h5>

        <div v-for="(metrics, point) in metric.metrics" v-bind:key="point.point">
          {{ point }} - {{ metrics }}
        </div>

        <br>
        <time-since :date="new Date(metric.date)" />
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
            metrics: {},
            labels: [],
            count: 0,
            //socket: io('', {path: "/ws"}),
            socket: io(this.socket_io_server, {path: "/ws"}),
        }
    },
    created() {
      //this.socket = io(this.socket_io_server, {path: "/ws"})
      this.socket.open()

      this.socket.on("label_list", (row) => {
        this.labels = row
      });

      this.socket.on("general_update", (row) => {
        console.log(row)
        this.metrics[row.id] = row
      });

      this.socket.on("deletion_update", (row) => {
        console.log(row)
        delete this.metrics[row.id]
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
        this.socket.send(JSON.stringify({
          type: "update_listener",
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

<style scoped>
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
  border-radius: 6px;
  text-decoration: none;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,.4),0 6px 20px 0 rgba(0,0,0,.3);
}
</style>