import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import colors

st.header("Line graph of random numbers")

df = pd.DataFrame({'y': np.random.rand(100)})

st.write("Here's the head of the dataframe I'll be charting", df.head())

color_choices = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
color = st.selectbox("Please select a color for the line", options = color_choices)
st.write("you picked", color, " aka ", colors.to_rgba(color))

st.line_chart(df, y="y", color=colors.to_rgba(color))

st.write("Github repo [here](https://github.com/arilamstein/day9)")