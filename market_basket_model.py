import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

class MarketBasketModel:
    def __init__(self, min_support=0.01, metric="confidence", min_threshold=0.5):
        self.min_support = min_support
        self.metric = metric
        self.min_threshold = min_threshold
        self.rules = None
        self.products = None

    def load_data(self, filepath):
        data = pd.read_csv(filepath, index_col=0)
        self.products = [col.lower() for col in data.columns]  # Convert column names to lowercase
        data.columns = self.products  # Update columns to lowercase
        data = data.astype(bool).astype(int)  # Convert data to binary format
        return data

    def train(self, data):
        frequent_itemsets = apriori(data, min_support=self.min_support, use_colnames=True)
        if frequent_itemsets.empty:
            raise ValueError("No frequent itemsets found. Consider lowering the min_support value.")
        
        # Calculate num_itemsets
        num_itemsets = len(frequent_itemsets)
        
        # Pass num_itemsets to association_rules
        self.rules = association_rules(frequent_itemsets, metric=self.metric, min_threshold=self.min_threshold, num_itemsets=num_itemsets)

    def get_recommendations(self, product):
        product = product.lower().strip()  # Clean input
        if self.rules is None or self.rules.empty:
            return None  # No rules available
        if product not in self.products:
            return None  # Product not in dataset
        try:
            recommendations = self.rules[self.rules['antecedents'].apply(lambda x: product in list(x))]
            return recommendations if not recommendations.empty else None
        except KeyError:
            return None  # Handle cases where 'antecedents' is missing
