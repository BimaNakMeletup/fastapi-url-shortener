# URL Shortener API (Bit.ly Clone)

A lightweight and fast URL Shortener built with FastAPI, MySQL, and JWT Authentication. Features a clean, single-page application (SPA) dashboard styled with Tailwind CSS.

## Features

- **Link Generation:** Convert long URLs into dynamic short links (auto-generated 6-character codes).
- **Custom Aliases:** Allow registered users to define their own custom short codes (e.g., `/my-portfolio`).
- **Click Analytics:** Real-time counter tracks the total number of visits per link.
- **JWT Authentication:** Secure User Register & Login system to manage personal links in a private dashboard.
- **Public Redirection:** Fast routing and HTTP 307 temporary redirection for visitors without requiring authentication.

---

## Tech Stack

- **Backend:** Python 3.13+, FastAPI, Uvicorn
- **Database ORM:** SQLAlchemy, PyMySQL
- **Security:** Passlib (Bcrypt for password hashing), Python-Jose (JWT Tokens)
- **Frontend:** Vanilla JavaScript, HTML5, Tailwind CSS via CDN

---

## Project Structure

```text
url-shortener/
├── app/
│   ├── config.py          # Environment configuration mapping
│   ├── database.py        # SQLAlchemy connection and engine setup
│   ├── main.py            # Entrypoint & FastAPI initialization
│   ├── models/            # Database schema definitions (MySQL)
│   ├── routers/           # Combined API Routes and Controllers
│   │   ├── auth.py        # Login, Register, & JWT Logic
│   │   └── url.py         # Shorten, Redirect, & Dashboard Logic
│   └── utils/             # Hashing, JWT creation, and code generators
├── frontend/
│   └── index.html         # SPA Dashboard UI
├── .env                   # Local configuration (Ignored in git)
├── .gitignore             # Git ignore file configuration
└── requirements.txt       # Python package dependencies
