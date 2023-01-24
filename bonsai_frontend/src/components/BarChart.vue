<template>
  <div>
    <apexchart
      width="100%"
      height="250"
      type="bar"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
export default {
  props: {
    metric: Array
  },
  watch: {
    metric: function(metric){
      //console.log(metric)
      /*if(this.chartOptions.xaxis.categories == []){
        var i = 0;
        while(i < metric.length){
          this.chartOptions.xaxis.categories.push(i);

          i += 1
        }
      }*/
      this.series[0].data = metric
    }
  },
  data: function() {
    return {
      chartOptions: {
        chart: {
          id: "vuechart-example",
        },
        // https://apexcharts.com/docs/options/xaxis/
        xaxis: {
          type: "numeric",
          tickAmount: 'dataPoints',
          decimalsInFloat: 0,
          labels: {
            style: {
              colors: 'var(--text-color-primary)'
            }
          }
        },
        yaxis: {
          labels: {
            style: {
              colors: 'var(--text-color-primary)'
            }
          }
        },
        dataLabels: {
        enabled: true,
        style: {
          colors: ['var(--text-color-primary)']
        },
      },
      },
      series: [
        {
          name: "series-1",
          data: [],
        },
      ],
    };
  },
  created() {
  },

};
</script>