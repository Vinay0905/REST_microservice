from pydantic import BaseModel, EmailStr, Field

class CustomerIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr

class OrderIn(BaseModel):
    customer_id: str
    item: str = Field(min_length=1)
    amount: float
