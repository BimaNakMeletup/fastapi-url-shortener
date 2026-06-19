````markdown
# URL Shortener API

A simple URL shortener built with **FastAPI**, **MySQL**, and **JWT Authentication**. Users can create short links, manage them through a dashboard, and track how many times each link has been visited.

## Preview

- Generate short URLs
- Create custom aliases
- User authentication (JWT)
- Personal dashboard
- Click analytics
- Fast HTTP redirect

---

## Tech Stack

| Backend | Database | Authentication | Frontend |
|---------|----------|----------------|-----------|
| FastAPI | MySQL | JWT | HTML, Tailwind CSS, JavaScript |

Other libraries:

- SQLAlchemy
- PyMySQL
- Passlib (bcrypt)
- Python-Jose
- Uvicorn

---

## Project Structure

```text
url-shortener/
│
├── app/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── url.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   └── url.py
│   │
│   └── utils/
│       ├── auth.py
│       ├── hashing.py
│       └── generator.py
│
├── frontend/
│   └── index.html
│
├── .env
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/url-shortener.git

cd url-shortener
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

```sql
CREATE DATABASE db_url_shortener;
```

### 5. Configure environment variables

Create a `.env` file in the project root.

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/db_url_shortener

JWT_SECRET_KEY=YOUR_SECRET_KEY

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 6. Run the server

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI provides interactive documentation out of the box.

| Documentation | URL |
|--------------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

## Main Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new account |
| POST | `/login` | Login and get access token |
| POST | `/shorten` | Create a short URL |
| GET | `/dashboard` | Get user's URLs |
| GET | `/{short_code}` | Redirect to the original URL |

---

## Features

- Automatic short code generation
- Custom aliases
- JWT authentication
- Click counter
- Personal dashboard
- Responsive interface

---

## Future Improvements

- QR Code generation
- URL expiration
- Link password protection
- Search & filtering
- Pagination
- Docker support
- Unit testing
- CI/CD

---

## License

This project is available under the MIT License.
````
