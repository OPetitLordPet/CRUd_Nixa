import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
      path: "/create",
      name: "create",
      component: () => import("./components/CreateClient.vue")
    },
    {
      path: "/edit/:id",
      name: "edit",
      component: () => import("./components/EditClient.vue")
    },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/ClientList.vue")
    },
  ]
});
