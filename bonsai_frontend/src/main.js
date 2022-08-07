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

app.mount('#app');
