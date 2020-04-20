from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .patient import Patinet
from .donor import Donor
from .blood_bank import BloodBank

__all__ = ["Base", "Patient", "Donor", "BloodBank"]
