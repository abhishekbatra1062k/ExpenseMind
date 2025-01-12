import jwt
from db.user import verify_user

def verify_token(encoded_data):
    data = jwt.decode(encoded_data, "secret", algorithms=["HS256"])
    print(data)
    status, msg, _ = verify_user(data["name"], data["password"], is_hashed=True)
    return status, msg, data