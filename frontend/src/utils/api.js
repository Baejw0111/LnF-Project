import axios from "axios";

// const DOMAIN = "http://13.209.64.54:8080";
const DOMAIN = "http://localhost:8080";

const request = axios.create({
  baseURL: `${DOMAIN}/api`,
});

export const api = {
  list: {
    // http://13.209.64.54:8080/api/list 요청과 같다.
    findAll: () => request.get("/list"),
    findOne: (id) => request.get(`/list/${id}`),

    create: (date, time, name, place, detail, file) => {
      const formData = new FormData();
      formData.append("date", date);
      formData.append("time", time);
      formData.append("name", name);
      formData.append("place", place);
      formData.append("detail", detail);
      formData.append("file", file);
      return request.post(`/list`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    },
    // 메뉴 삭제
    delete: (id) => request.delete(`/list/${id}`),
  },

  command: {
    find: (date, time, name, place) => {
      const formData = new FormData();
      formData.append("date", date);
      formData.append("time", time);
      formData.append("name", name);
      formData.append("place", place);
      console.log(formData);
      return request.post(`/find`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    },

    complete: (date, time, name, place) => {
      const formData = new FormData();
      formData.append("date", date);
      formData.append("time", time);
      formData.append("name", name);
      formData.append("place", place);
      return request.post(`/complete`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    },
  },

  history: {
    // 내역 조회
    findAll: () => request.get("/history"),
  },
};
