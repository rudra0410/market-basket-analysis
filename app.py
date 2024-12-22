import streamlit as st
import pandas as pd
from market_basket_model import MarketBasketModel

# Set up Streamlit app layout
st.set_page_config(page_title="Market Basket Analysis", layout="wide")
st.title("Market Basket Analysis")
st.write("Discover products that are frequently bought together.")

# Initialize the model
model = MarketBasketModel(min_support=0.01, metric="confidence", min_threshold=0.5)
data = model.load_data('data/data_transactions.csv')
try:
    model.train(data)
except Exception as e:
    st.error(f"Error training the model: {str(e)}")

# Input section
product = st.text_input("Enter a product to get recommendations (e.g., 'milk', 'bread', 'butter'):").lower().strip()

# Display recommendations
if st.button("Get Recommendations"):
    if product:
        if product not in model.products:
            st.warning(f"Product '{product}' not found in the dataset.")
        else:
            recommendations = model.get_recommendations(product)
            if recommendations is not None and not recommendations.empty:
                st.subheader(f"Recommendations for '{product}':")
                for _, row in recommendations.iterrows():
                    consequent = list(row['consequents'])[0]
                    confidence = row['confidence'] * 100  # Convert to percentage
                    st.write(f"**{consequent}** with a confidence of **{confidence:.2f}%**")
            else:
                st.warning(f"No recommendations found for '{product}'.")
    else:
        st.error("Please enter a product.")

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
