# webPath_API Project (API1 -> API2 via Docker Compose)

## 🔧 วิธีรัน

```bash
docker-compose up --build

# webPath_API Project Hello World (Docker Compose)

ระบบนี้ประกอบด้วย 2 API:
- **API1** (port 5000): รับ request และส่งต่อให้ API2
- **API2** (port 6000): ตอบกลับข้อความ

## 🔧 วิธีใช้งาน

### 1. ติดตั้ง Docker และ Docker Compose
- [Download Docker](https://docs.docker.com/get-docker/)

### 2. Clone โปรเจกต์
```bash
git clone https://github.com/username/multi-api-project.git
cd webPath_API
