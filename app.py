import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import numpy as np
import pandas as pd

import hw6.enrollment as enrollment

PAGES = {
    "School Enrollment": enrollment
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})

chart = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
)

st.altair_chart(chart)

