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
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST', default='localhost'),
            'PORT': env('DB_PORT', default='5432'),
        }
    }

## 5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

## 6. Create Superuser (Optional)
python manage.py createsuperuser

## 7. Run the Development Server
python manage.py runserver

API available at: http://127.0.0.1:8000/api/ 
Schools API Endpoints
<img width="1376" height="867" alt="image" src="https://github.com/user-attachments/assets/1e6a08a7-530e-4bcc-83fc-dbe05168c77a" />
<img width="1437" height="873" alt="image" src="https://github.com/user-attachments/assets/0c038e4d-a232-4e96-b0dc-7660ceba3647" />
<img width="1432" height="868" alt="image" src="https://github.com/user-attachments/assets/ae3d6413-87a7-4038-a865-57f73405ec8c" />
<img width="1435" height="856" alt="image" src="https://github.com/user-attachments/assets/8bc399b5-f701-4289-9bdc-480c6717199f" />

Students API Endpoints
<img width="1442" height="867" alt="image" src="https://github.com/user-attachments/assets/58960a99-6092-42fb-9cc1-b9caeb0ea711" />
<img width="1422" height="848" alt="image" src="https://github.com/user-attachments/assets/deecb6a3-69f3-4970-ae35-01b51ef6c082" />
<img width="1428" height="856" alt="image" src="https://github.com/user-attachments/assets/782d2fe9-6c85-48bf-aa41-2b1941562679" />
<img width="1432" height="850" alt="image" src="https://github.com/user-attachments/assets/43c565ff-fa0e-45de-aa9a-fe5e9be100dd" />

Teachers API Endpoints
<img width="1437" height="857" alt="image" src="https://github.com/user-attachments/assets/adb08c8f-d093-41fe-807b-5b902cf495f2" />
<img width="1427" height="856" alt="image" src="https://github.com/user-attachments/assets/a46bfe4e-2caf-48db-b95b-eaa82e91c65d" />
<img width="1436" height="863" alt="image" src="https://github.com/user-attachments/assets/d5739e25-1174-4d04-9ee3-fcf8e42311c9" />
<img width="1430" height="863" alt="image" src="https://github.com/user-attachments/assets/6782bd72-a705-4204-afcd-1da17cdd69ee" />





 

