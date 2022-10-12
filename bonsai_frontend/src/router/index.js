import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NodeView from '../views/NodeView.vue'
import AdminPanelView from '../views/AdminPanelView.vue'
import DashboardView from '../views/DashboardView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/nodes',
    name: 'nodes',
    component: NodeView
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPanelView
  },
  {
    path: '/dash',
    name: 'dashboard',
    component: DashboardView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
