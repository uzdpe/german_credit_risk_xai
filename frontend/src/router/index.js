import Vue from 'vue'
import VueRouter from 'vue-router'
import Instance from "../views/Instance";
import Global from "../views/Global";
import Training from "../views/Training";
import Intro from "../views/Intro";
import Survey from "../views/Survey";
import Prediction from "../views/Prediction";
import Testphase from "../views/Testphase";



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
    path: "/intro",
    name:"1. Intro",
    component: Intro
  },
  {
    path: "/Survey",
    name:"5. Survey",
    component: Survey
  },
  {
    path: "/Prediction",
    name:"4. Prediction",
    component: Prediction
  },
  {
    path: "/Testphase",
    name:"2. Testphase",
    component: Testphase
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
