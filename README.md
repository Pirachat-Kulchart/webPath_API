# webPath_API Project (API1 → API2 via Docker Compose)

## ระบบนี้ประกอบด้วย 2 API

- **API1** (port 5000): รับ request และส่งต่อให้ API2
- **API2** (port 6000): ตอบกลับข้อความ

**ตัวอย่างการใช้งาน:**

- <http://localhost:5000/hello>
- <http://localhost:6000/world>

## 🔧 วิธีใช้งาน

### 1. ติดตั้ง Docker และ Docker Compose

- [Download Docker](https://docs.docker.com/get-docker/)

### 2. Clone โปรเจกต์

```bash
git clone https://github.com/pirac-0/webPath_API.git
cd webPath_API
```

### 3. สั่งรันโปรเจกต์ด้วย Docker Compose

```bash
docker-compose up --build
```

### 4. ทดสอบ API

- เปิดเบราว์เซอร์หรือใช้ `curl` เพื่อทดสอบ endpoint:
  - `http://localhost:5000/hello`
  - `http://localhost:6000/world`

---

**หมายเหตุ:**  

- ตรวจสอบว่าไม่มีโปรแกรมอื่นใช้ port 5000 หรือ 6000 อยู่ก่อนแล้ว
- หากต้องการหยุดการทำงาน กด `Ctrl+C` ใน terminal หรือใช้ `docker-compose down`
