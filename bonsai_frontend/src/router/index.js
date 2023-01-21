import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/archive/HomeView_OLD.vue'
import NodeView from '../views/NodeView.vue'
import AdminPanelView from '../views/AdminPanelView.vue'
import DashboardView from '../views/DashboardView.vue'
import NodeOverviewView from '../views/HomeView.vue'
import DashboardListView from '../views/DashboardListView.vue'
import ExploreView from '../views/ExploreView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: NodeOverviewView
  },
  {
    path: '/home2',
    name: 'home2',
    component: HomeView
  },
  {
    path: '/nodes',
    name: 'nodes',
    component: NodeView
  },
  {
    path: '/explore',
    name: 'explore',
    component: ExploreView
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPanelView
  },
  {
    path: '/dash/:id',
    name: 'dashboard',
    component: DashboardView
  },
  {
    path: '/dashboards',
    name: 'dashboards',
    component: DashboardListView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
