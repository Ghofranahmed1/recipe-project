#import streamlit as st
import pandas as pd
from data import add_recipe, get_recipes

st.title("Recipe Web Application")

menu = ["Home", "Add Recipe", "View Recipes"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Recipe App!")
    st.write("This is a simple app to manage your recipes.")

elif choice == "Add Recipe":
    st.subheader("Add a New Recipe")
    title = st.text_input("Title")
    description = st.text_area("Description")
    ingredients = st.text_area("Ingredients")
    instructions = st.text_area("Instructions")
    
    if st.button("Add Recipe"):
        add_recipe(title, description, ingredients, instructions)
        st.success(f"Recipe '{title}' added successfully!")

elif choice == "View Recipes":
    st.subheader("View Recipes")
    recipes = get_recipes()
    st.dataframe(recipes)
