# Import python module 
import streamlit as st
#A restaurant management system in python.

#Difine the menu of restaurant 
menu = {
  "Pizza":40,
  "Pasta":50,
  "Burger":60,
  "Salad":70,
  "Coffee":80,
}

#Greet
st.write("Welcome to Pyrestaurant")
#Print menu
st.write("""
   Pizza:Rs-40,\n
   Pasta:Rs-50,\n
   Burger:Rs-60,\n
   Salad:Rs-70,\n
   Coffee:Rs-80
""")
# Order deta 
order_total = 0
#Get input order
item_1 = text_input("Enter Your first order")
if item_1 in menu:
  order_total += menu[item_1]
  st.write(f"Your item {item_1} has been added to yur order")
