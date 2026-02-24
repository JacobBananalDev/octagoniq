🥊 OctagonIQ

OctagonIQ is a production-grade MMA analytics backend platform engineered to manage fighter data, fight history, and predictive intelligence through a scalable API architecture.

This project demonstrates real-world backend engineering principles, including relational database modeling, containerized development, and cloud-ready infrastructure planning.

🚀 Tech Stack

Python 3.12

FastAPI

SQLAlchemy 2.0

PostgreSQL

Docker + Docker Compose

Planned: AWS + Terraform

🏗 System Architecture
Client
   ↓
FastAPI (Uvicorn)
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL (Docker Container)

The backend is structured using clean modular separation:

routes/ → API endpoints

models/ → Database tables

schemas/ → Request/response validation

database.py → Database engine & session management

Dockerfile → Backend container configuration

docker-compose.yml → Multi-container orchestration

🐳 Running with Docker (Recommended)

OctagonIQ runs fully containerized using Docker Compose.

1️⃣ Build and Start Services

From the project root:

docker compose up --build

This will:

Build the FastAPI backend container

Pull the PostgreSQL image

Start both containers

Connect them via an internal Docker network

2️⃣ Access the API

API root:

http://localhost:8000

Interactive Swagger documentation:

http://localhost:8000/docs
3️⃣ Stop Services
docker compose down

Database data is persisted using a Docker volume.

🔧 Local Development (Without Docker)

If you prefer running the backend locally:

1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/octagoniq.git
cd octagoniq/backend
2️⃣ Create a Virtual Environment
python -m venv venv
3️⃣ Activate the Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Run the API
uvicorn app.main:app --reload
🧠 Vision

OctagonIQ will evolve into a full MMA analytics engine capable of:

Managing structured fighter data

Modeling fight events and matchups

Storing advanced performance statistics

Powering predictive fight analysis

Deploying to AWS using Infrastructure as Code (Terraform)

Supporting a future frontend analytics dashboard

📍 Roadmap

 FastAPI foundation

 PostgreSQL containerization

 Docker multi-service architecture

 Relational schema modeling (Fighters, Events, Fights)

 Prediction engine layer

 AWS deployment via Terraform

 Frontend analytics dashboard

📌 Current Status

🚧 Backend core infrastructure complete
Now expanding into relational modeling and domain implementation.