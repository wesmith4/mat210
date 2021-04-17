# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Problem 3
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
import os
from sklearn.preprocessing import normalize


def app():
    st.title("NBA Player Clustering")
    st.write("See how your favorite NBA players fit into clusters according to their shooting, rebounds, steals, blocks, and minutes played.")

    dataFile = os.path.join(os.path.dirname(__file__),'perGameStats.csv')
    df = pd.read_csv(dataFile)
    df[['Player','handle']] = df['Player'].str.split('\\',expand=True)
    df = df[df['Tm'] != 'TOT']
    df = df.reset_index(drop=True)

    for index,row in df.iterrows():
        if len(np.where(df['Player'] == row['Player'])[0]) > 1:
            for ind in np.where(df['Player'] == row['Player'])[0]:
                df.loc[ind,'Player'] = '{} ({})'.format(df.loc[ind,'Player'], df.loc[ind,'Tm'])

    # Select desired fields
    data = df[['MP','2PA','2P','3PA','3P','FTA','FT','TRB','STL','BLK','TOV']]
    data_scaled = normalize(data)
    data_scaled = pd.DataFrame(data_scaled,columns=data.columns)

    numberOfClusters = 50
    kmeansCluster = KMeans(n_clusters=numberOfClusters,random_state=42)
    kmeansCluster.fit(data_scaled)

    yourPlayer = st.selectbox('Select a Player',options=df['Player'],index=128)
    
    def getCluster(player):
        indexOfYourPlayerInDataFrame = np.where(df['Player']==player)[0][0]

        clusterOfPlayer = kmeansCluster.labels_[indexOfYourPlayerInDataFrame]
        index = np.where(kmeansCluster.labels_ == clusterOfPlayer)[0]
        return index
    
    index = getCluster(yourPlayer)

    st.write("Here's the cluster:")
    st.write(df.iloc[index])

if __name__ == "__main__":
    app()
