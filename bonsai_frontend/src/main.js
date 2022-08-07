import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios';
import VueAxios from 'vue-axios';

import VNetworkGraph from "v-network-graph"
import "v-network-graph/style.css"

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.use(VNetworkGraph)

app.mount('#app');
