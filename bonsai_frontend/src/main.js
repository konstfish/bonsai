import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios';
import VueAxios from 'vue-axios';

axios.defaults.headers.common = {
    "Content-Type": "application/json"
}

import VNetworkGraph from "v-network-graph"
import "v-network-graph/style.css"

import VueCountdown from '@chenfengyuan/vue-countdown';

import vSelect from 'vue-select'

import VueApexCharts from "vue3-apexcharts";

import JsonViewer from 'vue-json-viewer'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faServer, faChartLine, faHouse, faCircleNodes, faHammer, faSeedling, faBars, faPlus, faCompassDrafting } from '@fortawesome/free-solid-svg-icons'
import { faHeart } from '@fortawesome/free-regular-svg-icons'

library.add(faServer)
library.add(faChartLine)
library.add(faCircleNodes)
library.add(faHouse)
library.add(faHammer)
library.add(faSeedling)
library.add(faBars)
library.add(faPlus)
library.add(faCompassDrafting)

library.add(faHeart)

import { TroisJSVuePlugin } from 'troisjs';

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.use(VNetworkGraph);

app.use(VueApexCharts);

app.use(JsonViewer);

app.component('v-select', vSelect);

app.component(VueCountdown.name, VueCountdown);

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(TroisJSVuePlugin);

console.log(process.env.NODE_ENV)

if(process.env.NODE_ENV === "production"){
    app.config.globalProperties.socket_io_server = '';
    app.config.globalProperties.api_server = '';
}else{
    app.config.globalProperties.socket_io_server = 'http://localhost:9000';
    app.config.globalProperties.api_server = 'http://localhost:9000';
}

app.mount('#app');
