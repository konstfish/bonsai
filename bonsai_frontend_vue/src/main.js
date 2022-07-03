import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import RethinkDB from 'vue-rethinkdb';

const app = createApp(App);
app.use(router);
app.use(RethinkDB, {url: 'wss://localhost:28015',
                    log: console});
app.mount('#app');
