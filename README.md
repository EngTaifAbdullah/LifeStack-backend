# 📚 LifeStack Web Application - Backend
---
### Overview

This is the backend of the LifeStack full stack web application.
It provides a Django REST API that handles user authentication, data storage, and CRUD operations for certificates, personal documents, and future Goals (courses).

The backend is designed to work seamlessly with the **React (Vite)** frontend.

---

### 💡 Platform Idea

LifeStack is a digital personal platform that allows users to:

Organize and store their certificates, achievements, and personal documents.

Set and track future learning goals or courses.

Access all their data anytime, anywhere, through a secure and authenticated system.

---

### 🛠️ Tech Stack

- Django 5.0+
- Django REST Framework (DRF)
- PostgreSQL
- Django CORS Headers
- SimpleJWT (for authentication)
- Docker


  ---

  
### 🛠️ Project Structure (Backend)

 ```
LifeStack-backend/
│
├── LifeStack/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── certificates/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── courses/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── personal/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── users/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
└── manage.py
 ```

 ---
 
 ### ⚙️ Installation & Setup

#### 1. Clone the repository

```bash
git clone https://github.com/EngTaifAbdullah/LifeStack-backend.git
cd LifeStack-backend
```

#### 2. Create and activate virtual environment

```bash
python -m venv venv
source LifeStack-venv/Scripts/activate   # for Windows
```

#### 3. Install dependencies

```bash
pip install 
```

#### 4. Setup the PostgreSQL database
Create a PostgreSQL database manually, or use `.env` file as shown below.

#### 5. Environment Variables (`.env`)

```bash
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS= [127.0.0.1, localhost]

DB_NAME=LifeStack
DB_USER=postgres
DB_PASSWORD=*****
DB_HOST=localhost
DB_PORT=5432
```
#### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Create superuser

```bash
python manage.py createsuperuser
```

#### 8. Run the server

```bash
python manage.py runserver
```
The API will now be available at : `http://127.0.0.1:8000/api/`

---

## User Story

As a user, I want to:

1. Create my own account and be able to log in securely.
2. Upload my certificates and add their details so I can access them later.
3. Download my certificates in PDF format to my personal device.
4. Add future goals or courses that I plan to take in order to track my progress.
5. Edit the information of any certificate or course I have added.
6. Delete a certificate or course that I no longer need.
7. View all my achievements in an organized way, categorized by type (through a dashboard).
8. Search or filter to easily find a specific certificate or course.
9. Access my personal documents in a dedicated section of the website.
10. As an unregistered user, I can only see the Home & About page until I decide to register.

---
### Main Endpoints (API Routes)

| Endpoint                  | Method             | Description                                     |
| ------------------------- | ------------------ | ----------------------------------------------- |
| `/api/token/`             | POST               | Obtain JWT Token                                |
| `/api/token/refresh/`     | POST               | Refresh Access Token                            |
| `/api/register/`          | POST               | Register a new user                             |
| `/api/certificates/`      | GET / POST         | List or create certificates                     |
| `/api/certificates/{id}/` | GET / PUT / DELETE | Retrieve, update, or delete a certificate       |
| `/api/personal/`          | GET / POST         | List or create personal documents               |
| `/api/personal/{id}/`     | GET / PUT / DELETE | Retrieve, update, or delete a personal document |
| `/api/courses/`           | GET / POST         | List or create goals/courses                    |
| `/api/courses/{id}/`      | GET / PUT / DELETE | Retrieve, update, or delete a course            |


---
### 🧠 Models Overview

#### Certificate Model

```bash
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_obtained = models.DateField()
    file = models.FileField(upload_to='certificate/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificate')
```

#### Personal Document Model
```bash
class PersonalDocument(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='personal_docs/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_docs')

```

#### Course Model (Goals)
```bash
class Course(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
```

#### Course Model 

```bash
class Category(models.Model):
    CATEGORY_CHOICES = [
        
        ('Task', 'Task'),
        ('Course', 'Course'),
        ('Exam', 'Exam'),
    ]
    category_type = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='COURSE')
```

---
## 🔐 Authentication
This project uses JWT (JSON Web Token) authentication with SimpleJWT library.
Users can register, obtain tokens, and authenticate their API requests by including:
```bash
Authorization: Bearer <access_token>
```
---
### CORS Configuration
CORS is enabled in settings.py to allow the frontend React app to communicate with the backend:
```bash
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
```
---
### Admin Panel
Django’s built-in admin interface allows you to manage all models easily.
Visit: `http://127.0.0.1:8000/admin/`
Login using your superuser credentials.

---

### 🧪 Testing
All major endpoints (CRUD + Auth) were tested using `Postman`.

---
### 🐳 Docker Setup

#### 1. Build Docker Image
```bash
docker build -t lifestack-backend .
```
#### 2. Run the container 
```bash
docker run -p 8000:8000 lifestack-backend
```
---
#### 📊 Requirements Checklist
- ✅ Django REST Framework setup
- ✅ PostgreSQL database integration
- ✅ JWT Authentication
- ✅ CRUD for 3 related models
- ✅ CORS enabled for React frontend
- ✅ Dockerized for deployment
- ✅ Full integration with frontend (React)

---
### 📁 Communication with Frontend

- Frontend Repository: `https://github.com/EngTaifAbdullah/LifeStack-frontend`
- Frontend Base URL: `http://localhost:5173`
- API Base URL: `http://localhost:8000/api/`

---
### 🔮 Future Improvements
 1. Add User Profile Customization
 2. Add Notifications & Reminders
 3. Add Progress Tracking to view completed and in-progress goals
 4. Add File Sharing Feature
 5. Add Security Features in Personal Documents
 6. Integrate Cloud Backup Services
 7. Add Mobile App Version
 8. Add Multi-language Support
 9- Add password reset functionality

---
## 🧊 IceBox (Future Features)

 1. Add User Profile Customization
 2. Add Notifications & Reminders
 3. Add Progress Tracking to view completed and in-progress goals
 4. Add File Sharing Feature
 5. Add Security Features in Personal Documents
 6. Integrate Cloud Backup Services
 7. Add Mobile App Version
 8. Add Multi-language Support

### 👩‍💻 Developer

#### Taif Abdullah AlAnzi 
- Email: Eng.taifabdullah@gmail.com
- GitHub: @EngTaifAbdullah
