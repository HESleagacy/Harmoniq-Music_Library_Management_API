# 🎵 Harmoniq - Music Library API

Harmoniq is a lightweight, modular **FastAPI** backend that manages a music library of bands and albums.  
Built with **SQLModel** for ORM modeling and **Alembic** for database migrations, Harmoniq demonstrates clean, scalable backend design following modern API architecture principles.

---

## 🚀 Features

- 🎶 CRUD operations for **Bands** and **Albums**
- 🔗 Relational database models with **one-to-many mapping**
- 🧩 **SQLModel ORM** integration for Pythonic database interaction
- 🪄 **Alembic migrations** for version-controlled schema management
- ✅ Input validation and typing with **Pydantic**
- 🧪 API testing and request templates via `api.http`
- 🗃️ Lightweight **SQLite** database for local development

---

## 🧠 Tech Stack

| **Category** | **Technology** | **Purpose** |
|---------------|----------------|--------------|
| Framework | FastAPI | API development |
| ORM | SQLModel | Database modeling |
| Migrations | Alembic | Schema evolution |
| Database | SQLite | Local persistence |
| Validation | Pydantic | Data integrity |
| Testing | HTTPX / api.http | API testing |

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/HESleagacy/Harmoniq.git
cd Harmoniq
