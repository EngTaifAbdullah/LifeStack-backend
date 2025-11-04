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
- Gunicorn (for production)
- Pillow (for image/file uploads)

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
Create a PostgreSQL database manually, or use .env file as shown below.
