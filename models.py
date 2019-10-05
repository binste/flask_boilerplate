from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class InterestingFact(Base):
    __tablename__ = "interesting_fact"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20))
    description = Column(VARCHAR(80))
    some_dimension_id = Column(Integer, ForeignKey("some_dimension.id"))

    some_dimension = relationship("SomeDimension", back_populates="interesting_facts")


class SomeDimension(Base):
    __tablename__ = "some_dimension"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20))

    interesting_facts = relationship("InterestingFact", back_populates="some_dimension")
