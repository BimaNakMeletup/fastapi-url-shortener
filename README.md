````markdown
# 🔗 URL Shortener API (Bit.ly Clone)

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![JWT](https://img.shields.io/badge/Auth-JWT-success)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight and fast **URL Shortener API** built with **FastAPI**, **MySQL**, and **JWT Authentication**. This project provides a modern Single Page Application (SPA) dashboard for managing shortened URLs, tracking click analytics, and creating custom aliases.

---

## ✨ Features

- 🔗 Generate short URLs with automatic 6-character codes.
- ✏️ Create custom aliases (e.g. `/portfolio`, `/github`).
- 📊 Track click counts for every shortened link.
- 🔐 JWT Authentication (Register & Login).
- 👤 Personal dashboard for managing user links.
- 🚀 Fast HTTP 307 Temporary Redirect.
- 🎨 Clean SPA interface using Tailwind CSS.
- 📱 Responsive design.

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Language | Python 3.13+ |
| Database | MySQL |
| ORM | SQLAlchemy |
| Authentication | JWT (Python-Jose) |
| Password Hashing | Passlib (Bcrypt) |
| ASGI Server | Uvicorn |
| Frontend | HTML5, Vanilla JavaScript, Tailwind CSS |

---

# 📁 Project Structure

```text
url-shortener/
│
├── app/
│   ├── config.py              # Environment configuration
│   ├── database.py            # Database connection
│   ├── main.py                # FastAPI entry point
│   │
│   ├── models/
│   │   ├── user.py            # User model
│   │   └── url.py             # URL model
│   │
│   ├── routers/
│   │   ├── auth.py            # Authentication endpoints
│   │   └── url.py             # URL management endpoints
│   │
│   └── utils/
│       ├── auth.py            # JWT utilities
│       ├── hashing.py         # Password hashing
│       └── generator.py       # Short code generator
│
├── frontend/
│   └── index.html             # Dashboard (SPA)
│
├── .env                       # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/url-shortener.git

cd url-shortener
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create MySQL Database

```sql
CREATE DATABASE db_url_shortener;
```

---

## 5. Configure Environment Variables

Create a file named **`.env`**

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/db_url_shortener

JWT_SECRET_KEY=YOUR_SUPER_SECRET_KEY

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 6. Run Application

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🌐 Main Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Login and receive JWT |

---

## URL Management

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/shorten` | Create shortened URL |
| GET | `/dashboard` | User dashboard |
| GET | `/{short_code}` | Redirect to original URL |

---

# 📊 Dashboard Features

- Create Short URL
- Custom Alias
- Copy Link
- Click Counter
- Delete URL
- User Authentication
- Responsive Interface

---

# 🔒 Authentication

Protected endpoints require a JWT Bearer Token.

Example Header:

```http
Authorization: Bearer <your_access_token>
```

---

# 🚀 Future Improvements

- QR Code Generator
- URL Expiration
- Link Password Protection
- User Profile
- Search & Filter
- Pagination
- Analytics Dashboard
- REST API Versioning
- Docker Support
- Unit Testing
- CI/CD with GitHub Actions

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

Developed for learning backend development using:

- FastAPI
- SQLAlchemy
- MySQL
- JWT Authentication
- Tailwind CSS

---

⭐ If you like this project, consider giving it a star on GitHub!
````
