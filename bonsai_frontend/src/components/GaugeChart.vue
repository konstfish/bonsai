<template>
  <div>
    <apexchart
      width="100%"
      height="300"
      type="radialBar"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
export default {
  props: {
    metric: Number
  },
  watch: {
    metric: function(metric){
      this.series = [ metric.toFixed(1) ]
    }
  },
  data: function() {
    return {
      chartOptions: {
        chart: {
          id: "bar-gague",
        },
        plotOptions: {
        radialBar: {
          startAngle: -135,
          endAngle: 135,
          dataLabels: {
            name: {
              fontSize: '16px',
              color: 'var(--text-color-primary)',
              offsetY: 120,
              show: false,
            },
            value: {
              offsetY: -10,
              fontSize: '18px',
              color: 'var(--text-color-primary)',
            }
          }
        }
      },
      fill: {
        type: 'gradient',
        gradient: {
            shade: 'dark',
            shadeIntensity: 0.0,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 50, 65, 91]
        },
      },
      stroke: {
        lineCap: 'round'
      },
      labels: ["CPU Utilization"],
      },
      series: [0],
    };
  },
  created() {
  },
};
</script>