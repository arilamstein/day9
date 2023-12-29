import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import colors

st.header("Line graph of random numbers")

df = pd.DataFrame({'y': np.random.rand(100),
                   'z': np.random.rand(100)})
st.write("Here's the head of the dataframe I'll be charting", df.head())

st.write("The values are all in [0, 1]. Shall is add 1 to each value of `z` to separate them?")
add_to_z = st.checkbox("Add 1 each value of `z`", value = True)
if add_to_z:
    df['z'] = df['z'] + 1

color_choices = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
line_colors = st.multiselect("Please select colors for the lines", 
                       options = color_choices, 
                       default = ['Red', 'Blue'],
                       max_selections=2)

# If user selected only 1 color, use that color for both lines
if len(line_colors) == 1:
    line_colors = [line_colors[0], line_colors[0]]
line_colors_rgb = [colors.to_rgb(one_color) for one_color in line_colors]

st.line_chart(df, color=line_colors_rgb)

st.write("Github repo [here](https://github.com/arilamstein/day9)")