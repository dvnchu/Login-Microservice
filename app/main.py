from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select, or_
from database import engine, get_db
from models import Base, User
from sqlalchemy.orm import Session
from argon2 import PasswordHasher 
from argon2.exceptions import HashingError, VerifyMismatchError
from schemas import UserLogin, UserCreate
from sqlalchemy.exc import IntegrityError
import jwt
from dotenv import load_dotenv
import os

load_dotenv()
Base.metadata.create_all(bind=engine)
app = FastAPI()
ph = PasswordHasher()
secretKey: str = os.getenv("SECRET_KEY")



def hashpwd(password : str) -> str:
   #Recibe una contrasena en plaintext y devuelve el hash argon2 
  try:
    return ph.hash(password)
  except HashingError:
    raise RuntimeError("Error al procesar la seguridad de la contraseña")


@app.post("/login")
async def login(usrlog: UserLogin, session: Session = Depends(get_db)):
  #Busca el usuario en la db
  user : User = session.execute(select(User).where(or_(User.username == usrlog.login_identifier, User.email == usrlog.login_identifier))).scalar_one_or_none()
  if user == None:
    raise HTTPException(status_code=401, detail="Incorrect username or password")
  else:
    #Si existe hace la verificacion de contrasena correspondiente con argon2
    try:
      ph.verify(user.password_hash, usrlog.password)
      payload =  {"sub": str(user.id),"email": user.email}
      token: str = jwt.encode(payload, secretKey,algorithm="HS256") 
      return {"access_token": token, "token_type":"bearer"} 
    except VerifyMismatchError:
     raise HTTPException(status_code=401, detail="Incorrect username or password") 

@app.post("/register")
async def register(account: UserCreate, session: Session = Depends(get_db)):
  hashedPass: str= hashpwd(account.password)
  newUser = User(rol="user", email=account.email, username=account.username, password_hash=hashedPass)
  try:
    #Si el usuario no estaba registrado lo agrega a la db
    session.add(newUser)
    session.commit()
    return{"message": "account registered succesfully"}  
  except IntegrityError:
    raise HTTPException(status_code = 400, detail="Theres already an account with that username/email")