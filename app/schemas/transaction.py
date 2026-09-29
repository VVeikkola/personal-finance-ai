from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TransactionCreate(BaseModel):
    description: str = Field(min_length=1, max_length=255)
    amount: Decimal
    transaction_date: date


class TransactionRead(BaseModel):
    id: int
    description: str
    amount: Decimal
    transaction_date: date

    model_config = ConfigDict(from_attributes=True)
