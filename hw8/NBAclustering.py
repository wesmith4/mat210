# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Problem 3
import pandas as pd
import numpy as np
import streamlit as st

def app():
    st.title("NBA Player Clustering")
    st.write("See how your favorite NBA players fit into clusters according to their shooting, rebounds, steals, blocks, and minutes played.")

    dataFile = "hw8/perGameStats.txt"
    df = pd.read_csv(dataFile)
    df.to_csv('{}.csv'.format(dataFile.split('.')[0]))
    df[['Player','handle']] = df['Player'].str.split('\\',expand=True)
    df = df[df['Tm'] != 'TOT']
    df = df.reset_index(drop=True)

    # Select desired fields
    data = df[['MP','2PA','2P','3PA','3P','FTA','FT','TRB','STL','BLK','TOV']]

    numberOfClusters = 50
    from sklearn.cluster import KMeans
    kmeansCluster = KMeans(n_clusters=numberOfClusters)
    kmeansCluster.fit(data)


    # import sys
    # original_stdout = sys.stdout

    # with open('playerClusterKmeans.txt', 'w') as f: 
    #    sys.stdout = f
    #    # Output the clusters
    #    for i in range(numberOfClusters):
    #        index = np.where(kmeansCluster.labels_ == i)[0]
    #        print('\nCluster %d\n' % i)
    #        for j in range(len(index)):
    #            print(df['Player'][index[j]])
    #    sys.stdout = original_stdout


    yourPlayer = 'Stephen Curry'
    yourPlayer = st.selectbox('Select a Player',options=df['Player'],index=128)

    indexOfYourPlayerInDataFrame = np.where(df['Player']==yourPlayer)[0][0]

    clusterOfPlayer = kmeansCluster.labels_[indexOfYourPlayerInDataFrame]
    index = np.where(kmeansCluster.labels_ == clusterOfPlayer)[0]
    st.write('\nk-means cluster')
    st.write('===============')
    for j in range(len(index)):
        st.write(df['Player'][index[j]])


