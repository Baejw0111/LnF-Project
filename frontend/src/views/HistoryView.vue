<template>
  <div class="history">
    <div class="router-header">
      <div>신고 및 반출 내역</div>
    </div>
    <div class="router-body">
      <div class="history-container">
        <div class="history-box">신고 날짜</div>
        <div class="history-box">신고 시각</div>
        <div class="history-box">분실물 이름</div>
        <div class="history-box">발견 장소</div>
        <div class="history-box">현재 상태</div>
      </div>
      <div v-for="info in history" :key="info.id">
        <div class="history-container">
          <div class="history-box">{{ info.date }}</div>
          <div class="history-box">{{ info.time }}</div>
          <div class="history-box">{{ info.name }}</div>
          <div class="history-box">{{ info.place }}</div>
          <div class="history-box">{{ info.state }}</div>
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
      history: [],
    };
  },
  async created() {
    const result = await api.history.findAll();

    this.history = result.data;
    console.log(history);
  },
  // methods: {
  // },
};
</script>
