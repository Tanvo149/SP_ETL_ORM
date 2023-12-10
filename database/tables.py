from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import column_property, relationship

from base import Base

class Fact_Transactions(Base):
    __tablename__ = "Fact_Transactions"

    transaction_id = Column(String, primary_key=True)
    customer_id = Column(String, ForeignKey('Dim_Customer.customer_id'))
    date_id = Column(Date)
    category_id = Column(Integer, ForeignKey('Dim_Category.category_id'))
    merchant_id = Column(Integer)
    amount = Column(Float)

    # Define the relationship with Dim_Category
    category = relationship("Dim_Category", back_populates="transactions")
    customer = relationship("Dim_Customer", back_populates="transactions")
    

class Dim_Category(Base):
    __tablename__ = "Dim_Category"

    category_id = Column(Integer, primary_key=True)
    category = Column(String)

    transactions = relationship("Fact_Transactions", back_populates="category")

class Dim_Customer(Base):
    __tablename__ = "Dim_Customer"

    customer_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email_address = Column(String)

    transactions = relationship("Fact_Transactions", back_populates="customer")

class Dim_Merchant(Base):
    __tablename__ = "Dim_Marchant"

    merchant_id = Column(Integer, primary_key=True)
    merchant = Column(Integer)

class Dim_Date(Base):
    __tablename__ = "Dim_Date"

    date_id = Column(Integer, primary_key=True)


    

