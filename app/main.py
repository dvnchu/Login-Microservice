from fastapi import FastAPI
from database import engine
from models import Base, User
from sqlalchemy.orm import Session,select
from argon2 import PasswordHasher 
from argon2.exceptions import HashError



Base.metadata.create_all(bind=engine)

app = FastAPI()
ph = PasswordHasher()
session = Session(engine)

def hashpwd(password : str) -> str:
   #Recibe una contrasena en plaintext y devuelve el hash argon2 
  try:
    return ph.hash(password)
  except HashError:
    raise RuntimeError("Error al procesar la seguridad de la contraseña")


def login(usr:str, password:str) -> bool:
    hash: str = session.execute(select(User.password_hash).where(User.username == usr or User.email == usr))
    return ph.verify(hash,password) 

    

@app.get("/")
async def root():
    return {"message": "Hello world"}
