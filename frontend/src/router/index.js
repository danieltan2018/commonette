import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: () => import('../views/Recommend.vue')
  },
  {
    path: '/questionnaire',
    name: 'Questionnaire',
    component: () => import('../views/Questionnaire.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
