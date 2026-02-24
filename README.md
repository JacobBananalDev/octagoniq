# 🥊 OctagonIQ

OctagonIQ is a production-grade MMA analytics backend platform engineered to manage fighter data, fight history, and predictive intelligence through a scalable API architecture.

This project demonstrates real-world backend engineering principles, including relational database modeling, containerized development, and cloud-ready infrastructure planning.

---

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.133.0-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-Planned-623CE4?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Planned-232F3E?logo=amazonaws&logoColor=white)

---

## 🏗 System Architecture


Client
↓
FastAPI (Uvicorn)
↓
SQLAlchemy ORM
↓
PostgreSQL (Docker Container)


The backend follows clean modular architecture:

- `routes/` → API endpoints  
- `models/` → Database tables  
- `schemas/` → Request/response validation  
- `database.py` → Database engine & session management  
- `Dockerfile` → Backend container configuration  
- `docker-compose.yml` → Multi-container orchestration  

---

## 🐳 Running with Docker (Recommended)

OctagonIQ runs fully containerized using Docker Compose.

### 1️⃣ Build and Start Services

From the project root:

```bash
docker compose up --build
```

This will:

Build the FastAPI backend container

Pull the PostgreSQL image

Start both containers

Connect them via an internal Docker network

### 2️⃣ Access the API

API root:

http://localhost:8000

Interactive Swagger documentation:

http://localhost:8000/docs
### 3️⃣ Stop Services
```bash
docker compose down
```

Database data is persisted using a Docker volume.

## 🔧 Local Development (Without Docker)

If you prefer running the backend locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/octagoniq.git
cd octagoniq/backend
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
### 3️⃣ Activate the Virtual Environment

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Run the API
```bash
uvicorn app.main:app --reload
```
## 🧠 Vision

OctagonIQ will evolve into a full MMA analytics engine capable of:

Managing structured fighter data

Modeling fight events and matchups

Storing advanced performance statistics

Powering predictive fight analysis

Deploying to AWS using Infrastructure as Code (Terraform)

Supporting a future frontend analytics dashboard

## 📍 Roadmap

 FastAPI foundation

 PostgreSQL containerization

 Docker multi-service architecture

 Relational schema modeling (Fighters, Events, Fights)

 Prediction engine layer

 AWS deployment via Terraform

 Frontend analytics dashboard

## 📌 Current Status

🚧 Backend core infrastructure complete.
Now expanding into relational modeling and domain implementation.

## 📈 Future Expansion

JWT authentication

Role-based access control

ML-powered prediction service

CI/CD with GitHub Actions

AWS ECS + RDS deployment

Infrastructure automation via Terraform

## 👨‍💻 Author

Built as a backend engineering portfolio project to demonstrate scalable API architecture, database modeling, and cloud-ready system design.