from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product, Category

app = FastAPI(title="Магазин товаров")

# Подключаем папку со статическими файлами
app.mount("/static", StaticFiles(directory="static"), name="static")

# Функция для работы с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 МАРШРУТ 1: Все товары
@app.get("/products/all")
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

# 📌 МАРШРУТ 2: Товар по ID
@app.get("/products/get/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    return {"error": "Товар не найден"}

# 📌 Все категории
@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories

# 📌 Товары по категории
@app.get("/products/category/{category_id}")
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.category_id == category_id).all()
    return products

@app.get("/")
def root():
    return {
        "message": "Сервер работает!",
        "endpoints": {
            "все_товары": "/products/all",
            "товар_по_id": "/products/get/1",
            "категории": "/categories",
            "сайт": "/static/index.html",
            "документация": "/docs"
        }
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Запуск сервера...")
    print("📱 Открой сайт: http://localhost:8000/static/index.html")
    print("📚 Документация: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)