import pandas as pd

def calculate_portfolio_metrics(df):
    """
    Calculates key mortgage portfolio metrics.
    WF Analytics Standard:
    - Use clear naming conventions
    - Return dictionary for reporting
    """
    total_loans = len(df)
    avg_interest = df["Interest_Rate"].mean()
    delinquency_rate = df["Delinquency_Flag"].mean() * 100
    avg_balance = df["Current_Balance"].mean()

    summary = {
        "Total Loans": total_loans,
        "Average Interest Rate": round(avg_interest, 2),
        "Delinquency Rate (%)": round(delinquency_rate, 2),
        "Average Current Balance": round(avg_balance, 2)
    }
    return summary


if __name__ == "__main__":
    # Load the dummy data
    df = pd.read_excel("data/mortgage_dummy.xlsx")

    # Calculate metrics
    metrics = calculate_portfolio_metrics(df)

    # Display results
    print("Mortgage Portfolio Summary:")
    for k, v in metrics.items():
        print(f"{k}: {v}")
