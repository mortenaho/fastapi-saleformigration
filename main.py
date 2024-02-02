from fastapi import APIRouter, FastAPI

from Controllers.LoginController import loginRoutes
from Controllers.ProductController import productRoutes

app = FastAPI()


app.include_router(loginRoutes)
app.include_router(productRoutes)


