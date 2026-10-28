# Flask Manufacturing API

A REST API built with Flask and SQLite demonstrating full CRUD operations across three manufacturing resources — parts, orders, and employees. Built as a companion to the FastAPI version to contrast the two frameworks.

## Tech Stack

- **Flask** — web framework
- **Flask-SQLAlchemy** — database ORM integration
- **SQLAlchemy** — database ORM
- **SQLite** — database

## Project Structure

```
flask-manufacturing-api/
├── main.py              # app entry point, blueprint registration
├── database.py          # SQLite connection setup
├── models.py            # SQLAlchemy table definitions
├── requirements.txt     # project dependencies
└── routes/
    ├── parts.py         # parts endpoints
    ├── orders.py        # orders endpoints
    └── employees.py     # employees endpoints
```

## Endpoints

### Parts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/parts` | Get all parts |
| GET | `/parts/<part_id>` | Get part by ID |
| POST | `/parts` | Create a new part |
| PUT | `/parts/<part_id>` | Update a part |
| DELETE | `/parts/<part_id>` | Delete a part |

### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orders` | Get all orders |
| GET | `/orders/<order_id>` | Get order by ID |
| POST | `/orders` | Create a new order |
| PUT | `/orders/<order_id>` | Update an order |
| DELETE | `/orders/<order_id>` | Delete an order |

### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| GET | `/employees/<employee_id>` | Get employee by ID |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/<employee_id>` | Update an employee |
| DELETE | `/employees/<employee_id>` | Delete an employee |

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Jonnypit/flask-manufacturing-api.git
cd flask-manufacturing-api
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in the project root:
```
DATABASE_URL=sqlite:///./manufacturing.db
```

**4. Run the server**
```bash
python main.py
```

**4. Test the API**
```
http://localhost:5000/parts
```

The SQLite database is created automatically on first run.

## Flask vs FastAPI

This project is the Flask equivalent of the [FastAPI Manufacturing API](https://github.com/Jonnypit/manufacturing-api). Key differences:

| | Flask | FastAPI |
|---|---|---|
| Validation | Manual via `request.get_json()` | Automatic via Pydantic |
| Serialization | Manual `jsonify()` on every return | Automatic |
| Routing | `Blueprint` | `APIRouter` |
| Interactive docs | Not built-in | Auto-generated at `/docs` |
| Session management | Handled by Flask-SQLAlchemy | Explicit `Depends(get_db)` |

Flask is older (2010) and more manual. FastAPI (2018) was purpose-built for APIs with modern conventions built in.
