from fastapi import APIRouter
from pydantic import BaseModel
from db.expense import create_expense_in_db, get_expenses_from_db, update_expense_in_db, delete_expense_from_db
from db.user import create_user_in_db, verify_user
from utils.auth import verify_token

class Expense(BaseModel):
    name: str
    amount: int

class User(BaseModel):
    username: str
    password: str

router = APIRouter()

@router.post("/signup")
def create_user(req: User):
    req_data = req.model_dump()
    _, msg, token = create_user_in_db(req_data["username"], req_data["password"])
    return {"status": msg, "token": token}

@router.post("/login")
def create_user(req: User):
    req_data = req.model_dump()
    _, msg, token = verify_user(req_data["username"], req_data["password"])
    return {"status": msg, "token": token}

@router.post("/expenses")
def create_expense(token: str, req: Expense):
    req_data = req.model_dump()
    status, message, user_data = verify_token(token)
    if not status:
        return {"status": "Invalid Token!"}
    expense_data = create_expense_in_db(req_data["name"], req_data["amount"], user_data["name"])
    return {"status": "Expense Created!", "data": expense_data}

@router.get("/expenses")
def get_expenses(token: str):
    status, message, user_data = verify_token(token)
    if not status:
        return {"status": "Invalid Token!"}
    expense_data = get_expenses_from_db(user_data["name"])
    return {"expenses": expense_data}

@router.put("/expenses")
def update_expense(token: str, expense_id: str, req: Expense):
    data = req.model_dump()
    status, message, user_data = verify_token(token)
    if not status:
        return {"status": "Invalid Token!"}
    updated_data = update_expense_in_db(expense_id, data["name"], data["amount"], user_data["name"])
    return {"status": "Expense Updated!", "data": updated_data}

@router.delete("/expenses")
def delete_expense(token: str, expense_id: str):
    status, message, user_data = verify_token(token)
    if not status:
        return {"status": "Invalid Token!"}
    expense_data = delete_expense_from_db(expense_id, user_data["name"])
    return {"status": "Expense Deleted!", "data": expense_data}
