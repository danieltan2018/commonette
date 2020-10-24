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
    component: () => import('../views/Recommend.vue'),
    meta: {
      requiresRoom: true
    }
  },
  {
    path: '/questionnaire',
    name: 'Questionnaire',
    component: () => import('../views/Questionnaire.vue'),
    meta: {
      requiresRoom: true
    }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/Dashboard.vue'),
    meta: {
      requiresRoom: true
    }
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresRoom)) {
    if (localStorage.getItem("roomCode")) {
      next();
      return;
    } else {
      next("/");
      return;
    }
  } else {
    next();
  }
});

export default router
