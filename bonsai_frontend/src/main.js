import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// axios for HTTP requests
import axios from 'axios';
import VueAxios from 'vue-axios';

axios.defaults.headers.common = {
    "Content-Type": "application/json"
}

// network graph for node view
import VNetworkGraph from "v-network-graph"
import "v-network-graph/style.css"

import VueCountdown from '@chenfengyuan/vue-countdown';

// vSelect for dropdown menus
import vSelect from 'vue-select'

// apexcharts for dashboarding view
import VueApexCharts from "vue3-apexcharts";

// json view for explore view
import JsonViewer from 'vue-json-viewer'

// import fontawesome icons
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faServer, faChartLine, faHouse, faCircleNodes, faHammer, 
        faSeedling, faBars, faPlus, faCompassDrafting, faFloppyDisk,
        faGaugeHigh, faChartColumn, faChartArea, faGear, faX } from '@fortawesome/free-solid-svg-icons'
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
library.add(faFloppyDisk)
library.add(faGaugeHigh)
library.add(faChartColumn)
library.add(faChartArea)
library.add(faGear)
library.add(faX)
library.add(faHeart)

import { TroisJSVuePlugin } from 'troisjs';

// create Vue App
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

// check what env deployment is in, set socket & api server accordingly
if(process.env.NODE_ENV === "production"){
    app.config.globalProperties.socket_io_server = '';
    app.config.globalProperties.api_server = '';
}else{
    app.config.globalProperties.socket_io_server = 'http://localhost:9000';
    app.config.globalProperties.api_server = 'http://localhost:9000';
}

app.mount('#app');
