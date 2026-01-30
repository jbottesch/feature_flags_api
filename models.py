from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FeatureFlag(Base):
    __tablename__ = "feature_flags"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    name = Column(String, unique=True)
    enabled = Column(Boolean, default=False)
