from pymongo import MongoClient
from dotenv import load_dotenv
import os
import jwt
import hashlib

load_dotenv()

client = MongoClient(host=os.getenv("MONGO_HOST"))

db = client[os.getenv("DB_NAME")]
user_collection = db[os.getenv("USER_COLLECTION_NAME")]

def hash_password(password):
    SALT = "SALT"
    dataBase_password = password+SALT
    hashed = hashlib.md5(dataBase_password.encode())
    return hashed.hexdigest()

def create_user_in_db(name, password):
    token = ""
    duplicate_user = user_collection.find_one({"name": name})
    if duplicate_user is not None:
        return False, "Username already exists!", 
    data = {"name": name, "password": hash_password(password)}
    token = jwt.encode(data, "secret", algorithm="HS256")
    user_collection.insert_one(data)
    return True, "Username Added!", token

def verify_user(name, password, is_hashed = False):
    user = user_collection.find_one({"name": name})
    token = ""
    if user is not None:
        hashed_password = password if is_hashed else hash_password(password)
        if user["password"] != hashed_password:
            return False, "Wrong Password, Use the correct password!", token
        token = jwt.encode({"name": name, "password": hashed_password}, "secret", algorithm="HS256")
        return True, "User Authenticated!", token
    return False, "No User Found, Please Signup first!", token