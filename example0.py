import secrets

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()


@app.get("/secure-endpoint/")
def secure_endpoint(username: str, password: str):
    if username != "admin" and password != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Помилка!!!!!")
    return {"message": f"Hello, {username}! You are authorized."}



@app.get("/get_product/")
def get_product(product_id:int, username: str, password: str):
    if username != "admin" and password != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Помилка!!!!!")

    return {"message": f"ти отримав продукт"}

uvicorn.run(app)