<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

    <div>
      <h4>{{ this.metrics.host }}</h4>
      <h4>{{ this.metrics.job }}</h4>

      <h3>Metrics</h3>
      <div v-for="(value, point) in metrics.values" v-bind:key="point.point">
        {{ point }} - {{ value }}
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
            socket: io('localhost:9000'),
        }
    },
    created() {
      this.socket.on("test", (row) => {
        console.log(row)
        this.metrics = row
      })
    },

    methods: {
    },
}
</script>
