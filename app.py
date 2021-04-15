import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import numpy as np
import pandas as pd

st.set_page_config(page_title="MAT210 - Will Smith")


import hw6.enrollment as enrollment
import hw8.NBAclustering as NBAclustering

PAGES = {
    "School Enrollment": enrollment,
    "NBA Clustering": NBAclustering
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()),index=1)
page = PAGES[selection]
page.app()

