<template>
  <div class="wrapper">
    <nav>
      <h1>Bonsai</h1>
      <router-link to="/">Home</router-link>
      <router-link to="/nodes">Node Graph</router-link>
      <br>
      <router-link to="/admin">Admin Panel</router-link>
    </nav>

    <router-view/>
  </div>
</template>

<style>
html, body{
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

nav {
  display: flex;
  flex-direction: column;

  padding: 12px;
  width: 240px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 12px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.home {
  width: 100%;
}

.wrapper {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-evenly;
}
</style>
