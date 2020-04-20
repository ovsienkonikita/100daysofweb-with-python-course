import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base


class BloodBank(Base):
    __tablename__ = "blood_banks"

    id_ = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    adress = sa.Column(sa.String)
    numbeeer = sa.Column(sa.Integer)

    donors = relationship("Donor")
