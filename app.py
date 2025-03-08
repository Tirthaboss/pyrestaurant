# Import python module 
import streamlit as st
#A restaurant management system in python.

#Difine the menu of restaurant 
menu = {
  "Pizza":40,\n
  "Pasta":50,\n
  "Burger":60,\n
  "Salad":70,\n
  "Coffee":80
}

#Greet
st.write("Welcome to Pyrestaurant")
#Print menu
st.write("""
   Pizza:Rs-40
   Pasta:Rs-50
   Burger:Rs-60
   Salad:Rs-70
   Coffee:Rs-80
""")
