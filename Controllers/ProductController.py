from typing import Type, Any

from fastapi import APIRouter

from DTOs.Response.ProductsResponse import ProductsResponse

productRoutes = APIRouter()


@productRoutes.post("/products/")
async def products() -> list[ProductsResponse]:
    return [
        ProductsResponse(productId=1, productName="آیفون 13", price=120000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول"),
        ProductsResponse(productId=2, productName="آیفون 14", price=1400000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول"),
        ProductsResponse(productId=3, productName="لپتاپ ایسوس", price=45600000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول"),
        ProductsResponse(productId=4, productName="لیتاپ آپل", price=123000000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول"),
        ProductsResponse(productId=5, productName="پوکو x3", price=14460000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول"),
        ProductsResponse(productId=6, productName="ردمی نوت 10", price=1200000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول"),
        ProductsResponse(productId=7, productName="ردمی نوت 14 پرو", price=1200000, imageUrl="",
                         description="تست توضیحات محصول تست توضیحات محصول تست توضیحات محصول")
    ]
