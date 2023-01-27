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

      <div class="dashboard" v-for="dashboard in this.dashboards" v-bind:key="dashboard">
        <a :href="'/dash/'+dashboard.id">
          <font-awesome-icon icon="fa-solid fa-chart-line" /> {{ dashboard.name }}
        </a>
        <span>
          {{dashboard.id}} <font-awesome-icon icon="fa-solid fa-x" @click="removeDashboard(dashboard.id)"/> 
        </span>
      </div>
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
    getIndexFromList(val){
      return this.dashboards.map(item => item.i).indexOf(val);
    },

    addDashboard(){
      document.getElementById('dashboard-add').style.cursor = 'wait';

      this.axios.post(this.api_server + "/api/dashboards/add").then((response) => {
        console.log(response.data.task.generated_keys[0])
        this.$router.push({path: '/dash/'+response.data.task.generated_keys[0]});
      })
    },

    removeDashboard(id){
      const index = this.getIndexFromList(id);
      this.dashboards.splice(index, 1);

      this.axios.post(this.api_server + "/api/dashboards/remove", {id: id}).then((response) => {
        console.log(response.data)
      })
    }
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

a {
  text-decoration: none;
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