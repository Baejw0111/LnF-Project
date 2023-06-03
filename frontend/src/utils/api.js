import axios from "axios";

// const DOMAIN = "http://43.201.65.87:8080";
const DOMAIN = "http://localhost:8080";

const request = axios.create({
  baseURL: `${DOMAIN}/api`,
});

export const api = {
  list: {
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
      // for (const [key, value] of formData.entries()) {
      //   console.log(`${key}: ${value}`);
      // }
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
