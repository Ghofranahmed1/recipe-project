import streamlit as st

def main():
    st.title("Welcome to My Recipe Website")

    st.image("https://cdn11.bigcommerce.com/s-hgeca6jj4z/product_images/uploaded_images/carmie-s-kitchen-recipe-picture.png", use_column_width=True)

    st.subheader("Discover and Share Your Favorite Recipes")
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

    st.button("Sign Up Now")

if __name__ == "__main__":
    main()
