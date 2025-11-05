# Task Service API

A simple REST API for task management.
Built with **Django + Django REST Framework**, uses **PostgreSQL** as a database, and runs via **Docker Compose**.

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/ArystanKonash/nic-task-api.git
cd nic-task-api
```

### 2. Build and start the containers

```bash
docker compose up --build
```

After the containers are up:

* API will be available at **[http://localhost:8000](http://localhost:8000)**
* PostgreSQL will be running inside the `db` container

---

## Environment Variables

Defined inside `docker-compose.yml`, but you can also move them to a `.env` file if you prefer:

```
DB_NAME=mydatabase
DB_USER=admin
DB_PASSWORD=password
DB_HOST=db
DB_PORT=5432
DEBUG=True
```

---

## Task Model

| Field         | Type     | Description                    |
| ------------- | -------- | ------------------------------ |
| `id`          | Integer  | Auto increment primary key     |
| `title`       | String   | Task title (required)          |
| `description` | String   | Optional description           |
| `status`      | Enum     | `new` / `in_progress` / `done` |
| `created_at`  | DateTime | Creation timestamp             |
| `updated_at`  | DateTime | Update timestamp               |

---

## API Endpoints

| Method   | Endpoint       | Description              |
| -------- | -------------- | ------------------------ |
| `POST`   | `/tasks/`      | Create a new task        |
| `GET`    | `/tasks/`      | Retrieve all tasks       |
| `GET`    | `/tasks/{id}/` | Retrieve a specific task |
| `PUT`    | `/tasks/{id}/` | Update a task            |
| `DELETE` | `/tasks/{id}/` | Delete a task            |

---

## Example Requests

```bash
# Create a new task
curl -X POST http://localhost:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Finish NIC assignment", "description": "Level 2 task", "status": "new"}'

# Get all tasks
curl http://localhost:8000/tasks/

# Update a task
curl -X PUT http://localhost:8000/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "done"}'

# Delete a task
curl -X DELETE http://localhost:8000/tasks/1/
```

