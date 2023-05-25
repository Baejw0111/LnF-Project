import Vue from "vue";
import VueRouter from "vue-router";
import Regist from "../views/RegistView.vue";
import List from "../views/ListView.vue";
import History from "../views/HistoryView.vue";
import LostItem from "../views/LostItem.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: Regist,
  },
  {
    path: "/list",
    component: List,
  },
  {
    path: "/list/:id",
    component: LostItem,
  },
  {
    path: "/history",
    component: History,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
