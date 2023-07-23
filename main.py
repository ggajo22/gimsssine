from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.itfcd import router as itfcd
from domain.complete import router as complete
from domain.booksen_category import router as booksen_category
from domain.booksen_info import router as booksen_info
from domain.currency import router as currency
from domain.dimension import router as dimension
from domain.dimension_from import router as dimension_from
from domain.failure import router as failure
from domain.shopify_collection import router as shopify_collection
from domain.shopify_collect import router as shopify_collect
from domain.shopify_product import router as shopify_product
from domain.shopify_image import router as shopify_image
from domain.shopify_variant import router as shopify_variant
from domain.shopify_price import router as shopify_price
from domain.writer import router as writer

app = FastAPI()

origins = [
    "http://localhost:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(itfcd.router)
app.include_router(complete.router)
app.include_router(booksen_category.router)
app.include_router(booksen_info.router)
app.include_router(currency.router)
app.include_router(dimension.router)
app.include_router(dimension_from.router)
app.include_router(failure.router)
app.include_router(shopify_collection.router)
app.include_router(shopify_collect.router)
app.include_router(shopify_product.router)
app.include_router(shopify_image.router)
app.include_router(shopify_variant.router)
app.include_router(shopify_price.router)
app.include_router(writer.router)
