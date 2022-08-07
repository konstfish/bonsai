<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

    <vue-countdown :time="2 * 24 * 60 * 60 * 1000" v-slot="{ days, hours, minutes, seconds }">
      Time Remaining: {{ days }} days, {{ hours }} hours, {{ minutes }} minutes, {{ seconds }} seconds.
    </vue-countdown>

    <div>
      <div v-for="metric in this.metrics" v-bind:key="metric">
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
            //socket: io('http://10.0.1.108:3000', {path: "/ws"}),
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
