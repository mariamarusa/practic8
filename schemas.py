from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None
    author: Optional[str] = None

class ReviewCreate(ReviewBase):
    product_id: int

class Review(ReviewBase):
    id: int
    product_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    created_at: datetime
    products: List["Product"] = []
    
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int = 0
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: datetime
    category: Optional[Category] = None
    reviews: List[Review] = []
    
    class Config:
        from_attributes = True

# Для обновления связей
Category.model_rebuild()
Product.model_rebuild()