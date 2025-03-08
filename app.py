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
   Pizza:Rs-40\n
   Pasta:Rs-50\n
   Burger:Rs-60\n
   Salad:Rs-70\n
   Coffee:Rs-80
""")
