from database import engine, SessionLocal
from models import Base, Category, Product

print("="*50)
print("СОЗДАНИЕ БАЗЫ ДАННЫХ")
print("="*50)

# Создаем таблицы
Base.metadata.create_all(bind=engine)
print("✅ Таблицы созданы!")

# Создаем сессию
db = SessionLocal()

# Проверяем, есть ли уже данные
if db.query(Product).count() == 0:
    print("📦 Добавляем товары...")
    
    # Категории
    categories = [
        Category(name="Электроника"),
        Category(name="Одежда"),
        Category(name="Книги"),
        Category(name="Дом и сад")
    ]
    
    db.add_all(categories)
    db.commit()
    print("✅ Категории добавлены!")
    
    # Товары
    products = [
        Product(
            name="Смартфон iPhone 15",
            description="Новый флагман Apple с камерой 48 МП",
            price=89990.00,
            stock=15,
            category_id=1
        ),
        Product(
            name="Ноутбук ASUS",
            description="Для работы и учебы, 16 ГБ ОЗУ",
            price=69990.00,
            stock=8,
            category_id=1
        ),
        Product(
            name="Наушники Sony",
            description="Беспроводные, с шумоподавлением",
            price=12990.00,
            stock=25,
            category_id=1
        ),
        Product(
            name="Футболка Nike",
            description="Хлопок, черный цвет",
            price=2990.00,
            stock=50,
            category_id=2
        ),
        Product(
            name="Джинсы Levi's",
            description="Классический синий",
            price=5990.00,
            stock=30,
            category_id=2
        ),
        Product(
            name="Python для начинающих",
            description="Самоучитель по программированию",
            price=1990.00,
            stock=20,
            category_id=3
        ),
        Product(
            name="FastAPI веб-фреймворк",
            description="Создание современных API",
            price=2490.00,
            stock=12,
            category_id=3
        ),
        Product(
            name="Набор посуды",
            description="6 предметов, нержавеющая сталь",
            price=3990.00,
            stock=18,
            category_id=4
        )
    ]
    
    db.add_all(products)
    db.commit()
    print(f"✅ Добавлено {len(products)} товаров!")
else:
    print("ℹ️ Товары уже есть в базе данных")

db.close()
print("="*50)
print("ГОТОВО! База данных создана")
print("="*50)