# School Management System Using API
## Objective
Build a School Management System using API , Django and Postgresql
## Description
This project implements a RESTful API for managing Schools, Students, and Teachers using Django REST Framework (DRF) with Postgresql as the database.
All CRUD operations, JWT authentication are implemented.
## Implemented Features
### 1.School Management
    .CRUD operations for schools
    .Endpoints:
        .GET /api/schools/ – List all schools
        .POST /api/schools/ – Add a new school
        .PUT /api/schools/{id}/ – Update school details
        .DELETE /api/schools/{id}/ – Delete a school
### 2.Student Management
    .CRUD operations for students
    .Students linked to schools via Foreign Key
    .Endpoints:
        .GET /api/students/ – List all students
        .POST /api/students/ – Add a new student
        .PUT /api/students/{id}/ – Update student details
        .DELETE /api/students/{id}/ – Remove a student
### 3.Teacher Management
    .CRUD operations for teachers
    .Teachers linked to schools via Foreign Key
    .Endpoints:
        .GET /api/teachers/ – List all teachers
        .POST /api/teachers/ – Add a new teacher
        .PUT /api/teachers/{id}/ – Update teacher details
        .DELETE /api/teachers/{id}/ – Remove a teacher
### 4.Security & Enhancements
    .JWT authentication for secure API access
    .Basic validation in serializers
## Setup Instructions

## 1. Clone the Repository
git clone https://github.com/aayushmapokhrel/school.git

## 2. Create a virtual environment
python -m venv venv source venv/bin/activate # macOS/Linux venv\Scripts\activate # Windows

## 3. Install dependencies
pip install -r requirements.txt

## 4. Configure Postgresql

## 5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

## 6. Create Superuser (Optional)
python manage.py createsuperuser

## 7. Run the Development Server
python manage.py runserver

API available at: http://127.0.0.1:8000/api/ Schools API Endpoints
<img width="1376" height="867" alt="image" src="https://github.com/user-attachments/assets/1e6a08a7-530e-4bcc-83fc-dbe05168c77a" />

 

