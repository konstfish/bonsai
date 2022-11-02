import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios';
import VueAxios from 'vue-axios';

import VNetworkGraph from "v-network-graph"
import "v-network-graph/style.css"

import VueCountdown from '@chenfengyuan/vue-countdown';

import vSelect from 'vue-select'

import VueApexCharts from "vue3-apexcharts";

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.use(VNetworkGraph);

app.use(VueApexCharts);

app.component('v-select', vSelect);

app.component(VueCountdown.name, VueCountdown);

console.log(process.env.NODE_ENV)

if(process.env.NODE_ENV === "production"){
    app.config.globalProperties.socket_io_server = '';
    app.config.globalProperties.api_server = '';
}else{
    app.config.globalProperties.socket_io_server = 'http://localhost:9000';
    app.config.globalProperties.api_server = 'http://localhost:9000';
}

app.mount('#app');
