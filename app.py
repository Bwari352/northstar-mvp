import streamlit as st
from logic import check_order_status, process_return_info, check_stock

# Page Configuration
st.set_page_config(page_title="Northstar Support Hub", page_icon="🛍️")

# Header & Branding
st.title("🛍️ Northstar Retail Support")
st.write("Welcome! Select your request below for instant help.")

# Navigation Tabs for Categories
tab1, tab2, tab3 = st.tabs(["📦 Order Status", "🔄 Returns & Refunds", "🏷️ Stock Check"])

# TAB 1: Order Status
with tab1:
    st.subheader("Where is my order?")
    order_id_input = st.text_input("Enter your Order ID (e.g., ORD1001, ORD1002):", key="status_id")
    
    if st.button("Track Order"):
        if order_id_input:
            response = check_order_status(order_id_input)
            st.info(response)
        else:
            st.warning("Please enter a valid Order ID.")

# TAB 2: Returns & Refunds
with tab2:
    st.subheader("Process a Return or View Policy")
    return_id_input = st.text_input("Enter your Order ID for Returns:", key="return_id")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Check Return Eligibility"):
            if return_id_input:
                response = process_return_info(return_id_input)
                st.success(response)
            else:
                st.warning("Please enter an Order ID.")
    with col2:
        if st.button("View General Return Policy"):
            response = process_return_info("")
            st.write(response)

# TAB 3: Stock Availability
with tab3:
    st.subheader("Check Item Availability")
    prod_input = st.selectbox("Select Product:", ["Running Shoes", "Denim Jacket", "Wireless Headphones"])
    size_input = st.text_input("Enter Size (e.g., Size 10, S, M, Standard):", value="Size 10")
    
    if st.button("Check Stock"):
        response = check_stock(prod_input, size_input)
        st.write(response)