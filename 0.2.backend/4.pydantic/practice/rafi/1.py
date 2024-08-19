from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    # Pydantic - Custom Field Validation
    @field_validator('account_id')
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value


user = User(name = "Rafi", email = "rafi@gmail.com", account_id = 1234)
print(user)


# Pydantic - Json Serialization
user_json_str = user.json()
print(user_json_str)

user_json_obj = user.dict()
print(user_json_obj)


# Pydantic - Json Deserialization
json_str = '{"name": "user2", "email": "user2@gmail.com", "account_id": 1234}'
user2 = User.parse_raw(json_str)
print(user2)