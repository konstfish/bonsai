<template>
  <div class="home">
    <h1>Metric Overview</h1>

    <div class="metric-container">
      <div class="metric-card" v-for="metric in this.metrics" v-bind:key="metric">
        <h4>{{ metric.job }}</h4>
        <h5>{{ metric.host }}</h5>

        <div v-for="(value, point) in metric.values" v-bind:key="point.point">
          {{ point }} - {{ value }}
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

export default {
    components: {
      TimeSince
    },
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

<style scoped>
.metric-container {
    display: flex;
}

.metric-card{
  padding: 12px;
  margin: 12px;
  border-radius: 6px;
  text-decoration: none;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,.4),0 6px 20px 0 rgba(0,0,0,.3);

  height: 220px;
  width: 220px;
}
</style>