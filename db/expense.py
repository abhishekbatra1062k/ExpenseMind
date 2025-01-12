from pymongo import MongoClient
from dotenv import load_dotenv
import os
from uuid import uuid4
from bson import ObjectId

load_dotenv()

client = MongoClient(host=os.getenv("MONGO_HOST"))

db = client[os.getenv("DB_NAME")]
expense_collection = db[os.getenv("EXPENSE_COLLECTION_NAME")]

def create_expense_in_db(name, amount, username):
    data = {
        "_id": ObjectId(),
        "expense_id": str(uuid4()),
        "name": name, 
        "amount": amount,
        "user": username
    }
    expense_collection.insert_one(data)
    if "_id" in data:
        del data["_id"]
    return data

def get_expenses_from_db(username):
    data_from_db = expense_collection.find({"user": username})
    expense_data = []
    for data in data_from_db:
        if "_id" in data:
            del data["_id"]
        expense_data.append(data)
    return expense_data

def update_expense_in_db(expense_id, name, amount, username):
    filter = {"expense_id": expense_id, "user": username}
    updated_data = {"name": name, "amount": amount}
    expense_collection.update_one(filter, {"$set": updated_data})
    return updated_data

def delete_expense_from_db(expense_id, username):
    filter = {"expense_id": expense_id, "user": username}
    deleted_data = expense_collection.find_one_and_delete(filter)
    if deleted_data is not None and "_id" in deleted_data:
        del deleted_data["_id"]
    return deleted_data
