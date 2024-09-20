import pandas as pd
from sklearn.linear_model import LogisticRegression
from flask import Flask, request, jsonify

# Flask API for stateless requests
app = Flask(__name__)

# Sample bank transaction categories
CATEGORIES = {
    "groceries": ["supermarket", "grocery", "mart"],
    "utilities": ["electricity", "water", "gas", "internet"],
    "entertainment": ["movies", "concert", "game", "music"],
    "income": ["salary", "bonus", "income"]
}

# Dummy model for probability of default
def compute_default_probability(balance, transactions):
    # A simple logistic regression model with random data
    X = transactions[["transaction_amount"]]
    y = (transactions["transaction_type"] == "withdrawal").astype(int)  # 1 if withdrawal, else 0
    model = LogisticRegression()
    model.fit(X, y)
    
    # Predict probability of default based on account balance
    default_probability = model.predict_proba([[balance]])[0][1]
    return default_probability

# Function to classify transactions
def classify_transaction(transaction):
    description = transaction.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in description for keyword in keywords):
            return category
    return "other"

# Function to process bank data from a file (CSV format for this example)
def process_bank_data(file_path):
    # Reading CSV into a DataFrame
    data = pd.read_csv(file_path)
    
    # Ensure a standard format
    data.columns = [col.lower() for col in data.columns]
    
    # Classify each transaction into categories
    data["category"] = data["transaction_description"].apply(classify_transaction)
    
    # Compute default probability for each account
    account_balance = data["balance"].iloc[-1]  # Simplified assumption: balance from the last row
    default_probability = compute_default_probability(account_balance, data)
    
    return data, default_probability

# API to process transactions and get analytics
@app.route("/process", methods=["POST"])
def process_transactions():
    # Simulate file upload with 'file' in POST request
    file = request.files["file"]
    
    # Process the file and get results
    transactions, default_prob = process_bank_data(file)
    
    # Convert the processed data to JSON
    response = {
        "classified_transactions": transactions.to_dict(orient="records"),
        "default_probability": default_prob
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
