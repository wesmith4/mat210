import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import numpy as np
import pandas as pd
import home

st.set_page_config(page_title="MAT210 - Will Smith")


import hw6.enrollment as enrollment
import hw8.NBAclustering as NBAclustering

PAGES = {
    "Home": home,
    "School Enrollment": enrollment,
    "NBA Clustering": NBAclustering
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()),index=0)
page = PAGES[selection]
page.app()

