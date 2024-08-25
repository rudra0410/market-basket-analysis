import streamlit as st
import pandas as pd
from market_basket_model import MarketBasketModel

# Set up Streamlit app layout
st.set_page_config(page_title="Market Basket Analysis", layout="wide")
st.title("Market Basket Analysis")
st.write("Discover products that are frequently bought together.")

# Initialize the model
model = MarketBasketModel(min_support=0.02, metric="lift", min_threshold=1)
data = model.load_data('data/data_transactions.csv')
model.train(data)

# Input section
product = st.text_input("Enter a product to get recommendations (e.g., 'milk', 'bread', 'butter'):")

# Display recommendations
if st.button("Get Recommendations"):
    if product:
        recommendations = model.get_recommendations(product)
        if recommendations is not None:
            st.subheader(f"Recommendations for '{product}':")
            for _, row in recommendations.iterrows():
                st.write(f"**{list(row['consequents'])[0]}** with a lift of **{row['lift']:.2f}**")
        else:
            st.warning(f"No recommendations found for '{product}'. Ensure the product is in the dataset.")
    else:
        st.error("Please enter a product name.")

# Footer
st.markdown(
    """
    <hr style="border:1px solid #d1d1d1; margin: 40px 0;">
    <div style="text-align: center;">
        &copy; 2024 Market Basket Analysis. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)

