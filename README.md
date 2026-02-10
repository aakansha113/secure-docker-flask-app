# 🔐 Secure Docker Flask App

![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-WebApp-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Security](https://img.shields.io/badge/Security-Non--Root-green)
![Compose](https://img.shields.io/badge/Docker--Compose-Orchestration-blue)

A production-style secure multi-container Docker project demonstrating best practices including multi-stage builds, non-root containers, environment-based configuration, persistent volumes, and custom networking.

---

# 🏗️ Architecture Diagram

```
                +-------------------+
                |      Browser      |
                |  http://localhost |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   Flask App       |
                |  (Non-root user)  |
                |  Port: 5000       |
                +---------+---------+
                          |
                          |  Docker Network (appnet)
                          |
                          v
                +-------------------+
                |      MySQL        |
                |  Persistent Data  |
                |  Named Volume     |
                +-------------------+
```

---

# 📦 Project Structure

```
secure-docker-project/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .env
├── docker-compose.yml
└── README.md
```

---

# 🚀 Features

- 🔥 Multi-stage Docker build (optimized image)
- 🔐 Runs container as non-root user
- 🗄️ MySQL with named volume for persistence
- 🌐 Custom Docker network
- 🔑 Environment variable based secret handling
- 🧱 Minimal Python slim base image
- ⚙️ Docker Compose orchestration

---

# 🔒 Security Best Practices Used

| Practice | Implementation |
|-----------|---------------|
| Non-root container | `USER appuser` |
| Multi-stage build | Separate builder & runtime |
| No hardcoded secrets | `.env` file |
| Data persistence | Named Docker volume |
| Service isolation | Custom Docker network |
| Minimal base image | python:3.9-slim |

---

# 🛠️ How To Run

## 1️⃣ Clone Repository

```bash
git clone 
cd secure-docker-project
```

---

## 2️⃣ Create `.env` File

```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=testdb

DB_HOST=db
DB_USER=root
DB_PASSWORD=root
DB_NAME=testdb
```

---

## 3️⃣ Build & Start Containers

```bash
docker compose up -d --build
```

---

## 4️⃣ Verify Running Containers

```bash
docker ps
```

---

## 5️⃣ Access Application

Open in browser:

```
http://localhost:5000
```

Or via terminal:

```bash
curl http://localhost:5000
```

---

# 🧠 What This Project Demonstrates

- Container lifecycle management
- Multi-container orchestration
- Service-to-service communication
- Secure image building
- Docker networking
- Volume-based database persistence

---

# 📊 Docker Components Used

| Component | Purpose |
|------------|----------|
| Dockerfile | Multi-stage secure build |
| Docker Compose | Service orchestration |
| Volume | MySQL data persistence |
| Network | Service communication |
| ENV file | Secure config management |

---

# 📌 Useful Commands

View logs:

```bash
docker compose logs
```

Stop services:

```bash
docker compose down
```

Remove volumes:

```bash
docker compose down -v
```

Rebuild without cache:

```bash
docker compose build --no-cache
```
👩‍💻 Built as part of hands-on DevOps learning journey.

---

👩‍💻 Built as part of hands-on DevOps learning journey.
👩‍💻 Built as part of hands-on DevOps learning jou
