# Import python module 
import streamlit as st

# A restaurant management system in python.

# Define the menu of restaurant 
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,
}

# Greet
st.write("Welcome to Pyrestaurant")

# Print menu
st.write("""
   **Menu:**
   - Pizza: Rs-40
   - Pasta: Rs-50
   - Burger: Rs-60
   - Salad: Rs-70
   - Coffee: Rs-80
""")

# Order details 
order_total = 0

# Get input order
item_1 = st.text_input("Enter Your first order")

if item_1 in menu:
    order_total += menu[item_1]
    st.write(f"Your item {item_1} has been added to your order.")
if item_1 not in menu:
    st.write("Sorry, that item is not on the menu.")

# Display the total order amount
st.write(f"Your current order total is: Rs-{order_total}")
