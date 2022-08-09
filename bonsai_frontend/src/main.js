import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios';
import VueAxios from 'vue-axios';

import VNetworkGraph from "v-network-graph"
import "v-network-graph/style.css"

import VueCountdown from '@chenfengyuan/vue-countdown';

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.use(VNetworkGraph)

app.component(VueCountdown.name, VueCountdown);

app.config.globalProperties.socket_io_server = '';
//app.config.globalProperties.socket_io_server = 'http://localhost:9000';

app.config.globalProperties.api_server = 'http://rest:4000';
//app.config.globalProperties.api_server = 'http://localhost:4000';


app.mount('#app');
