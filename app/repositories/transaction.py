from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate


def get_transactions(session: Session) -> list[Transaction]:
    statement = select(Transaction)

    return session.execute(statement).scalars().all()


def create_transaction(
    session: Session,
    transaction_data: TransactionCreate,
) -> Transaction:
    transaction = Transaction(**transaction_data.model_dump())
    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return transaction
