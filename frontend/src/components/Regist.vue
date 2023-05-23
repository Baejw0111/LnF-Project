<template>
  <div class="regist">
    <div class="router-header">
      <div>분실물 등록</div>
    </div>
    <div class="router-body">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="name" label="분실물명" label-for="name-input">
          <b-form-input
            id="name-input"
            v-model="form.name"
            type="name"
            placeholder="분실물명을 입력해주세요"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-group
          id="location"
          label="분실물 발견 위치"
          label-for="location-input"
        >
          <b-form-input
            id="location-input"
            v-model="form.location"
            type="location"
            placeholder="분실물 발견 위치를 입력해주세요"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <b-form-group id="time" label="신고 시각" label-for="time-input">
          <b-form-input
            id="time-input"
            v-model="form.time"
            type="time"
            placeholder="분실물 신고 시각"
            required
          ></b-form-input>
        </b-form-group>
        <br />

        <div style="height: 180px"></div>

        <b-form-file
          v-model="file1"
          :state="Boolean(file1)"
          placeholder="분실물 이미지 파일을 넣어주세요"
          drop-placeholder="이미지 파일을 드롭"
          required
        ></b-form-file>
        <div class="mt-3">Selected file: {{ file1 ? file1.name : "" }}</div>
        <br />

        <div class="button-container float-right">
          <b-button type="submit" variant="primary">등록</b-button>
        </div>
      </b-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: "",
        location: "",
        time: "",
        img: [],
      },
      foods: [
        { text: "Select One", value: null },
        "Carrots",
        "Beans",
        "Tomatoes",
        "Corn",
      ],
      show: true,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
