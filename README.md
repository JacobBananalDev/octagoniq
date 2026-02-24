# OctagonIQ

OctagonIQ is a production-grade MMA analytics backend platform engineered to manage fighter data, fight history, and predictive intelligence through a scalable API architecture.

The project is built to demonstrate real-world backend engineering principles, including relational database design, containerized development, and cloud-ready infrastructure planning.

---

## 🚀 Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Docker (integration in progress)
- Planned: AWS + Terraform

---

## 🧠 Vision

OctagonIQ will evolve into a full MMA analytics engine capable of:

- Managing structured fighter data
- Modeling fight events and matchups
- Storing performance statistics
- Powering predictive fight analysis
- Deploying to cloud infrastructure using Infrastructure as Code

---

## 🏗 Architecture (Phase 1)

Client → FastAPI → SQLAlchemy → PostgreSQL

The backend is being developed using clean modular architecture with separated layers for:

- API routes
- Database models
- Validation schemas
- Configuration management

---

## 🔧 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/octagoniq.git
cd octagoniq/backend
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
```
### 3. Activate the Virtual Environment

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Run the API
```bash
uvicorn app.main:app --reload
```
Visit:

API root: http://localhost:8000

Swagger docs: http://localhost:8000/docs

## 📍 Roadmap

 FastAPI foundation

 PostgreSQL integration

 Relational schema modeling (Fighters, Events, Fights)

 Docker containerization

 Prediction engine layer

 AWS deployment via Terraform

 Frontend analytics dashboard

## 📌 Status

🚧 Backend foundation in progress
Actively expanding into database modeling and infrastructure design.