from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.transaction import get_transactions, create_transaction
from app.schemas.transaction import TransactionRead, TransactionCreate


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)


@router.get("/", response_model=list[TransactionRead])
def read_transactions(
    db: Annotated[Session, Depends(get_db)],
):
    return get_transactions(db)


@router.post(
    "/",
    response_model=TransactionRead,
    status_code=status.HTTP_201_CREATED,
)
def create_new_transaction(
    transaction_data: TransactionCreate,
    db: Annotated[Session, Depends(get_db)],
):
    return create_transaction(db, transaction_data)
