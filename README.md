# ExpenseMind Backend

ExpenseMind is a backend service for managing personal financial tracking. Built with Python and FastAPI, it offers a secure and scalable architecture for handling user authentication and expense management.

## Features
- User authentication with JSON Web Tokens (JWT).
- CRUD operations for managing expenses.
- Secure password storage using bcrypt.
- Input validation with Pydantic models.
- Interactive API documentation via Swagger UI.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: MongoDB (NoSQL)

## Endpoints
- **Authentication**:
  - `POST /signup`: User registration.
  - `POST /login`: User login and JWT issuance.
- **Expenses**:
  - `GET /expenses`: Fetch all expenses for the authenticated user.
  - `POST /expenses`: Add a new expense.
  - `PUT /expenses`: Update an existing expense.
  - `DELETE /expenses`: Delete an expense.

## Installation and Setup

### Prerequisites
- Python 3.13.1
- MongoDB instance (local or MongoDB Atlas).

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/abhishekbatra1062k/ExpenseMind.git
   cd ExpenseMind/app
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate
   env\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Set up environment variables:
   ```bash
   MONGO_HOST = ''
   DB_NAME = 'Expense-Tracker'
   EXPENSE_COLLECTION_NAME = 'expenses'
   USER_COLLECTION_NAME = 'users'
5. Run the application:
   ```bash
   uvicorn main:app --reload