import Vue from "vue";
import VueRouter from "vue-router";
import Regist from "../views/RegistView.vue";
import List from "../views/ListView.vue";
import History from "../views/HistoryView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "regist",
    component: Regist,
  },
  {
    path: "/list",
    name: "list",
    component: List,
  },
  {
    path: "/history",
    name: "history",
    component: History,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
