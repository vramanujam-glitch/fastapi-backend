from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.controllers import users, products, stocks, market

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Backend API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(stocks.router)
app.include_router(market.router)


@app.get("/")
def root():
    return {"message": "API is running", "docs": "/docs"}
