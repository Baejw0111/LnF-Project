<template>
  <div class="list">
    <div class="router-header">
      <div>분실물 목록</div>
    </div>
    <div class="router-body">
      <div v-for="lost in list" :key="lost.id">
        <div @click="moveDetail(lost.id)" class="lost-container">
          <div
            class="lost-image"
            :style="`background-image:url(${setImage(lost.image)})`"
          ></div>

          <div class="lost-info-wrapper">
            <h2 class="lost-name">
              {{ lost.name }}
            </h2>
            <p class="lost-date">습득일자 {{ lost.date }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api } from "../utils/api.js";

export default {
  data() {
    return {
      list: [],
    };
  },
  async created() {
    const result = await api.list.findAll();

    this.list = result.data;
    console.log(this.list);
  },
  methods: {
    setImage(image_src) {
      // return `http://43.201.65.87:8080/${image_src}`;
      return `http://localhost:8080/${image_src}`;
    },
    moveDetail(id) {
      this.$router.push(`/list/${id}`);
    },
  },
};
</script>

<style>
.lost-container {
  display: flex;
  align-items: center;
  border: 3px solid black;
  border-radius: 10px;
  cursor: pointer;
  margin: 10px;
  width: 100%;
}

.lost-info-wrapper {
  margin: 0 auto;
  text-align: center;
}

.lost-name {
  font-size: 25px;
  font-weight: bold;
}

.lost-date {
  padding-top: 10px;
}

.lost-image {
  background-color: #42b983;
  background-size: cover;
  background-position: center;
  width: 180px;
  height: 180px;
}
</style>
