from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str 

    @field_validator('username')
    def username_length(cls,v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v 

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(self):   #  instance method
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
