<div align="center">
  
  # FixinIT
  ### Jalan Rusak? Jangan Diam.
  
  [![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_Site-success?style=for-the-badge)](https://[URL_DEMO])
  [![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://[URL_REPO])
  [![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
  
  **Submission for ITECHNO CUP 2026 - Web Development**
  
  **By Lunara**
  
</div>

---

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Unggulan](#-fitur-unggulan)
- [Demo & Screenshot](#-demo--screenshot)
- [Teknologi](#-teknologi)
- [Arsitektur Sistem](#-arsitektur-sistem)
- [Instalasi & Setup](#-instalasi--setup)
- [Penggunaan](#-penggunaan)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Tim Developer](#-tim-pengembang)
- [Lisensi](#-lisensi)

---

## 👥 Tim Developer

| Nama | Peran | GitHub |
|------|-------|--------|
| **Raditya Al-Ghifari** | Project Lead &  Frontend Developer | [GitHub](https://github.com/Raditya1o) |
| **Qiandra Attaqilla Johan** | Frontend Developer & UI/UX Designer| [GitHub](https://github.com/QiandraTaqi) |
| **Muhammad Izzuddin El-Fakhri** | Backend Developer & Cloud Engineer | [GitHub](https://github.com/ElFakhri)

---

## 🎯 Tentang Proyek

### Latar Belakang

Jalan rusak bukan sekadar masalah kenyamanan, melainkan sumber ancaman serius bagi keselamatan jiwa dan kelancaran mobilitas warga. Berdasarkan data Badan Pusat Statistik (BPS), sebanyak 31% dari total panjang jalan di Indonesia berada dalam kondisi rusak hingga rusak berat.

Persentase kerusakan yang tinggi ini berdampak langsung pada maraknya insiden fatal di jalan raya. Menurut data Pusat Informasi Kriminal Nasional (Pusiknas) Polri, pada periode 1–28 Januari 2026 saja, tercatat 748 kasus kecelakaan di tingkat nasional yang dipicu oleh kondisi jalan berlubang/rusak, yang mengakibatkan 29 orang meninggal dunia serta ratusan lainnya mengalami luka-luka . Bahkan di wilayah metropolitan seperti Jakarta, Dinas Bina Marga DKI Jakarta mengidentifikasi sedikitnya 70 ruas jalan mengalami rusak berat pada awal 2026, yang berujung pada terjadinya 27 kecelakaan lalu lintas akibat jalan berlubang hanya dalam kurun waktu satu bulan (Januari 2026) hingga memakan korban jiwa.

Secara regulasi, Undang-Undang Nomor 22 Tahun 2009 tentang Lalu Lintas dan Angkutan Jalan telah mewajibkan penyelenggara jalan untuk segera memperbaiki jalan yang rusak atau memasang rambu peringatan demi mencegah korban jatuh . Namun di lapangan, proses penanganan kerap terlambat karena belum adanya wadah pelaporan yang terstruktur, visual, dan mudah diakses secara anonim oleh warga tanpa rasa khawatir. Keluhan yang beredar di media sosial kerap kali kehilangan detail lokasi yang presisi atau tidak terpantau perkembangan perbaikannya.

Akibat lambatnya penanganan ini, lubang-lubang kecil berisiko makin membesar akibat lalu lalang kendaraan dan genangan air hujan, yang berujung pada bertambahnya angka kecelakaan dan biaya perbaikan fisik. Oleh karena itu, diperlukan sebuah platform berbasis web yang dapat menjembatani laporan masyarakat langsung ke pihak berwenang melalui sistem pemetaan visual dan manajemen pengaduan yang terpusat.

Sumber data resmi:  
- Data Kondisi Jalan Nasional (31% Rusak): Liputan6 - BPS: 31 Persen Jalan di Indonesia Rusak dan Rusak Berat
- Data Kasus Kecelakaan & Jalan Rusak (Nasional & Jakarta 2026): Kompas.com - Jalan Rusak di Jakarta Picu Puluhan Kecelakaan di Awal 2026 (Memuat data Ditlantas Polda Metro Jaya & Pusiknas Polri).

### Solusi yang Ditawarkan

Untuk mengatasi permasalahan tersebut, solusi yang ditawarkan adalah Platform Web Pengaduan Jalan Rusak Berbasis Peta Interaktif. Platform ini berfungsi sebagai sarana digital bagi masyarakat untuk menyampaikan laporan kerusakan jalan secara langsung, terstruktur, dan tervisualisasi kepada pihak berwenang/admin pengelola, sekaligus mempermudah admin dalam memantau alur penanganannya.

### Tujuan Proyek

- 🎯 **Tujuan Utama**: Membantu Melapor Jalan yang rusak agar segera ditangani/diperbaiki
- 📊 **Target Pengguna**: Masyarakat Umum/Pengguna jalan
- 💡 **Value Proposition**: Pelaporan Presisi & Terstruktur: Memastikan setiap laporan warga dilengkapi dengan bukti foto dan titik lokasi yang jelas, meminimalisir kesalahan survei lokasi oleh petugas di lapangan.
· Visualisasi Spasial Real-Time: Penggunaan peta interaktif memudahkan warga maupun pihak berwenang untuk melihat pemetaan sebaran jalan rusak di suatu wilayah secara cepat.
· Manajemen Pengaduan Terpusat untuk Admin: Memudahkan pihak pengelola/pemerintah dalam mengorganisir penanganan fasilitas rusak berdasarkan titik lokasi dan memantau progres pengerjaannya secara efisien.

---

## ✨ Fitur Unggulan

### Fitur Utama

| Fitur | Deskripsi | Keunggulan |
|----------|--------------|---------------|
| **Form Pengaduan Terstruktur** | Formulir bagi pengguna untuk menginput nama, deskripsi kerusakan, lokasi presisi, dan lampiran foto bukti. | Memastikan laporan valid, akurat, dan langsung menyajikan konteks visual tanpa perlu survei berulang. |
| **MAP Interaktif** | Peta digital yang menampilkan sebaran titik-titik lokasi jalan rusak yang dilaporkan oleh masyarakat. | Memudahkan visualisasi pemetaan wilayah terdampak secara real-time bagi publik dan pengelola. |
| **Manajemen Laporan Berbasis Titik (Admin)** | Dashboard pengelola untuk mengelompokkan dan memproses laporan fasilitas berdasarkan lokasi tertentu. | Membantu pihak berwenang mengorganisir dan memprioritaskan penanganan jalan rusak secara efisien. |
| **Pemantauan Progress Pengaduan (Admin)** | Panel kontrol bagi admin untuk memperbarui status dan melacak tahapan penyelesaian pengaduan.] | [Menciptakan akuntabilitas dan transparansi sistematis dalam tata kelola perbaikan fasilitas publik. |

### Fitur Tambahan

- **Upload Foto Bukti** - [Memungkinkan pelapor mengunggah dokumentasi kondisi jalan rusak secara langsung di lapangan.]
- **Geolokasi Presisi** - [Menentuan titik koordinat lokasi kerusakan secara otomatis atau manual pada peta.]
- **Dashboard Ringkasan (Admin)** - [Menampilkan statistik dan ringkasan total laporan masuk serta status pengerjaannya.]
---

## 📸 Demo & Screenshot

### Live Demo

🔗 **[Kunjungi Website](https://fixin-it.onrender.com/)**

### Screenshot Aplikasi

<div align="center">
  <img src="screenshots/Screenshot 2026-09-06 at 22-40-53 Pengaduan Jalan Rusak.png" alt="Homepage" width="800"/>
  <p><em>Homepage - Tampilan utama aplikasi</em></p>
  
  <img src="screenshots/Screenshot 2026-09-06 at 23-08-11 Pengaduan Jalan Rusak.png" alt="Dashboard" width="800"/>
  <p><em>Dashboard - Panel kontrol pengguna</em></p>
  
  <img src="screenshots/Screenshot 2026-09-06 at 22-41-40 Pengaduan Jalan Rusak.png" alt="Feature" width="800"/>
  <img src="screenshots/Screenshot 2026-09-06 at 22-43-39 Pengaduan Jalan Rusak.png" alt="Feature" width="800"/>
  <p><em>Formulir Laporan - Lapor jalan rusak</em></p>
</div>

### Video Demo

📹 **[Link Video Demo](https://[URL_VIDEO])** _(opsional)_

---

## 🛠️ Teknologi

### Tech Stack

#### Frontend
```
Framework    : Vue.js 3
Build Tool   : Vite
UI Library   : Tailwind CSS
Routing      : Vue Router
HTTP Client  : Axios
```

#### Backend
```
Runtime      : Python 3
Framework    : Flask
Database     : PostgreSQL / SQLite (untuk pengembangan lokal)
ORM          : SQLAlchemy
Auth         : JWT (PyJWT)
CORS         : Flask-CORS
```

#### DevOps & Tools
```
Environment  : Local development + Firebase emulators for Dataconnect tooling
Testing      : Pytest-ready backend structure, frontend Vite build validation
Versioning   : Git + GitHub
```

### Alasan Pemilihan Teknologi

| Teknologi | Alasan Pemilihan |
|-----------|------------------|
| **Vue.js 3 + Vite** | Mempermudah pembuatan interface admin dan form laporan yang interaktif dengan ekosistem yang ringan dan cepat. |
| **Tailwind CSS** | Memungkinkan styling cepat, konsisten, dan responsif untuk UI yang modern tanpa konfigurasi CSS yang kompleks. |
| **Flask + SQLAlchemy** | Cocok untuk API cepat, struktur backend sederhana, dan pengelolaan data laporan serta pengguna dengan biaya implementasi yang efisien. |
| **SQLite + JWT** | Menyediakan penyimpanan data yang ringan untuk proyek kompetisi sekaligus autentikasi stateless untuk flow admin/user. |

### Dependencies Utama

```json
{
  "frontend": {
    "vue": "^3.5.41",
    "vue-router": "^5.2.0",
    "axios": "^1.5.0",
    "tailwindcss": "^4.3.3",
    "vite": "^8.2.1"
  },
  "backend": {
    "Flask": "3.1.3",
    "flask-cors": "6.0.5",
    "Flask-SQLAlchemy": "3.1.1",
    "PyJWT": "2.13.0",
    "SQLAlchemy": "2.0.52"
  }
}
```

---

## 🏗️ Arsitektur Sistem

### System Architecture

### Komponen & Tanggung Jawab
- **Frontend (`Vue 3` + `Vite`)**: UI untuk pelapor dan admin; menampilkan peta (Leaflet), form pengaduan bertipe multipart/form-data, preview foto, dan ringkasan laporan.
- **Geocoding / Maps**: `Leaflet` untuk rendering peta; `photon.komoot.io` (atau alternatif) untuk pencarian dan reverse-geocoding lokasi.
- **Backend (`Flask`)**: Endpoint REST untuk autentikasi (JWT), pembuatan dan pengambilan laporan, penyajian gambar via route terproteksi, dan logika admin (ubah status laporan).
- **Database (Postgres / SQLite)**: Menyimpan tabel `profiles` dan `pengaduans` sesuai skema SQL di bawah.
- **Storage untuk Foto**: Sementara menggunakan folder `uploads/`; untuk produksi gunakan S3-compatible object storage dan simpan URL di `pengaduans.pictureUrl`.
- **Notifikasi / Integrasi**: Opsional — webhook atau email ketika status laporan berubah atau untuk sinkronisasi dengan sistem pengelolaan aset publik.

### Alur Data (High-level)
1. Pengguna mengisi form di frontend (deskripsi, lokasi, foto) dan mengirimkan request multipart ke `POST /api/reports/`.
2. Backend memverifikasi JWT, menyimpan file (uploads) dan menulis record `pengaduans` di database dengan `status='pending'`.
3. Admin melihat daftar laporan di dashboard, memperbarui status (e.g., in_progress, resolved), dan dapat menambahkan catatan atau bukti perbaikan.
4. Frontend menampilkan marker peta dari data `pengaduans` yang diambil lewat endpoint `GET /api/reports/`.

### Keamanan & Praktik Operasional
- Gunakan HTTPS/TLS di semua lingkungan produksi.
- Simpan `JWT_SECRET` dan kredensial database di environment variables / secret manager.
- Batasi tipe file dan ukuran upload (sudah dilakukan pada backend dengan `ALLOWED_EXTENSIONS`).
- Sanitasi input teks dan gunakan parameterized queries melalui SQLAlchemy.

### Deployment & Scaling
- **Kecil / Demo**: Deploy backend di Render / Heroku / Fly.io dan frontend di Vercel. Gunakan `SQLite` untuk demo cepat, namun disarankan `Postgres` untuk penyimpanan yang persisten.
- **Produksi**: Gunakan instance `Postgres` terkelola, penyimpanan objek (mis. `S3`), dan penskalaan horizontal untuk API di balik load balancer. Pindahkan aset statis dan gambar ke CDN.
- **Monitoring**: Tambahkan logging terstruktur, pelacakan error (mis. `Sentry`), serta metrik sederhana untuk jumlah permintaan, tingkat error, dan throughput laporan.


### Database Schema

```sql
-- Profiles (users)
CREATE TABLE profiles (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  namaLengkap TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'admin',
  dibuatPada DATETIME NOT NULL DEFAULT (datetime('now'))
);

-- Reports (pengaduans)
CREATE TABLE pengaduans (
  id TEXT PRIMARY KEY,
  profile_id TEXT NOT NULL REFERENCES profiles(id),
  description TEXT NOT NULL,
  lokasi TEXT NOT NULL,
  pictureUrl TEXT,
  status TEXT NOT NULL DEFAULT 'pending',
  dibuatPada DATETIME NOT NULL DEFAULT (datetime('now'))
);

-- Helpful indexes
CREATE INDEX IF NOT EXISTS idx_pengaduans_profile_id ON pengaduans(profile_id);
CREATE INDEX IF NOT EXISTS idx_pengaduans_status ON pengaduans(status);
```

### Folder Structure

```
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── admin.py
│   │   │   ├── auth.py
│   │   │   └── reports.py
│   │   ├── config.py
│   │   ├── extensions.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── .env.example
│   ├── fixinit.db
│   ├── requirements.txt
│   ├── run.py
│   └── tests
│       └── test_admin_status.py
├── frontend
│   ├── dataconnect
│   │   ├── .dataconnect
│   │   │   └── schema
│   │   │       ├── main
│   │   │       │   ├── input.gql
│   │   │       │   ├── mutation.gql
│   │   │       │   ├── query.gql
│   │   │       │   └── relation.gql
│   │   │       └── prelude.gql
│   │   ├── dataconnect.yaml
│   │   ├── example
│   │   │   ├── connector.yaml
│   │   │   └── queries.gql
│   │   └── schema
│   │       └── schema.gql
│   ├── .env.example
│   ├── firebase.json
│   ├── .firebaserc
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── skills-lock.json
│   ├── src
│   │   ├── Admin_selesai.vue
│   │   ├── Admin_users.vue
│   │   ├── Admin.vue
│   │   ├── api.js
│   │   ├── App.vue
│   │   ├── Form.vue
│   │   ├── Home.vue
│   │   ├── img
│   │   │   └── rusak.jpg
│   │   ├── JS
│   │   │   ├── main.js
│   │   │   └── router.js
│   │   ├── Login.vue
│   │   ├── Register.vue
│   │   ├── report-forms
│   │   ├── style
│   │   │   └── style.css
│   │   └── tailwind.config.js
│   └── vite.config.js
├── .gitignore
├── README.md
├── scripts
│   └── tree.py
└── vercel.json
```

---

## ⚙️ Instalasi & Setup

### Prerequisites

Pastikan Anda telah menginstall:
- **Node.js** (v18.x atau lebih tinggi)
- **npm**
- **PostgreSQL / Sqlite**
- **Git**

Untuk backend juga diperlukan:
- **Python 3.10+**
- **pip** dan **virtualenv**

### Langkah Instalasi


#### 1. Clone repository

```bash
git clone https://github.com/ElFakhri/FixinIT.git
cd FixinIT
```

#### 2. Backend (Python / Flask)

1. Buat virtual environment dan aktifkan (opsional, tapi disarankan):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies backend:

```bash
pip install -r backend/requirements.txt
```

3. Buat folder untuk uploads (aplikasi biasanya sudah membuatnya otomatis, tetapi pastikan ada):

```bash
mkdir -p backend/app/uploads
```

4. Buat file `.env` di root atau atur environment variables yang diperlukan (contoh minimal):

```env
# untuk Postgres (opsional)
DATABASE_URL="postgresql://user:pass@localhost:5432/fixinit"

# secret untuk JWT / Flask
JWT_SECRET="change_me"
SECRET_KEY="change_me"
```

5. Jalankan server backend (development):



---


Server backend default berjalan di `http://localhost:5000`.

> Catatan: aplikasi memanggil `db.create_all()` saat startup sehingga tabel akan dibuat otomatis jika menggunakan SQLite. Untuk Postgres gunakan variabel `DATABASE_URL` di `.env`.

#### 3. Frontend (Vue / Vite)

1. Pindah ke folder frontend dan install dependensi:


## Penggunaan

### Menjalankan Aplikasi


2. Jalankan dev server frontend:

```bash
# Development mode

Frontend default akan berjalan di `http://localhost:5173` (Vite). Untuk mengakses API backend, pastikan konfigurasi `api.js` mengarah ke `http://localhost:5000` atau set proxy pada Vite jika diperlukan.

### Troubleshooting singkat
- Jika upload tidak tersimpan, periksa `backend/app/config.py` `UPLOAD_FOLDER` dan permission folder `backend/app/uploads`.
- Untuk masalah koneksi DB, verifikasi `DATABASE_URL` dan bahwa service Postgres berjalan.
- Jika environment variables tidak terbaca, pastikan `python-dotenv` terinstal dan file `.env` berada di root.

Aplikasi backend + frontend sekarang dapat dijalankan secara lokal: backend di `:5000` dan frontend di Vite port default.
npm run dev

# Production build
npm run build
npm run start

# Run tests
npm run test

# Linting
npm run lint
```

### User Guide

#### Untuk Pengguna Umum

1. **Registrasi/Login**: [Jelaskan cara mendaftar atau login]
2. **[Fitur 1]**: [Jelaskan cara menggunakan fitur ini]
3. **[Fitur 2]**: [Jelaskan cara menggunakan fitur ini]

#### Untuk Admin

1. **Akses Admin Panel**: [Jelaskan cara mengakses]
2. **[Fungsi Admin 1]**: [Jelaskan cara menggunakan]
3. **[Fungsi Admin 2]**: [Jelaskan cara menggunakan]

---

## 📚 API Documentation

### Base URL

```
Development: http://localhost:5000
Production:  https://fixinit-g0vh.onrender.com
```

### Endpoints

#### Authentication

```http
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/me
```

#### [Resource 1]

```http
GET    /api/[resource]       # Get all
GET    /api/[resource]/:id   # Get by ID
POST   /api/[resource]       # Create
PUT    /api/[resource]/:id   # Update
DELETE /api/[resource]/:id   # Delete
```

### Example Request

```javascript
// Login
const response = await fetch('/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
});
```

📖 **[Dokumentasi API Lengkap](./docs/API.md)** _(opsional)_

---

## 🧪 Testing

### Backend (pytest)

1. Pastikan virtualenv aktif dan dependencies backend terinstal (`pip install -r backend/requirements.txt`). Jika belum terpasang, install `pytest`:

```bash
pip install pytest
```

2. Jalankan test suite backend:

```bash
pytest backend/tests -q
```

3. Menjalankan satu file atau test tertentu:

```bash
pytest backend/tests/test_admin_status.py -q
```

Catatan: repository sudah menyertakan `backend/tests/test_admin_status.py` sebagai titik awal. Jika `pytest` belum ada di `requirements.txt`, tambahkan pada environment development Anda.

### Frontend

Saat ini tidak ada test runner yang dikonfigurasi untuk frontend dalam `package.json`. Untuk menambahkan pengujian unit/E2E, pertimbangkan:

- Unit: `vitest` atau `jest` untuk Vue 3
- E2E: `cypress` atau `playwright`

Contoh singkat untuk menambahkan `vitest`:

```bash
cd frontend
npm install -D vitest @vue/test-utils
# tambahkan script di package.json: "test": "vitest"
npm run test
```

### Smoke tests manual

- Pastikan backend berjalan di `http://localhost:5000` dan frontend di `http://localhost:5173`.
- Tes pengiriman laporan manual: buka form di frontend, isi deskripsi, lokasi, unggah foto, dan kirim — periksa apakah record muncul di `GET /api/reports/`.

Jika mau, saya bisa menambahkan konfigurasi `pytest` / contoh test lebih lengkap, atau menambahkan `vitest` ke frontend. Mana yang ingin Anda prioritaskan?

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE) - lihat file LICENSE untuk detail lebih lanjut.

---

<div align="center">

  **Made with ❤️ by Lunara for ITECHNO CUP 2026**

  
</div>