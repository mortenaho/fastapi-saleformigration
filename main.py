from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from Controllers.LoginController import loginRoutes
from Controllers.ProductController import productRoutes

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(loginRoutes)
app.include_router(productRoutes)


