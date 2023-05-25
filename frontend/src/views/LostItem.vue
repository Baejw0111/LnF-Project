<template>
  <div class="lost">
    <div class="router-header">
      <div>분실물 상세 정보</div>
    </div>
    <div class="router-body detail-body">
      <b-card
        v-if="data && data.image"
        :img-src="setImage()"
        img-alt="Image"
        :img-left="windowWidth > 1000"
        img-width="400px;"
        img-height="300px;"
        tag="article"
        class="mb-2 border-0 detail-card"
        style="width: 100%"
      >
        <b-card-text class="text-container">
          <div style="font-size: 40px">{{ data.name }}</div>
          <div>
            신고 날짜: <span style="font-weight: normal">{{ data.date }}</span>
          </div>
          <div>
            신고 시각: <span style="font-weight: normal">{{ data.time }}</span>
          </div>
          <div>
            발견 장소: <span style="font-weight: normal">{{ data.place }}</span>
          </div>
          <div>
            상세 정보:
            <span style="font-weight: normal">{{ data.detail }}</span>
          </div>
        </b-card-text>
      </b-card>

      <div class="btn-container">
        <b-button @click="find" href="#" variant="primary">찾기</b-button>
        <b-button @click="complete" href="#" variant="danger"
          >수령완료</b-button
        >
      </div>

      <div class="list-btn" v-if="$store.state.isPC">
        <b-button @click="moveList" href="#" variant="outline-primary"
          >목록</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { api } from "../utils/api.js";

export default {
  data() {
    return {
      data: {},
      windowWidth: 0,
    };
  },
  mounted() {
    this.windowWidth = window.innerWidth;
    window.addEventListener("resize", this.getWindowWidth);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.getWindowWidth);
  },
  async created() {
    const result = await api.list.findOne(this.$route.params.id);
    this.data = result.data[0];
  },
  methods: {
    // 창 너비 가져오기
    getWindowWidth() {
      this.windowWidth = window.innerWidth;
    },

    // 이미지 세팅
    setImage() {
      return `http://43.201.65.87:8080/${this.data.image}`;
    },

    // 목록으로 이동하기
    moveList() {
      this.$router.push("/list");
    },

    // 현재 조회 중인 아이템 목록에서 삭제
    async delete() {
      const result = await api.list.delete(this.$route.params.id);
      alert(result.data.message);
      this.moveList();
    },

    // DB에 해당 물건 찾아오기 명령
    async find() {
      console.log(this.data.date);
      const result = await api.command.find(
        this.data.date,
        this.data.time,
        this.data.name,
        this.data.place
      );

      console.log(result);
      if (result.data.success === true) {
        alert(result.data.message);
      } else {
        alert(result.data.message);
      }
    },

    // 수령 완료
    async complete() {
      const result = await api.command.complete(
        this.data.date,
        this.data.time,
        this.data.name,
        this.data.place
      );

      console.log(this.result);
      if (result.data.success === true) {
        alert(result.data.message);
        // 수령된 물건이므로 목록에서 삭제
        this.delete();
      } else {
        alert(result.data.message);
      }
    },
  },
};
</script>

<style>
.detail-body {
  display: flex;
  flex-direction: column;
}
.text-container {
  height: 300px;
  padding-left: 10%;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
}
.btn-container {
  margin-left: auto;
}
.list-btn {
  margin: auto;
  margin-top: 10%;
}
</style>
