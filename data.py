import pandas as pd

# Simulate a database with a DataFrame
data = {
    "Title": [],
    "Description": [],
    "Ingredients": [],
    "Instructions": []
}

# Load data into a DataFrame
df = pd.DataFrame(data)

def add_recipe(title, description, ingredients, instructions):
    global df
    df = df.append({
        "Title": title,
        "Description": description,
        "Ingredients": ingredients,
        "Instructions": instructions
    }, ignore_index=True)

def get_recipes():
    return df
