
# Distributed Task Queue System

A production-oriented **Distributed Task Queue** built with **FastAPI, Celery, Redis, and Docker**.
This project demonstrates clean architecture, asynchronous processing, fault tolerance,
and observability using Flower.

---

## 🚀 Features

- Modular architecture (API Service & Worker Service separation)
- Asynchronous task processing with Celery
- Redis as Message Broker & Result Backend
- Automatic retries with exponential backoff
- Task monitoring with Flower
- Dockerized environment using docker-compose
- API documentation via Swagger (FastAPI)
- Unit testing with pytest

---

## 🏗️ Architecture Overview

Client
│
▼
FastAPI (API Service)
│
▼
Redis (Message Broker)
│
▼
Celery Workers
│
▼
Redis (Result Backend)


---

## 🧰 Tech Stack

- Python 3.11
- FastAPI
- Celery
- Redis
- Docker & Docker Compose
- Flower
- Pytest

---

## 📂 Project Structure

distributed-task-queue/
│
├── docker-compose.yml
├── README.md
│
├── api/
│ ├── Dockerfile
│ ├── main.py
│ ├── core/
│ │ ├── config.py
│ │ └── celery_app.py
│ ├── routes/
│ │ └── tasks.py
│ └── schemas/
│
├── worker/
│ ├── Dockerfile
│ ├── celery_worker.py
│ └── tasks/
│ └── heavy_task.py
│
└── tests/
└── test_task_enqueue.py


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/distributed-task-queue.git
cd distributed-task-queue

2️⃣ Build & start all services
docker-compose up --build

🌐 Services URLs
| Service        | URL                                                      |
| -------------- | -------------------------------------------------------- |
| FastAPI Docs   | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Flower Monitor | [http://localhost:5555](http://localhost:5555)           |
| Redis          | redis://localhost:6379                                   |

📬 API Usage
Submit a Task

POST /tasks/submit

Request Body
{
  "data": "sample payload"
}

Response
{
  "task_id": "c2a9c7...",
  "status": "submitted"
}
🌸 Monitoring with Flower

Flower provides a real-time dashboard to monitor:

Task states (PENDING, STARTED, SUCCESS, FAILURE)

Retries and failures

Worker health

Open:
http://localhost:5555
🧪 Running Tests
pytest

🎯 Why This Project?

This project is designed to showcase:

Distributed system design

Asynchronous architecture

Fault tolerance strategies

Observability & monitoring

Production-ready structure

📄 License

MIT License
