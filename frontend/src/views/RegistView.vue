<template>
  <div class="regist">
    <div class="router-header">
      <div>분실물 등록</div>
    </div>
    <div class="router-body">
      <b-form class="register-form" @submit="create">
        <b-form-group
          id="date"
          label="신고 날짜"
          label-for="date-input"
          description="분실물 신고 날짜를 입력해주세요."
        >
          <b-form-input
            id="date-input"
            v-model="date"
            type="date"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-group
          id="time"
          label="신고 시각"
          label-for="time-input"
          description="분실물 신고 시각을 입력해주세요."
        >
          <b-form-input
            id="time-input"
            v-model="time"
            type="time"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-group id="name" label="분실물명" label-for="name-input">
          <b-form-input
            id="name-input"
            v-model="name"
            type="text"
            placeholder="분실물명을 입력해주세요"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-group
          id="place"
          label="분실물 발견 위치"
          label-for="place-input"
        >
          <b-form-input
            id="place-input"
            v-model="place"
            type="text"
            placeholder="분실물 발견 위치를 입력해주세요"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-group
          id="significant"
          label="분실물 상세 정보"
          label-for="significant-input"
        >
          <b-form-input
            id="significant-input"
            v-model="significant"
            type="text"
            placeholder="분실물의 상세 정보(색, 그림)들을 입력해주세요"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-file
          v-model="file"
          :state="Boolean(file)"
          placeholder="분실물 이미지 파일을 넣어주세요"
          drop-placeholder="이미지 파일을 드롭"
          required
        ></b-form-file>
        <div class="mt-3">Selected file: {{ file ? file.name : "" }}</div>
        <br />

        <b-button type="submit" variant="primary" style="float: right"
          >등록</b-button
        >
      </b-form>
    </div>
  </div>
</template>

<script>
import { api } from "../utils/api";

export default {
  data() {
    return {
      date: "",
      time: "",
      name: "",
      place: "",
      significant: "",
      file: null,
    };
  },
  methods: {
    async create() {
      console.log(this.date);
      const result = await api.list.create(
        this.date,
        this.time,
        this.name,
        this.place,
        this.significant,
        this.file
      );

      console.log(this.result);
      // result.data.success가 true인 경우에만 성공적으로 업로드
      if (result.data.success === true) {
        alert(result.data.message);
        // 성공했으니까 메세지 띄우고 라우터 이동
        this.$router.push("/list");
      } else {
        alert(result.data.message);
      }
    },
  },
};
</script>
