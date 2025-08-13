from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI(title="Chatbot API", version="1.0.0")

# Enable CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Question(BaseModel):
    id: str
    name: str
    answer: str

class Job(BaseModel):
    id: str
    name: str
    questions: List[Question]

class Client(BaseModel):
    id: str
    name: str
    questions: List[Question]

# Static data
data = {
    "jobs": [
        {
            "id": "J001",
            "name": "Frontend Developer",
            "questions": [
                {"id": "Q001", "name": "What is your experience in Angular?", "answer": "I have extensive experience with Angular, including Angular 16+ with standalone components, reactive forms, and state management. I've built complex applications with routing, HTTP interceptors, and custom directives."},
                {"id": "Q002", "name": "Have you worked with REST APIs?", "answer": "Yes, I have extensive experience working with REST APIs. I've integrated with various backend services, handled authentication, implemented error handling, and used HTTP interceptors for request/response processing."},
                {"id": "Q003", "name": "What CSS frameworks are you familiar with?", "answer": "I'm proficient with Bootstrap 5, Tailwind CSS, Material Design, and custom CSS. I can create responsive designs, implement animations, and ensure cross-browser compatibility."}
            ]
        },
        {
            "id": "J002",
            "name": "Backend Developer",
            "questions": [
                {"id": "Q004", "name": "What Python frameworks do you know?", "answer": "I'm experienced with FastAPI, Django, Flask, and Pyramid. I can build REST APIs, implement authentication, work with databases, and deploy applications using Docker and cloud services."},
                {"id": "Q005", "name": "Have you worked with databases?", "answer": "Yes, I have experience with PostgreSQL, MySQL, MongoDB, and Redis. I can design schemas, write complex queries, implement ORMs, and optimize database performance."},
                {"id": "Q006", "name": "What's your experience with APIs?", "answer": "I've designed and built RESTful APIs, GraphQL endpoints, and microservices. I implement proper error handling, validation, documentation, and testing strategies."}
            ]
        },
        {
            "id": "J003",
            "name": "Full Stack Developer",
            "questions": [
                {"id": "Q007", "name": "Can you work on both frontend and backend?", "answer": "Absolutely! I'm a full-stack developer who can work across the entire technology stack. I can build complete applications from database design to user interface, ensuring seamless integration between frontend and backend."},
                {"id": "Q008", "name": "What's your preferred tech stack?", "answer": "My preferred stack includes Angular/React for frontend, FastAPI/Django for backend, PostgreSQL for database, and Docker for deployment. I'm also comfortable with Node.js, TypeScript, and various cloud platforms."},
                {"id": "Q009", "name": "How do you handle deployment?", "answer": "I use CI/CD pipelines with GitHub Actions, Docker containers, and cloud platforms like AWS, Azure, or Google Cloud. I implement automated testing, monitoring, and rollback strategies for reliable deployments."}
            ]
        }
    ],
    "clients": [
        {
            "id": "C001",
            "name": "ABC Corp",
            "questions": [
                {"id": "Q101", "name": "What services do you provide to ABC Corp?", "answer": "We provide comprehensive web development services including custom web applications, e-commerce solutions, API development, and ongoing maintenance. Our team handles everything from initial design to deployment and support."},
                {"id": "Q102", "name": "What's the project timeline?", "answer": "Typical project timelines range from 8-16 weeks depending on complexity. We follow agile methodologies with 2-week sprints, providing regular updates and demos throughout the development process."},
                {"id": "Q103", "name": "What's the budget range?", "answer": "Our projects typically range from $15,000 to $100,000+ depending on scope and complexity. We provide detailed proposals with transparent pricing and can work within various budget constraints."}
            ]
        },
        {
            "id": "C002",
            "name": "XYZ Industries",
            "questions": [
                {"id": "Q201", "name": "Can you handle enterprise solutions?", "answer": "Yes, we specialize in enterprise-grade solutions with scalable architectures, robust security, and high availability. We've successfully delivered solutions for Fortune 500 companies with complex requirements."},
                {"id": "Q202", "name": "What's your support policy?", "answer": "We offer 24/7 support with guaranteed response times, dedicated support teams, and comprehensive SLAs. Our support includes monitoring, maintenance, updates, and emergency response procedures."},
                {"id": "Q203", "name": "Do you provide maintenance?", "answer": "Absolutely! We provide ongoing maintenance including security updates, performance optimization, bug fixes, and feature enhancements. We offer various maintenance packages to suit different needs and budgets."}
            ]
        },
        {
            "id": "C003",
            "name": "TechStart Inc",
            "questions": [
                {"id": "Q301", "name": "What's your startup pricing?", "answer": "We offer special startup pricing with flexible payment terms and equity options. We understand startup constraints and can work with limited budgets while delivering high-quality solutions."},
                {"id": "Q302", "name": "Can you scale with our growth?", "answer": "Yes! We design solutions with scalability in mind from day one. Our architectures can handle growth from startup to enterprise, with modular designs that allow for easy expansion and feature additions."},
                {"id": "Q303", "name": "What's your development process?", "answer": "We use agile methodologies with rapid prototyping, iterative development, and continuous feedback. Our process includes regular demos, user testing, and the ability to pivot quickly based on market feedback."}
            ]
        }
    ]
}

@app.get("/")
async def root():
    return {"message": "Chatbot API is running"}

@app.get("/jobs", response_model=List[dict])
async def get_jobs():
    """Get all jobs with id and name only"""
    return [{"id": job["id"], "name": job["name"]} for job in data["jobs"]]

@app.get("/clients", response_model=List[dict])
async def get_clients():
    """Get all clients with id and name only"""
    return [{"id": client["id"], "name": client["name"]} for client in data["clients"]]

@app.get("/jobs/{job_id}/questions", response_model=List[Question])
async def get_job_questions(job_id: str):
    """Get questions for a specific job"""
    job = next((job for job in data["jobs"] if job["id"] == job_id), None)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job["questions"]

@app.get("/clients/{client_id}/questions", response_model=List[Question])
async def get_client_questions(client_id: str):
    """Get questions for a specific client"""
    client = next((client for client in data["clients"] if client["id"] == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client["questions"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

