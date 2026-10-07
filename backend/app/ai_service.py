from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role: str = "admin"


class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    created_at: datetime


class LoginRequest(BaseModel):
    email: str
    password: str


class ClientCreate(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None


class ClientOut(ClientCreate):
    id: int
    created_at: datetime


class VendorCreate(BaseModel):
    name: str
    contact: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None


class VendorOut(VendorCreate):
    id: int
    created_at: datetime


class ProductCreate(BaseModel):
    name: str
    sku: str
    category: Optional[str] = None
    unit_price: float = 0.0
    cost_price: float = 0.0
    stock_quantity: int = 0
    low_stock_threshold: int = 5


class ProductOut(ProductCreate):
    id: int
    created_at: datetime


class SaleCreate(BaseModel):
    client_id: int
    product_id: int
    quantity: int = 1
    unit_price: float = 0.0
    total_amount: float = 0.0
    status: str = "paid"


class SaleOut(SaleCreate):
    id: int
    sale_date: datetime


class InvoiceCreate(BaseModel):
    client_id: int
    total_amount: float = 0.0
    status: str = "pending"
    due_date: Optional[datetime] = None


class InvoiceOut(InvoiceCreate):
    id: int
    issue_date: datetime


class AIRequest(BaseModel):
    message: str = Field(..., min_length=3)


class AIResponse(BaseModel):
    summary: str
    action_points: list[str]
    confidence: float
    model: str
