const express = require("express");
const pool = require("./db");

const app = express();
const PORT = 8080;

// cors
const cors = require("cors");
app.use(cors());

// morgan
const morgan = require("morgan");
app.use(morgan("dev"));

// multer(이미지 업로드용)
const path = require("path");
const multer = require("multer");
const { takeCoverage } = require("v8");

// 업로드
const upload = multer({
  storage: multer.diskStorage({
    destination: (req, file, done) => {
      done(null, "public/");
    },

    // 업로드 할 경우 파일 이름 형식
    filename: (req, file, done) => {
      // 해당 파일의 확장자만 가져옴
      const ext = path.extname(file.originalname);

      // 확장자를 제외한 파일 이름
      // const fileNameExceptExt = path.basename(file.originalname);
      const fileNameExceptExt = path.parse(file.originalname).name;

      // 파일이름 + 현재 시간 + 확장자
      // ex) hello.jpg -> hello182902345.jpg
      // 저장할 파일 이름 형식
      const saveFileName = fileNameExceptExt + Date.now() + ext;
      done(null, saveFileName);

      /*
            파일 이름을 이렇게 하는 이유:
            원래 존재하는 파일의 이름과 같은 파일을 업로드하는 경우
            원래 파일이 업로드 파일로 덧씌워질 수 있기 때문
            또한 DB에 파일의 주소를 올릴 거임
            */
    },
  }),
});

// 정적 파일 서비스
app.use("/public", express.static("public"));

/*
파일 업로드 -> DB에 파일 경로 저장
-> front에서 경로에 대해 요청해서 불러오기
(public/image1.jpg) -> localhost:8080/public/image1.jpg
*/

// body 데이터 받아오기
app.use(express.json());

/* list
GET /api/list
GET /api/list/:id
POST /api/list
DELETE /api/list/:id
*/

// GET /api/list
// 전체 분실물 조회
app.get("/api/list", async (req, res) => {
  try {
    const data = await pool.query("SELECT * FROM LIST");
    return res.json(data[0]);
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "전체 메뉴 목록 조회에 실패하였습니다.",
    });
  }
});

// GET /api/list/:id
// 한가지 분실물 조회
app.get("/api/list/:id", async (req, res) => {
  try {
    const id = req.params.id;
    // DB의 id를 검색하는 거임
    const data = await pool.query("SELECT * FROM LIST WHERE id = ?", [id]);

    return res.json(data[0]);
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "분실물 조회에 실패하였습니다.",
    });
  }
});

// POST /api/list
app.post("/api/list", upload.single("file"), async (req, res) => {
  try {
    console.log(req.file);
    // 파일 경로
    const file_path = req.file.path.replace(/\\/g, "/");
    console.log(req.body);
    console.log(file_path);

    // 파일 업로드
    const { date, time, name, place, detail } = req.body;

    const data = await pool.query(
      `
        INSERT INTO LIST (date, time, name, place, detail, image)
        VALUES (?,?,?,?,?,?)
        `,
      [date, time, name, place, detail, file_path]
    );

    return res.json({
      success: true,
      message: "분실물 등록에 성공하였습니다.",
    });
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "분실물 등록에 실패하였습니다.",
    });
  }
});

// DELETE /api/list/:id
// 메뉴 삭제
app.delete("/api/list/:id", async (req, res) => {
  try {
    const data = await pool.query("DELETE FROM LIST WHERE id = ?", [
      req.params.id,
    ]);

    return res.json({
      success: true,
      message: "메뉴 삭제에 성공하였습니다.",
    });
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "메뉴 삭제에 실패하였습니다.",
    });
  }
});

// command

// POST /api/find
app.post("/api/find", async (req, res) => {
  try {
    console.log(req.body);
    // DB 업로드
    const { date, time, name, place } = req.body;

    const data = await pool.query(
      `
        INSERT INTO COMMAND (date, time, name, place, is_done)
        VALUES (?,?,?,?,?)
        `,
      [date, time, name, place, 0]
    );

    return res.json({
      success: true,
      message: "RC카가 출발했습니다.",
    });
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "RC카가 출발하지 못했습니다.",
    });
  }
});

// POST /api/complete
app.post("/api/complete", async (req, res) => {
  try {
    // DB 업로드
    const { date, time, name, place } = req.body;

    const data = await pool.query(
      `
        INSERT INTO COMMAND (date, time, name, place, is_done)
        VALUES (?,?,?,?,?)
        `,
      [date, time, name, place, 1]
    );

    return res.json({
      success: true,
      message: "수령이 완료되었습니다.",
    });
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "수령 처리가 되지 않았습니다.",
    });
  }
});

// history

// GET /api/history
app.get("/api/history", async (req, res) => {
  try {
    const data = await pool.query("SELECT * FROM HISTORY");
    return res.json(data[0]);
  } catch (error) {
    console.log(error);
    return res.json({
      success: false,
      massage: "전체 내역 조회에 실패하였습니다.",
    });
  }
});

app.listen(PORT, () => console.log("this server listening on " + PORT));
