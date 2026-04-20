# Emotion Detection Project

This project uses AI to detect emotions from text. It is structured into separate frontend and backend folders for easy deployment.

## 🚀 Structure

- **`backend/`**: A Flask API that handles emotion prediction using a trained model.
- **`frontend/`**: A modern, responsive web interface built with HTML/CSS and Vanilla JavaScript.

## 🛠️ How to Run Locally

### 1. Start the Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```
The backend will run on `http://localhost:5000`.

### 2. Start the Frontend
Simply open `frontend/index.html` in any browser, or serve it using a local server (e.g., Live Server in VS Code).

## ☁️ Deployment Tips

### Backend (e.g., Render, Heroku)
- Point the deployment to the `backend/` directory.
- Use `python app.py` (or `gunicorn app:app`) as the start command.
- Set the `PORT` environment variable if required.

### Frontend (e.g., Vercel, Netlify)
- Deploy the `frontend/` directory as a static site.
- If the backend is hosted at a different URL, update the `fetch()` URL in `frontend/index.html`.

## ✨ Features
- **Modern UI**: Dark mode with premium aesthetics and animations.
- **Real-time API**: Fast predictions using scikit-learn models.
- **Separation of Concerns**: Easy to maintain and scale.
