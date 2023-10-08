<template>
  <div>
    <apexchart
      type="radialBar"
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
      this.series = metric
    }
  },
  data: function() {
    return {
      series: [],
      chartOptions: {
        chart: {
          id: "bar-gague-multi",
          width: "100%",
          height: "100%"
        },
        plotOptions: {
        radialBar: {
          startAngle: -135,
          endAngle: 135,
          dataLabels: {
            name: {
              fontSize: '16px',
              color: 'var(--text-color-primary)',
              offsetY: 120
            },
            value: {
              offsetY: -10,
              fontSize: '18px',
              color: 'var(--text-color-primary)',
            },
            total: {
              show: true,
              label: "",
              offsetY: -10,
              fontSize: '18px',
              color: 'var(--text-color-primary)',
              formatter: function (arr) {
                // console.log(arr)
                return (arr.globals.seriesTotals.reduce((a,b) => a + b, 0) / arr.globals.seriesTotals.length).toFixed(1) + "%"; 
              }
            },
          }
        }
      },
      stroke: {
        lineCap: 'round'
      },
      labels: ["CPU Utilization"],
      },
    };
  },
  created() {
  },
};
</script>