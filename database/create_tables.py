from base import Base, engine
from tables import Fact_Transactions, Dim_Category, Dim_Date, Dim_Merchant

# Create the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)