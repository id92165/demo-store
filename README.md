
# Demo Store

This project is a simple web store application with a Python backend and a static frontend.

## How to Run the Application

### 1. Using Docker Compose

1. Make sure you have Docker and Docker Compose installed.
2. In the project root, run:

```zsh
docker-compose up --build
```

- The app will be available at: http://localhost:9000

### 2. Without Docker (Locally)

1. Install dependencies:

```zsh
pip install -r requirements.txt
```

2. Start the server:

```zsh
python app/main.py
```

- The app will be available at: http://localhost:9000

## How to Stop the Application

### If running with Docker Compose:

```zsh
docker-compose down
```

### If running locally:

- Just stop the server process (Ctrl+C in the terminal).

## Project Structure

- `app/` — application source code
  - `frontend/` — HTML files and images
  - `services/` — microservices
  - `main.py` — entry point
  - `database.py`, `models.py`, `seed.py` — data management
- `requirements.txt` — Python dependencies
- `Dockerfile`, `docker-compose.yml` — containerization

## Additional

- To seed the database with initial data, run:

```zsh
python app/seed.py
```

---

If you have any questions, contact the project author.
