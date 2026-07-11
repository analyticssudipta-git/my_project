import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_dummy_mortgage_data(n=100):
    np.random.seed(42)
    data = {
        "Loan_ID": [f"WF{1000+i}" for i in range(n)],
        "Customer_ID": [f"CUST{i:03d}" for i in range(n)],
        "Loan_Amount": np.random.randint(100000, 500000, n),
        "Interest_Rate": np.round(np.random.uniform(3.5, 8.5, n), 2),
        "Loan_Term": np.random.choice([15, 20, 25, 30], n),
        "Property_Type": np.random.choice(["Residential", "Commercial"], n, p=[0.8, 0.2]),
        "State": np.random.choice(["CA", "TX", "FL", "NY", "NC"], n),
        "Origination_Date": [datetime(2015,1,1) + timedelta(days=np.random.randint(0,3000)) for _ in range(n)],
        "Current_Balance": np.random.randint(50000, 450000, n),
        "Delinquency_Flag": np.random.choice([0,1], n, p=[0.9,0.1])
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = create_dummy_mortgage_data()

    # ✅ Ensure 'data' folder exists
    os.makedirs("data", exist_ok=True)

    # ✅ Save file inside 'data'
    df.to_excel("data/mortgage_dummy.xlsx", index=False)
    print("Dummy mortgage data created successfully!")
