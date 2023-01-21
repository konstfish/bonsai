<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-circle-nodes" /> Home View Test
      </h1>
    </div>
    
    {{labels}}
    {{count}}
    <v-select :options="labels" @option:deselected="count++" @option:selected="update_socket_listener"></v-select>


    <div class="metric-container">
      <div class="metric-card" v-for="metric in this.metrics" v-bind:key="metric">
        <h4>{{ hosts[metric.id].job }}</h4>
        <h5>{{ hosts[metric.id].host }}</h5>

        <div v-for="(metrics, point) in metric.metrics" v-bind:key="point.point">
          {{ point }} - {{ metrics }}
        </div>

        <br>
        <time-since :date="new Date(metric.date)" />
      </div>
    </div>

  <Renderer ref="renderer">
    <Camera :position="{ z: 5 }" />
    <Scene>
      <PointLight :position="{ y: 50, z: 50 }" />
      <Box ref="box" :rotation="{ y: Math.PI / 4, z: Math.PI / 4 }" :scale="{ x: 1, y: 3, z: 0.25 }">
        <LambertMaterial />
      </Box>
    </Scene>
  </Renderer>

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
            hosts: {},
            labels: [],
            count: 0,
            //socket: io('', {path: "/ws"}),
            socket: io(this.socket_io_server, {path: "/ws"}),
            box: {}
        }
    },
    created() {
      //this.socket = io(this.socket_io_server, {path: "/ws"})
      this.socket.open()

      this.socket.on("label_list", (row) => {
        this.labels = row
      });

      this.socket.on("hosts_general_update", (row) => {
        this.hosts[row.id] = row
      });

      this.socket.on("metrics_general_update", (row) => {
        console.log(row)
        this.metrics[row.id] = row
        this.box.x = row.metrics.ACCEL.x
        this.box.y = row.metrics.ACCEL.y
        this.box.z = row.metrics.ACCEL.z
      });

      this.socket.on("metrics_deletion_update", (row) => {
        console.log(row)
        delete this.metrics[row.id]
        delete this.hosts[row.id]
      });

      this.socket.send(JSON.stringify({
          type: "get_labels",
          content: []
        }));
    },

    mounted() {
      const renderer = this.$refs.renderer;
      const box = this.$refs.box.mesh;
      renderer.onBeforeRender(() => {
        box.rotation.x = this.box.y;
        box.rotation.y = this.box.x;
        box.rotation.z = this.box.z;
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

        this.metrics = {}
        this.hosts = {}
        
        this.socket.send(JSON.stringify({
          type: "update_listener",
          content: [event]
        }));

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
  border-radius: var(--border-rad-secondary);
  text-decoration: none;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,.4),0 6px 20px 0 rgba(0,0,0,.3);
}
</style>