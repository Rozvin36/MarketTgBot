import uuid
from datetime import datetime

from sqlalchemy import String, BigInteger, Integer, UUID, Enum, DateTime, func, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from core.database import Base
from core.enums import Status

class AbstractTableModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)

class ProductORM(AbstractTableModel):
    __tablename__ = 'product'


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
class PurchaseORM(AbstractTableModel):
    __tablename__ = 'purchase'


    user_id: Mapped[int] = mapped_column(BigInteger)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product.id"))
    amount: Mapped[int] = mapped_column(Integer)
    paid_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    product = relationship("ProductORM", back_populates="purchases")