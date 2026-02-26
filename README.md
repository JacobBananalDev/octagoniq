# 🥊 OctagonIQ

OctagonIQ is a production-grade MMA analytics backend engineered with modern Python backend architecture. It manages fighters, events, fights, and authentication through a secure, containerized API designed for scalability and cloud deployment.

This project demonstrates:

* Clean modular backend architecture

* JWT authentication & role-based access control

* Relational database modeling with SQLAlchemy

* Containerized development with Docker

* Automated testing with Pytest

* Continuous Integration via GitHub Actions

* Cloud-ready infrastructure planning (AWS + Terraform)

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

[ Client ]
     ↓
[ FastAPI Application Layer ]
     ↓
[ Service Layer ]
     ↓
[ SQLAlchemy ORM ]
     ↓
[ PostgreSQL Database ]

## 📂 Project Structure
OCTAGONIQ/
│
├── .github/                 # GitHub Actions workflows
│
├── backend/
│   ├── app/
│   │   ├── routes/          # API endpoints
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── core/            # Security, settings, dependencies
│   │   ├── services/        # Business logic layer
│   │   ├── database.py      # Engine & session management
│   │   └── main.py          # FastAPI application instance
│   │
│   ├── alembic/             # Database migrations
│   ├── tests/               # Pytest integration tests
│   ├── Dockerfile
│   ├── alembic.ini
│   ├── pyproject.toml
│   └── requirements.txt
│
├── docker-compose.yml
├── docs/
└── README.md

##  🔐 Authentication & Authorization

OctagonIQ implements:

OAuth2 password flow

JWT access tokens

Password hashing with bcrypt

Role-based access control (admin / user)

Dependency-based authorization guards

Protected endpoints (e.g., creating fighters) require admin privileges.

## 🧪 Testing & CI

The backend includes:

Pytest integration tests

Isolated test database

Schema reset before each test

Dependency override for database sessions

GitHub Actions CI pipeline

CI validates:

Authentication flows

Role-based access control

Protected endpoints

Pagination logic

Health check endpoints 

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
## 🧠 Domain Model

Current relational entities:

* Users

* Fighters

* Fights

* Events

Designed to support:

* Historical performance tracking

* Matchup modeling

* Statistical aggregation

* Future predictive intelligence engine

## 📍 Roadmap

✅ FastAPI foundation

✅ PostgreSQL containerization

✅ Docker multi-service setup

✅ JWT authentication

✅ Role-based access control

✅ Pytest test suite

✅ CI with GitHub Actions

⏳ Advanced fight analytics

⏳ AWS deployment

⏳ Terraform infrastructure automation

⏳ Frontend analytics dashboard

## ☁️ Cloud Deployment (Planned)

Upcoming infrastructure:

* AWS EC2

* AWS RDS (PostgreSQL)

* Dockerized backend

* Terraform-managed infrastructure

* IAM-based security model

## 📈 Future Enhancements

Global exception handling

Structured logging middleware

Request ID tracing

Rate limiting

Async SQLAlchemy layer

ELO ranking algorithm

ML-powered fight prediction engine

## 👨‍💻 Author

OctagonIQ is a backend engineering portfolio project designed to demonstrate:

Secure API architecture

Clean separation of concerns

Database modeling

Containerized development

Automated testing

CI/CD integration

Cloud deployment readiness
