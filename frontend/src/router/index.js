import Vue from 'vue'
import VueRouter from 'vue-router'
import Instance from "../views/Instance";
import Global from "../views/Global";
import Training from "../views/Training";
import Prediction from "../views/Prediction";


Vue.use(VueRouter)

const routes = [
  {
    path: "/instance",
    name:"Instance",
    component: Instance
  },
      {
    path: "/global",
    name:"Global",
    component: Global
  },
  {
    path: "/training",
    name:"Training",
    component: Training
  },
  {
    path: "/prediction",
    name:"Prediction",
    component: Prediction
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
