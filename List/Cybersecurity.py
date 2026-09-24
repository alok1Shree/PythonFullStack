#Detecting Fraudulent Transactions in Financial Data

daily_transactions = [450.00, 1200.00, 15.75, 3000.00, 9.99, 29.99, 49.95, 19.99, 5000.00, 5001.00, 7500.00, 10000.00]
flagged_fraud_alerts = []

for transaction in daily_transactions:
    if transaction > 5000.00:
        flagged_fraud_alerts.append(transaction)

print("Flagged Fraud Alerts:", flagged_fraud_alerts)