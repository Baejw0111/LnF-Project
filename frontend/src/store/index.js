import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isPC: true, // 현재 디바이스가 PC인지 모바일인지 구분
  },
  getters: {},
  mutations: {
    CHANGE_IS_PC(state, data) {
      state.isPC = data;
    },
  },
  actions: {},
  modules: {},
});
