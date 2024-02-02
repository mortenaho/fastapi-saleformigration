from pydantic import BaseModel


class LoginResponse(BaseModel):
    ResponseMessage: str
    ResponseCode: int
