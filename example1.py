import secrets

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

def check_credentials(username: str, password: str):
    if username != "admin" and password != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Помилка!!!!!")
    return username




@app.get("/secure-endpoint/")
def secure_endpoint(username = Depends(check_credentials)):
    return {"message": f"Hello, {username}! You are authorized."}

uvicorn.run(app)