from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import product_routes, cart_routes, order_routes, contact_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_routes.router, prefix="/api/products", tags=["Products"])
app.include_router(cart_routes.router, prefix="/api/cart", tags=["Cart"])
app.include_router(order_routes.router, prefix="/api/orders", tags=["Orders"])
app.include_router(contact_routes.router, prefix="/api/contacts", tags=["Contacts"])
