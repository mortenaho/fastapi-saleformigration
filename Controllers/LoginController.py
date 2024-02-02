from typing import Type

from fastapi import APIRouter

from DTOs.Request.LoginRequest import LoginRequest
from DTOs.Response.LoginResponse import LoginResponse

loginRoutes = APIRouter()


@loginRoutes.post("/login/")
async def login(loginRequest: LoginRequest) -> LoginResponse:
    response = LoginResponse
    if loginRequest.username == "mortenaho" and loginRequest.password == "1662":
        response.ResponseMessage = "Logged in successfully"
        response.ResponseCode = 200
    else:
        response.ResponseMessage = "Wrong username or password"
        response.ResponseCode = 401
    return response
