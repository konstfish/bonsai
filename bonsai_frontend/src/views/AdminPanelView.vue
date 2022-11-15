<template>
  <div class="home">
    <h1><font-awesome-icon icon="fa-solid fa-hammer" /> Admin Panel</h1>

    <span>{{ metric_amount }}</span>

    <button @click="purge_database_entries()">Purge DB</button>
  
  </div>
</template>

<script>

export default {
  components: {

  },
  data() {
    return {
      metric_amount: 0
    }
  },
  created() {
    this.axios.get(this.api_server + "/api/admin/amount").then((response) => {
        this.metric_amount = response.data.amount
      })
  },

  methods: {
    purge_database_entries(){
      this.axios.get(this.api_server + "/api/admin/purge").then((response) => {
        console.log(response.data)
      })
    },    
  },
}
</script>

<style scoped>

</style>