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

# Initialize session state for order total and items
if 'order_total' not in st.session_state:
    st.session_state.order_total = 0
if 'order_items' not in st.session_state:
    st.session_state.order_items = []

# Get input order
item_1 = st.text_input("Enter Your order (type the item name)")

if st.button("Add to Order"):
    if item_1 in menu:
        st.session_state.order_total += menu[item_1]
        st.session_state.order_items.append(item_1)
        st.write(f"Your item '{item_1}' has been added to your order.")
    else:
        st.write("Sorry, that item is not on the menu.")

# Display the current order items and total amount
if st.session_state.order_items:
    st.write("Your current order items:")
    for item in st.session_state.order_items:
        st.write(f"- {item}")
    st.write(f"Your current order total is: Rs-{st.session_state.order_total}")
else:
    st.write("You have not added any items to your order yet.")
