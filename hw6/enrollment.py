# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <a href="https://colab.research.google.com/github/wesmith4/mat210/blob/main/hw6/problem3-4.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

# # Problem 3
def app():
    # Transition matrix
    A = np.array([[.15, 0, 0, 0], [.60, .15, 0, 0],
                [0, .8, 1, 0], [.25, .05, 0, 1]])
    st.write(A)

    st.markdown("## Transition Matrix")
    st.latex(r'''
    \mathbf{A} = \begin{bmatrix}.15 & 0 & 0 & 0 \\ .60 & .15 & 0 & 0 \\ 0 & .80 & 1 & 0 \\ .25 & .05 & 0 & 1 \end{bmatrix}
    ''')
    
    # ## Probability that a freshman will graduate

    # Set initial state
    v0 = np.array([[1], [0], [0], [0]])

    # print(np.linalg.matrix_power(A,10)@v0)
    # print(np.linalg.matrix_power(A,50)@v0)
    print(np.linalg.matrix_power(A, 400)@v0)

    # ## Probability that a sophomore will graduate

    v0 = np.array([[0], [1], [0], [0]])

    print(np.linalg.matrix_power(A, 400)@v0)

    # # Problem 4
    
    st.markdown("## New transition matrix like Leslie matrix")
    st.latex(r'''
    \mathbf{A} = \begin{bmatrix}.15 & .80\beta & 0 & 0 \\ .60 & .15 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ .25 & .05 & 0 & 1 \end{bmatrix}
    ''')
    
    beta = 1.505
    beta = st.slider(label="Beta",min_value=1.0,max_value=2.0,value=1.505,step=.001,format="%f")

    L = np.array([[.15, beta*.80, 0, 0], [.60, .15, 0, 0],
                [0, 0, 1, 0], [.25, .05, 0, 1]])
    st.write(L)


    v0 = np.array([[1000], [1000], [0], [0]])


    data = np.zeros((50, 4))
    for n in range(50):
        vn = np.linalg.matrix_power(L, n)@v0
        data[n] = vn.reshape((1, 4))

    populations = data[:, 0:2]
    populations = pd.DataFrame(populations)
    populations['Total'] = np.sum(populations, axis=1)
    populations = populations.rename(columns={0: 'Freshmen', 1: 'Sophomores'})
    populations['Year'] = populations.index

    populations['Freshmen (%)'] = populations['Freshmen']/populations['Total']*100

    # Plotly bar chart
    dat = populations[['Year','Freshmen','Sophomores']].melt(id_vars=['Year'],value_vars=['Freshmen','Sophomores'],var_name='Class',value_name='Students')
    fig = px.bar(dat,x='Year',y='Students',color='Class',title="Enrollment by Class Year over Times")
    fig.update_xaxes(tick0=0,dtick=5)
    fig.update_layout(hovermode='x')
    st.plotly_chart(fig)

    # Plotly line chart
    fig2 = px.line(populations,x='Year',y='Freshmen (%)',title="Freshmen share of Student Body")
    fig2.update_layout(hovermode='x')
    st.plotly_chart(fig2)
