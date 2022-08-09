<template>
  <div class="home">
    <h1>Admin Panel</h1>

    <button @click="purge_database_entries()">Purge DB</button>
  </div>
</template>

<script>

export default {
  components: {

  },
  data() {
    return { }
  },
  created() {
  
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