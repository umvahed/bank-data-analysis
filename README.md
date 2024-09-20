# Bank Transaction Data Analysis and Default Probability Prediction

This Python project is designed to analyze **bank transaction data** and predict the **probability of default** (PD) for a given customer. It processes **bank data** (such as transactions and account information), unifies different data formats, categorizes transactions, and computes analytics like the probability of a customer defaulting on their financial obligations.

## Features

- **Data Processing**: The program reads transaction data (withdrawals, deposits) from customers, categorizing them and preparing the data for analysis.
- **Predictive Modeling**: Uses a **logistic regression** machine learning model to predict the probability of customer default based on their current balance.
- **Database Integration**: Stores and retrieves customer account and transaction data using an integrated **SQLite** database with **SQLAlchemy**.
- **API Access**: Includes a **Flask** API for easy interaction, allowing clients to input customer balances and receive real-time default probability predictions.
- **User Dashboard (Planned)**: A dashboard for clients to visualize account data, transactions, and default risk statistics.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed. This project also requires the following Python packages:
- `Flask`
- `SQLAlchemy`
- `pandas`
- `scikit-learn`
- `sqlite3`

You can install all necessary packages via:

```bash
pip install -r requirements.txt
```

## Installation

- Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo/bank-data-analysis.git
cd bank-data-analysis

```


