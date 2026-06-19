# URL Shortener API (Bit.ly Clone)

Aplikasi pemendek URL sederhana menggunakan **FastAPI** untuk backend, **MySQL** untuk penyimpanan data, dan **Vanilla JS + Tailwind CSS** untuk antarmuka *single-page application* (SPA). Proyek ini dibuat modular dan sudah dilengkapi dengan sistem autentikasi JWT.

## 🚀 Fitur Utama
* **Shorten URL:** Ubah URL panjang menjadi kode unik 6 karakter.
* **Custom Alias:** Bisa buat custom string sendiri untuk ujung link (misal: `/portofolio`).
* **JWT Authentication:** Fitur register & login untuk mengamankan link yang digenerate.
* **Dashboard Analitik:** Melihat daftar link yang sudah dibuat beserta total hitungan klik (`clicks counter`) secara real-time.
* **Expiration Link:** Pengaturan masa aktif link (opsional).

## 📁 Struktur Folder
```text
url-shortener/
├── app/
│   ├── main.py          # Entry point aplikasi & mounting frontend
│   ├── config.py        # Validasi environment (.env)
│   ├── database.py      # Koneksi SQLAlchemy & Dependency DB
│   ├── models/          # Skema tabel MySQL (User & Url)
│   ├── schemas/         # Validasi data masuk/keluar (Pydantic)
│   ├── routers/         # Endpoint API / Controller (Auth & Url)
│   └── utils/           # Helper fungsi acak & keamanan JWT
└── frontend/
    └── index.html       # Tampilan Landing Page & Dashboard SPA

