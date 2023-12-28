import streamlit as st
import pandas as pd
import numpy as np

st.header("Line graph of random numbers")

df = pd.DataFrame({'y': np.random.rand(100)})

st.write("Here's the dataframe I'll be charting", df.head())

st.write("And here's the chart!")

st.line_chart(df, y="y")

st.write("Github repo [here](https://github.com/arilamstein/day9)")