import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

class MarketBasketModel:
    def __init__(self, min_support=0.01, metric="lift", min_threshold=1):
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
        self.rules = association_rules(frequent_itemsets, metric=self.metric, min_threshold=self.min_threshold)

    def get_recommendations(self, product):
        product = product.lower().strip()  # Clean the input and convert to lowercase
        if product not in self.products:
            return None
        recommendations = self.rules[self.rules['antecedents'].apply(lambda x: product in x)]
        if recommendations is not None and not recommendations.empty:
            # Extract only the consequents and ensure they are unique
            unique_recommendations = set([list(row['consequents'])[0] for _, row in recommendations.iterrows()])
            return unique_recommendations
        return None
