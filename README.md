# 🎓 Student Management System

A simple full-stack application for managing student records such as **student name, course, and course fee**.

The application supports complete **CRUD operations**:

- ➕ Add Student
- 📋 View Students
- 🔍 Search Students
- ✏️ Update Student
- 🗑️ Delete Student

Built with **Python, FastAPI, Streamlit, MySQL, Docker, Git, GitHub, and Cloud Deployment**.

---

## 🌐 Live Project

| Resource | Link |
|---|---|
| 🚀 **Live Demo** | [Open Application](https://student-management-system-jagan.streamlit.app) |
| ⚡ **Backend API** | [Open API](https://student-management-system-uxo9.onrender.com) |
| 📖 **API Documentation** | [Open Swagger Docs](https://student-management-system-uxo9.onrender.com/docs) |
| 💻 **Source Code** | [View GitHub Repository](https://github.com/jagankumarpanda/STUDENT-MANAGEMENT-SYSTEM) |

---

# 📌 Project Overview

The **Student Management System** is a full-stack CRUD application designed to manage basic student information.

A user can enter:

- Student Name
- Course
- Course Fee

The application follows a simple architecture:

```text
User
  ↓
Streamlit UI
  ↓
FastAPI REST API
  ↓
MySQL Database

In simple words
Streamlit provides the user interface, FastAPI handles the REST APIs, and MySQL stores the student data.

The FastAPI backend is containerized using Docker and deployed on Render, while the MySQL database is hosted on Aiven Cloud.
✨ Features
Student Management
- ➕ Add new students
- 📋 View all students
- 🔍 Search students by name or course
- ✏️ Update student information
- 🗑️ Delete student records
Backend
- ⚡ FastAPI REST API
- 🔄 Complete CRUD operations
- ✅ Request validation using Pydantic
- 📖 Automatic Swagger API documentation
- 🔐 Environment-based database configuration
- 🔒 SSL connection to cloud MySQL
Deployment
- 🐳 Dockerized FastAPI backend
- ☁️ Cloud-hosted backend
- ☁️ Cloud-hosted MySQL database
- 🌐 Public frontend
🏗️ Architecture
Application Architecture
                    👤 USER
                      │
                      ▼
              ┌───────────────┐
              │  Streamlit UI │
              │   Frontend    │
              └───────┬───────┘
                      │
                  HTTP / REST
                      │
                      ▼
              ┌───────────────┐
              │    FastAPI    │
              │    Backend    │
              └───────┬───────┘
                      │
                  SQL Queries
                      │
                      ▼
              ┌───────────────┐
              │     MySQL     │
              │    Database   │
              └───────────────┘

Request Flow
Streamlit
    ↓
HTTP Request
    ↓
FastAPI
    ↓
Database Layer
    ↓
MySQL
    ↓
Response
    ↓
Streamlit

☁️ Production Architecture
The deployed application uses separate services for the frontend, backend, and database.
                         🌐 USER
                            │
                            ▼
                ┌─────────────────────┐
                │   Streamlit Cloud   │
                │      Frontend       │
                └──────────┬──────────┘
                           │
                      HTTPS / REST
                           │
                           ▼
                ┌─────────────────────┐
                │       Render        │
                │                     │
                │   Docker Container  │
                │       FastAPI       │
                └──────────┬──────────┘
                           │
                        MySQL + SSL
                           │
                           ▼
                ┌─────────────────────┐
                │    Aiven Cloud      │
                │       MySQL         │
                └─────────────────────┘

Services
Service	Purpose
Streamlit Cloud	Hosts the frontend
Render	Hosts the FastAPI backend
Docker	Containerizes the backend
Aiven	Hosts the MySQL database
GitHub	Stores the source code


Easy Way to Remember
Streamlit → Frontend
FastAPI   → Backend / API
MySQL     → Database
Docker    → Container
Render    → Backend Hosting
Aiven     → Database Hosting
GitHub    → Source Code

🛠️ Technology Stack
Technology	Purpose
🐍 Python	Application development
⚡ FastAPI	REST API development
🎨 Streamlit	Web interface
🗄️ MySQL	Database
✅ Pydantic	Data validation
🚀 Uvicorn	FastAPI server
🔗 Requests	API communication
📊 Pandas	Data processing and display
🐳 Docker	Backend containerization
🔧 Git	Version control
🐙 GitHub	Source code hosting
☁️ Render	Backend deployment
☁️ Aiven	Cloud MySQL
🌐 Streamlit Cloud	Frontend deployment


📁 Project Structure
STUDENT-MANAGEMENT-SYSTEM/
│
├── STUDENT_CRUD_API/
│   ├── main.py
│   ├── db.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── STUDENT_CRUD_UI/
│   ├── main.py
│   └── requirements.txt
│
├── .gitignore
├── README.md
└── requirements.txt

📂 Main Components
⚡ FastAPI Backend
Located inside:
STUDENT_CRUD_API/

main.py
Contains:
- FastAPI application
- Student data model
- API routes
- Request validation
- CRUD endpoints
db.py
Contains the database layer responsible for:
- Creating the student table
- Inserting students
- Reading students
- Updating students
- Deleting students
🎨 Streamlit Frontend
Located inside:
STUDENT_CRUD_UI/

The Streamlit application provides:
- 📋 View Students
- ➕ Add Student
- 🔍 Search Students
- ✏️ Update Student
- 🗑️ Delete Student
🔄 CRUD Operations
CRUD represents the four basic data operations.
Operation	HTTP Method	Project Example
Create	POST	Add Student
Read	GET	View Students
Update	PUT	Edit Student
Delete	DELETE	Remove Student


Easy Way to Remember
Create → Add
Read   → View
Update → Edit
Delete → Remove

🔌 REST API
The FastAPI backend provides the following endpoints:
Method	Endpoint	Description
GET	/	Check API status
POST	/api/student	Create a student
GET	/api/students	Get all students
GET	/api/students/{id}	Get student by ID
PUT	/api/students/{id}	Update student
DELETE	/api/students/{id}	Delete student


📖 Interactive API Documentation
FastAPI automatically provides Swagger documentation.
👉 Open Swagger API Docs
🧪 Example API Request
Create Student
POST /api/student

Request Body
{
  "name": "Rahul",
  "course": "Python",
  "fee": 5000
}

Request Flow
Streamlit
    ↓
HTTP POST
    ↓
FastAPI
    ↓
Pydantic Validation
    ↓
Database Layer
    ↓
MySQL
    ↓
Response
    ↓
Streamlit

🔍 Data Validation
The project uses Pydantic with FastAPI to validate incoming API data.
Current Validation Rules
Student Name → 3–15 characters
Course Name  → 3–15 characters
Course Fee   → Greater than 0

This helps ensure that invalid data is rejected before it reaches the database.
Interview Answer
Pydantic is used to validate and structure the data received by my FastAPI endpoints.

🗄️ Database
The application uses MySQL to store student information.
Students Table
STUDENTS
│
├── ID
├── NAME
├── COURSE
└── FEE

Example
ID	Name	Course	Fee
1	Rahul	Python	₹5,000
2	Priya	Java	₹6,000


The ID column is the primary key and uniquely identifies each student.
🔐 Security & Configuration
Database credentials are stored using environment variables instead of being written directly into the source code.
The application uses:
DB_HOST
DB_PORT
DB_USER
DB_PASSWORD
DB_NAME

The .env file is excluded from Git using .gitignore.
The cloud database connection uses SSL for secure communication.
Important Practice
Never hardcode passwords, API keys, or other sensitive credentials in source code.

🐳 Docker
The FastAPI backend is containerized using Docker.
Why Docker?
Docker packages the application together with its required dependencies.
Application
     +
Dependencies
     +
Python Runtime
     ↓
Docker Image
     ↓
Docker Container

This provides a consistent environment for running the backend.
Build Docker Image
cd STUDENT_CRUD_API

docker build -t student-crud-api .

Run Docker Container
docker run --env-file .env -p 8000:8000 student-crud-api

Backend:
http://localhost:8000

Swagger:
http://localhost:8000/docs

💻 Run Locally
1. Clone the Repository
git clone https://github.com/jagankumarpanda/STUDENT-MANAGEMENT-SYSTEM.git

cd STUDENT-MANAGEMENT-SYSTEM

2. Run the FastAPI Backend
Go to the backend directory:
cd STUDENT_CRUD_API

Install dependencies:
pip install -r requirements.txt

Start FastAPI:
uvicorn main:app --reload

Backend:
http://localhost:8000

API Documentation:
http://localhost:8000/docs

3. Run the Streamlit Frontend
Open another terminal.
Go to:
cd STUDENT_CRUD_UI

Install dependencies:
pip install -r requirements.txt

Start Streamlit:
streamlit run main.py

Frontend:
http://localhost:8501

🔄 How the Application Works
Let's see what happens when a user adds a student.
1. User enters student details
            ↓
2. Streamlit collects the data
            ↓
3. Streamlit sends a POST request
            ↓
4. FastAPI receives the request
            ↓
5. Pydantic validates the data
            ↓
6. Database function is called
            ↓
7. MySQL stores the student
            ↓
8. FastAPI returns the response
            ↓
9. Streamlit displays the result

Complete Flow
👤 User
  ↓
🎨 Streamlit
  ↓
⚡ FastAPI
  ↓
✅ Pydantic
  ↓
🗄️ MySQL
  ↓
⚡ FastAPI
  ↓
🎨 Streamlit
  ↓
👤 User

🎯 What I Learned
This project helped me understand how different parts of a modern application work together.
Backend
- Python
- FastAPI
- REST APIs
- CRUD operations
- Pydantic validation
- HTTP methods
Database
- MySQL
- SQL queries
- Database connectivity
- Primary keys
- Environment-based configuration
- SSL database connections
Frontend
- Streamlit
- API integration
- Forms
- Search and filtering
- Data presentation
DevOps
- Docker
- Docker images
- Docker containers
- Git
- GitHub
- Cloud deployment
Deployment
- Streamlit Cloud
- Render
- Aiven Cloud
- Connecting frontend, backend, and database
🧠 Interview Quick Revision
1. Explain your project.
I developed a Student Management System using Python. I used Streamlit for the frontend, FastAPI for building REST APIs, and MySQL for storing student data. The application supports CRUD operations such as creating, reading, updating, and deleting student records. The frontend communicates with the FastAPI backend through HTTP requests, and the backend communicates with MySQL using SQL queries. I also containerized the FastAPI backend using Docker and deployed the application using cloud services.

2. Why did you use FastAPI?
I used FastAPI because it is lightweight and well suited for building REST APIs. It also provides request validation through Pydantic and automatically generates Swagger API documentation.

3. Why did you use Streamlit?
I used Streamlit because it allows me to quickly build an interactive web interface using Python without developing a separate frontend framework.

4. Why did you use MySQL?
I used MySQL because the application manages structured student data and requires relational database operations such as INSERT, SELECT, UPDATE, and DELETE.

5. Why did you use Docker?
I used Docker to package my FastAPI application and its dependencies into a container so that it can run consistently across different environments.

6. How does the frontend communicate with the backend?
The Streamlit frontend sends HTTP requests to the FastAPI REST API. FastAPI processes the request, communicates with MySQL, and returns the response to Streamlit.

7. What happens when a student is added?
The user enters the details in Streamlit. Streamlit sends a POST request to FastAPI. FastAPI validates the data using Pydantic, calls the database function, and inserts the data into MySQL. The response is then returned to Streamlit.

8. Where is your database hosted?
The MySQL database is hosted on Aiven Cloud, while the FastAPI backend is deployed on Render.

9. Why are environment variables used?
Environment variables keep configuration and sensitive information such as database credentials outside the application source code.

10. What is CRUD?
CRUD stands for Create, Read, Update, and Delete. These are the four basic operations used to manage data in the application.

🚀 Future Improvements
Possible future improvements include:
- 🔐 User authentication and authorization
- 🧪 Automated testing
- 🔄 CI/CD pipeline
- 📊 Logging and monitoring
- ☸️ Kubernetes deployment
- ☁️ AWS deployment
These are future plans and are not part of the current implementation.

👨‍💻 Author
Jagan Kumar Panda
B.Tech Graduate | Aspiring Software Engineer
- 💻 GitHub: jagankumarpanda
- 🔗 LinkedIn: Jagan Kumar Panda
⭐ Project Status
✅ Completed & Deployed
✅ Python
✅ FastAPI
✅ REST API
✅ CRUD Operations
✅ MySQL
✅ Streamlit
✅ Pydantic
✅ Docker
✅ Git & GitHub
✅ Swagger API Documentation
✅ Cloud Deployment

⭐ Thank You
Thank you for visiting this project!
