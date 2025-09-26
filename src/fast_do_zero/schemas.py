from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel): # Contrato de Entrada
    username: str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel): # Contrato de Saída
    username: str
    email: EmailStr
