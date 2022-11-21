<template>
  <div class="wrapper">    
    <div class="nav-wrapper">
      <nav>
        <router-link to="/">
          <font-awesome-icon icon="fa-solid fa-house" /> <span>Home</span>
        </router-link>
        <router-link to="/nodes">
          <font-awesome-icon icon="fa-solid fa-circle-nodes" /> <span>Node Graph</span>
        </router-link>
        <router-link to="/dash">
          <font-awesome-icon icon="fa-solid fa-chart-line" /> <span>Dashboard</span>
        </router-link>
        <router-link to="/admin">
          <font-awesome-icon icon="fa-solid fa-hammer" /> <span>Admin Panel</span>
        </router-link>
      </nav>

      <span class="made-with">Made with <font-awesome-icon icon="fa-regular fa-heart" /></span>
    </div>

    <!--<div class="nav-spacer"></div>-->

    <router-view/>
  </div>
</template>

<style>
:root{
  --background-color-primary: #2e3440;
  --background-color-secondary: #3b4252;

  --text-color-primary: #e5e9f0;
  --text-color-secondary: #eceff4;

  --accent-color: #a3be8c;
  --accent2-color: #b48ead;
  --accent3-color: #bf616a;
  --accent4-color: #ebcb8b;
  --accent5-color: #d08770;

  --font-size: 12px;
  --font-size-secondary: 8px;

  --border-rad-primary: 8px;
  --border-rad-secondary: 6px;
}

@media (prefers-color-scheme: light) {
  :root{
    --background-color-primary: #e5e9f0;
    --background-color-secondary: #eceff4;

    --text-color-primary: #2e3440;
    --text-color-secondary: #3b4252;
  }
}

.wrapper{
  height: 100%;
}

html, body{
  height: 100vh;
  width: 100vw;

  margin: 0px;
  background-color: var(--background-color-primary);
  overflow: hidden;
}

h1, h2, h3, h4, h5, h6, span, div{
  color: var(--text-color-primary);
}

#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}

.wrapper {
  display: grid; 
  grid-template-columns: 0.3fr 1.7fr 1fr; 
  grid-template-rows: 1.9fr 1fr; 
  gap: 0px 0px; 
  grid-template-areas: 
    "nav-wrapper router-view router-view"
    "nav-wrapper router-view router-view"; 
}

.nav-wrapper { grid-area: nav-wrapper; }
.home { grid-area: router-view; }

.home{
  overflow: auto;
  overflow-x: hidden;
}

.header{
  border-radius: var(--border-rad-primary);
  margin: 12px;

  padding: 12px;
  background-color: var(--background-color-secondary);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
}

.header h1{
  margin: 0;
}

.nav-wrapper{
  display: flex;
  flex-wrap: wrap;

  background-color: var(--background-color-secondary);

  height: calc(100% - 24px);
  width: 180px;

  border-radius: var(--border-rad-primary);
  margin: 12px;
  margin-right: 0px;


  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
  transition: 0.05s;
}

nav {
  display: flex;
  flex-direction: column;
  padding: 12px;
}


nav a {
  font-weight: bold;
  color: var(--text-color-secondary);
  margin: 12px;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: var(--accent-color);
}

nav a.router-link-exact-active span {
  color: var(--accent-color);
}

.made-with{
  align-self: flex-end;
  padding: 12px;
  margin-left: 12px;
  font-size: 12px;
}

.made-with svg {
  color: var(--accent3-color);
}

@media only screen and (max-width: 800px){
  .node{
    width: 90%;
  }
  
  nav a span{
    display: none;
  }

  .made-with{
    display: none;
  }

  .nav-wrapper{
    width: 66px;
  }
}

</style>
