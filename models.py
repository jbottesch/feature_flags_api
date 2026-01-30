from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

#Create Base for models
Base = declarative_base()

class FeatureFlag(Base):
    __tablename__ = "feature_flags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    enabled = Column(Boolean, default=False)
