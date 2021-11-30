import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
// import Register from "../views/Register.vue";
import Results from "../views/Results.vue";
import Athletes from "../views/Athletes.vue";
import Success from "../views/Success.vue";
import DisabledRegister from "../views/DisabledRegister.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/success",
    name: "Success",
    component: Success,
  },
  {
    path: "/register",
    name: "Register",
    component: DisabledRegister,
  },
  {
    path: "/results",
    name: "Results",
    component: Results,
  },
  {
    path: "/athletes",
    name: "Athletes",
    component: Athletes,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
