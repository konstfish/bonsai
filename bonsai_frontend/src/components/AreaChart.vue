<template>
  <div>
    <apexchart
      type="area"
      width="100%"
      height="250"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
export default {
  props: {
    points: Number,
    metric: Object
  },
  watch: {
    metric: function(metric){
      if(this.series[0].data.length > this.points){
        this.series[0].data.shift();
        this.chartOptions.xaxis.categories.shift();
      }

      this.series[0].data.push(metric.val)
      this.chartOptions.xaxis.categories.push(metric.date)
    }
  },
  data: function() {
    return {
      series: [{
            name: 'series1',
            data: []
          }],
      chartOptions: {
          chart: {
            type: 'area'
          },
          dataLabels: {
            enabled: false
          },
          stroke: {
            curve: 'smooth'
          },
          xaxis: {
            type: 'datetime',
            categories: []
          },
          tooltip: {
            x: {
              format: 'dd/MM/yy HH:mm'
            },
          },
        },
    };
  },
  created() {
  },
};
</script>