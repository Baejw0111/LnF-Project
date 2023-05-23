<template>
  <div id="app">
    <div class="sidebar" v-if="$store.state.isPC">
      <div class="sidebar-header">
        <div>
          <span>L</span>
          <span style="font-size: 53px">&</span>
          <span>F</span>
          <span style="font-size: 13px">Lost and Found</span>
        </div>
      </div>
      <ul>
        <li>
          <router-link to="/" :class="{ active: $route.path === '/' }"
            >Regist</router-link
          >
        </li>
        <li>
          <router-link to="/list" :class="{ active: $route.path === '/list' }"
            >List</router-link
          >
        </li>
        <li>
          <router-link
            to="/history"
            :class="{ active: $route.path === '/history' }"
            >History</router-link
          >
        </li>
      </ul>
    </div>
    <router-view v-if="$store.state.isPC" class="costom-router-view" />
    <router-view v-else />
  </div>
</template>

<script>
export default {
  data() {
    return {
      isPC: false,
    };
  },
  mounted() {
    this.checkDeviceType();
    window.addEventListener("resize", this.checkDeviceType);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.checkDeviceType);
  },
  methods: {
    checkDeviceType() {
      if (window.innerWidth > 600 && this.$store.state.isPC === false) {
        this.$store.commit("CHANGE_IS_PC", true);
      } else if (window.innerWidth < 600 && this.$store.state.isPC === true) {
        this.$store.commit("CHANGE_IS_PC", false);
      }
    },
  },
};
</script>

<style>
#app {
  /*부트스트랩 폰트 교체*/
  font-family: Avenir, Helvetica, Arial,
    sans-serif var(--font-family-sans-serif);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.sidebar {
  width: 245px;
  background: #349167;
  height: 100%;
  overflow: auto;
  position: fixed;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  font-size: 30px;

  display: flex;
  align-content: center;
  flex-direction: column;
}

.sidebar-header {
  background: #42b983;
  height: 100px;
  font-size: 65px;
  font-weight: bold;
  padding-left: 10px;
  padding-top: 20px;

  display: flex;
  align-items: center;
}

.sidebar ul {
  padding: 0px;
  margin: 0px;
  list-style-type: none;
}

.sidebar li a {
  text-decoration: none;
  padding: 20px;
  display: block;
  color: #000;
  font-weight: bold;
  font-size: 25px;
}

.sidebar li a:hover {
  background: #286e4f;
  color: #fff;
}

.sidebar li a.active {
  background: #286e4f;
  color: #fff;
}

.sidebar li a.home {
  background: #42b983;
  color: #fff;
}

.costom-router-view {
  margin-left: 245px;
}

.router-header {
  padding-left: 20px;
  padding-top: 10px;
  height: 100px;
  font-size: 25px;
  font-weight: bold;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);

  display: flex;
  align-items: center;
}
.router-body {
  padding: 40px;
  width: 70%;
  height: 1200px;
  font-weight: bold;

  /* display: flex;
  justify-content: left;
  align-items: center; */
}
</style>
