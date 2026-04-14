# ⚽ Football News Hub

A premium, real-time football news aggregator built with Django and powered by NewsAPI. Stay updated with the latest headlines from the Premier League, UEFA, and your favorite teams like Barcelona and Real Madrid.

**🚀 Live Demo:** [https://news-1-u5vj.onrender.com/](https://news-1-u5vj.onrender.com/)

---

## ✨ Features

- **Real-Time Aggregation:** Fetches the latest football news dynamically from hundreds of sources via NewsAPI.
- **Smart Filtering:** Specifically curated for football enthusiasts, focusing on major leagues (EPL, UEFA) and top-tier clubs.
- **Premium UI:** A modern, dark-themed responsive interface optimized for all devices, featuring football-themed animations and hover effects.
- **Fast Performance:** Optimized for production using WhiteNoise for static file serving and Gunicorn for the app server.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Django 5.1.7
- **Frontend:** HTML5, CSS3 (Vanilla)
- **API:** [NewsAPI.org](https://newsapi.org/)
- **Deployment:** Render (Web Service)
- **Static Assets:** WhiteNoise (Compressed & Manifested)
- **Server:** Gunicorn

---

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ramuuzz/news.git
   cd news/news
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Environment Variables:**
   Create a `.env` file in the `news/news` directory and add:
   ```env
   NEWSAPI_KEY=your_api_key_here
   DEBUG=True
   SECRET_KEY=your_development_secret_key
   ```

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

---

## 🚀 Deployment (Render)

This project is configured for seamless deployment on Render using the `render.yaml` file.

### Required Environment Variables on Render:
| Key | Value |
|---|---|
| `NEWSAPI_KEY` | Your NewsAPI.org key |
| `SECRET_KEY` | A long random string |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*.onrender.com` (handled automatically by code) |
| `CSRF_TRUSTED_ORIGINS` | `https://*.onrender.com` (handled automatically by code) |

### Build & Start Commands:
- **Build:** `pip install -r requirements.txt && python manage.py collectstatic --no-input`
- **Start:** `gunicorn news.wsgi:application`

---

