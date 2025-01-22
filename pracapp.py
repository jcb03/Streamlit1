import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to my dashboard!")

# Example visualization
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 30]}
df = pd.DataFrame(data)

# Bar Chart
st.write("Here's a bar chart:")
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'])
st.pyplot(fig)
