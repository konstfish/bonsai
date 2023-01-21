<template>
  <div class="home">
    <div class="header">
      <h1>
        <font-awesome-icon icon="fa-solid fa-chart-line" /> Dashboards
      </h1>
    </div>
    <div class="dashboard-container">
      <a class="dashboard" id="dashboard-add" @click="addDashboard">
        <span>
          <font-awesome-icon icon="fa-solid fa-plus" /> Add Dashboard
        </span>
      </a>

      <a :href="'/dash/'+dashboard.id" class="dashboard" v-for="dashboard in this.dashboards" v-bind:key="dashboard">
        <span>
          <font-awesome-icon icon="fa-solid fa-chart-line" /> {{ dashboard.name }}
        </span>
        {{dashboard.id}}
      </a>
    </div>
  </div>
</template>

<script>

export default {
  components: {

  },
  data() {
    return {
      dashboards: []
    }
  },
  created() {
    this.axios.get(this.api_server + "/api/dashboards/list").then((response) => {
        console.log(response.data.return)
        this.dashboards = response.data.return
      })
  },

  methods: {
    addDashboard(){
      document.getElementById('dashboard-add').style.cursor = 'wait';

      this.axios.post(this.api_server + "/api/dashboards/add").then((response) => {
        console.log(response.data.task.generated_keys[0])
        this.$router.push({path: '/dash/'+response.data.task.generated_keys[0]});
      })
    },
  },
}
</script>

<style scoped>
.dashboard{
  display: block;
  border-radius: var(--border-rad-primary);
  margin: 12px;

  padding: 12px;
  background-color: var(--background-color-secondary);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);

  text-decoration: none;

  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
}

a:link{
  color: var(--text-color-primary);
}

a:visited{
  color: var(--text-color-primary);
}

#dashboard-add{
  cursor: pointer;
}

</style>