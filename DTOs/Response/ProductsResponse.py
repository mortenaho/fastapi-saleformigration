from pydantic import BaseModel


class ProductsResponse(BaseModel):
    productName: str
    price: float
    imageUrl: str
    description: str
    productId: int
