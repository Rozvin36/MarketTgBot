import uuid
from datetime import datetime

from sqlalchemy import String, BigInteger, Integer, UUID, Enum, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped

from core.database import Base
from core.enums import Status


class ProductORM(Base):
    __tablename__ = 'product'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)

    name: Mapped[str] = mapped_column(
        String(32 ),
        nullable=False
    )

    price: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[Status] = mapped_column(
        Enum(Status, name="status_enum", create_type=False),
        default=Status.ABSENT.value
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

# id, user_id, product_id, amount, paid_a
class PurchaseORM(Base):
    __tablename__ = 'purchase'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(BigInteger)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    amount: Mapped[int] = mapped_column(Integer)
    paid_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
