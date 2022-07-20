<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

    <div>
      <div v-for="(id, metric) in this.metrics.values" v-bind:key="id.id">
        <h4>{{ metric.host }}</h4>
        <h5>{{ metric.job }}</h5>
        
        <div v-for="(value, point) in metric.values" v-bind:key="point.point">
          {{ point }} - {{ value }}
        </div>

      </div>
    </div>
  </div>
</template>

<script>

import io from 'socket.io-client';

export default {
    data() {
        return {
            metrics: {},
            socket: io('', {path: "/ws"}),
        }
    },
    created() {
      this.socket.on("test", (row) => {
        console.log(row)
        this.metrics[row.id] = row
      })
    },

    methods: {
    },
}
</script>
