# Market Basket Analysis and Product Recommendation System

## Overview

This project implements a Market Basket Analysis and Product Recommendation System using the Apriori algorithm and association rule learning. The goal is to analyze transaction data to identify associations between products and recommend products that are frequently bought together. The system provides a user-friendly web interface built with Streamlit.

## Features

- **Market Basket Analysis**: Identifies frequent itemsets and association rules from transaction data using the Apriori algorithm.
- **Product Recommendations**: Suggests products that are frequently bought together with the specified product.
- **Streamlit Interface**: Provides an interactive web application for users to input products and receive recommendations.

## Prerequisites

- Python 3.12 or higher
- Virtual environment (recommended)
- Necessary Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/market-basket-analysis.git
   cd market-basket-analysis
   ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

**Data**
The project requires a CSV file named **'data_transaction.csv'** located in the **data** directory. The CSV file should have the following structure:

  **Columns**: Each column represents a product, and each row represents a transaction.
  **Values**: Binary values (0 or 1) indicating whether a product was bought in the transaction.
  Example CSV:
  ```csv
  TransactionID,Bread,Milk,Cheese,Eggs,Yogurt,Butter,Fruits,Vegetables,Meat,Fish,Pasta,Rice,Cereal,Juice,Coffee,Tea,Snacks,Chocolate,Cleaning Supplies,Personal Care
  T0001,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1
  T0002,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0
  T0003,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0
  ...
```

**Usage**
1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    
2. **Open the web application:**
    Go to **'http://localhost:8501'** in your web browser.
    
3. **Get Recommendations:**
    Enter a product name in the input field (e.g., 'milk').
    Click the "Get Recommendations" button to see products that are frequently bought together with the input product.
