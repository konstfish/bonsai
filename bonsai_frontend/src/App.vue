<template>
  <div class="wrapper">
    
    <div class="nav-wrapper">
      <nav>
        <router-link to="/"><font-awesome-icon icon="fa-solid fa-house" /> Home</router-link>
        <router-link to="/nodes"><font-awesome-icon icon="fa-solid fa-circle-nodes" /> Node Graph</router-link>
        <router-link to="/dash"><font-awesome-icon icon="fa-solid fa-chart-line" /> Dashboard</router-link>
        <router-link to="/admin"><font-awesome-icon icon="fa-solid fa-hammer" /> Admin Panel</router-link>
      </nav>
      <span class="made-with">Made with <font-awesome-icon icon="fa-regular fa-heart" /></span>
    </div>

    <div class="nav-spacer"></div>

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
  height: 100%;

  margin: 0px;
  background-color: var(--background-color-primary);
}

body, html{
}

h1, h2, h3, h4, h5, h6, span{
  color: var(--text-color-primary);
}

#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}

.nav-spacer{
  height: 100%;
  margin-right: calc(180px + 16px);
}

.nav-wrapper{
  display: flex;
  flex-wrap: wrap;

  position: fixed;
  right: 0;
  top: 0;
  left: 0;

  background-color: var(--background-color-secondary);

  width: 180px;
  height: calc(100% - 24px);
  margin-top: 12px;
  margin-bottom: 12px;

  border-top-right-radius: 12px;
  border-bottom-right-radius: 12px;

  margin-right: 24px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1), 0 6px 20px 0 rgba(0, 0, 0, 0.1);
}

nav {
  display: flex;
  flex-direction: column;
  width: 180px;
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

.made-with{
  align-self: flex-end;
  padding: 12px;
  margin-left: 12px;
  font-size: 12px;
}

.made-with svg {
  color: var(--accent3-color);
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
