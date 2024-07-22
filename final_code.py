import streamlit as st
import pandas as pd
import hashlib

# Sample user data (replace with a real database in production)
users = {
    "user@example.com": {
        "password": hashlib.sha256("password".encode()).hexdigest(),
        "recipes": []
    }
}

def main():
    st.title("Welcome to My Recipe Website")

    menu = ["Home", "Login", "Sign Up", "Add Recipe", "View Recipes"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home_page()

    elif choice == "Login":
        login_page()

    elif choice == "Sign Up":
        signup_page()

    elif choice == "Add Recipe":
        add_recipe_page()

    elif choice == "View Recipes":
        view_recipes_page()


def home_page():
    st.subheader("Discover and Share Your Favorite Recipes")
    st.image("https://via.placeholder.com/800x400.png?text=Delicious+Recipes", use_column_width=True)
    st.write("""
        Welcome to our recipe website! Whether you're a seasoned chef or just starting out in the kitchen,
        our platform offers a wide variety of recipes for every taste and occasion.
    """)
    st.write("### Features:")
    st.write("""
    - **Browse Recipes**: Explore our extensive collection of recipes from various cuisines.
    - **Add Your Own Recipes**: Share your culinary creations with our community.
    - **Save Your Favorites**: Keep track of recipes you love and want to try later.
    - **Interactive Charts**: Visualize your cooking data with interactive charts using Plotly.
    """)
    st.write("### Get Started:")
    st.write("""
    - **Sign Up**: Create an account to save your favorite recipes and add your own.
    - **Explore**: Browse our collection of recipes and start cooking.
    """)
    if st.button("Sign Up Now"):
        st.session_state["menu"] = "Sign Up"


def login_page():
    st.subheader("Login to Your Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if email in users and users[email]["password"] == hashed_password:
            st.success(f"Welcome back, {email}!")
            st.session_state["email"] = email
            st.session_state["menu"] = "Home"
        else:
            st.error("Invalid email or password")


def signup_page():
    st.subheader("Create a New Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    if st.button("Sign Up"):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if email not in users:
            users[email] = {"password": hashed_password, "recipes": []}
            st.success("Account created successfully!")
            st.session_state["email"] = email
            st.session_state["menu"] = "Home"
        else:
            st.error("Email already exists")


def add_recipe_page():
    st.subheader("Add a New Recipe")
    if "email" not in st.session_state:
        st.error("Please login to add a recipe")
        return

    title = st.text_input("Recipe Title")
    description = st.text_area("Recipe Description")
    ingredients = st.text_area("Ingredients")
    instructions = st.text_area("Instructions")
    if st.button("Add Recipe"):
        email = st.session_state.get("email")
        users[email]["recipes"].append({
            "title": title,
            "description": description,
            "ingredients": ingredients,
            "instructions": instructions
        })
        st.success("Recipe added successfully!")


def view_recipes_page():
    st.subheader("View Recipes")
    if "email" not in st.session_state:
        st.error("Please login to view your recipes")
        return

    email = st.session_state["email"]
    recipes = users[email]["recipes"]
    if recipes:
        for recipe in recipes:
            st.write(f"### {recipe['title']}")
            st.write(recipe['description'])
            st.write("#### Ingredients")
            st.write(recipe['ingredients'])
            st.write("#### Instructions")
            st.write(recipe['instructions'])
    else:
        st.info("No recipes found")

if __name__ == "__main__":
    main()
