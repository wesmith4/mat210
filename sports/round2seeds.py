# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <a href="https://colab.research.google.com/github/wesmith4/mat210/blob/main/sports/round2seeds.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

pageContainer = st.beta_container()
with pageContainer:
    left_col, right_col = st.beta_columns(2)

with left_col:
    main = st.beta_container()
    main.title('Measuring the Madness')
    main.write("Looking at the average seeds of teams that have made the second round.")

# %%
def getWinners(round):
    games = round.findChildren('div', recursive=False)
    
    seeds = []
    for game in games:
        teams = game.findChildren('div', recursive=False)
        for team in teams:
            seeds.append(int(team.find('span').string))
    return seeds


@st.cache
# %%
def getRound2Seeds(year):
    pageaddress = "https://www.sports-reference.com/cbb/postseason/{}-ncaa.html".format(year)
    soup = BeautifulSoup(urlopen(pageaddress), "html.parser")
    bracketDiv = soup.find_all('div', {'id': 'brackets'})[0]
    print('Finding teams from {}'.format(year))
       
    allWinners = []
    for region in range(4):
        bracket = bracketDiv.findChildren('div',recursive=False)[region].find_all('div', {'class': 'round'})[1]
        allWinners.extend(getWinners(bracket))
    allWinners = np.array(allWinners)
    
    return allWinners
    


# %%
allRound2Seeds = np.zeros((len(range(1990,2022)),32))
counter = 0
for year in range(1990,2022):
    if not year == 2020:
        allRound2Seeds[counter] = getRound2Seeds(year)
    counter += 1
allRound2Seeds = allRound2Seeds.astype(int)


# %%
df = pd.DataFrame(allRound2Seeds)
means = np.mean(df, axis=1)
variances = np.var(df,axis=1)


# %%
stats = pd.DataFrame(range(1990,2022),columns=['year'])
stats['avg_seed'] = means
stats['variance'] = variances
stats = stats.set_index('year')
stats = stats.drop([2020])


# %%
fig, ax = plt.subplots()
ax.scatter(stats.index, stats.avg_seed)

z = np.polyfit(stats.index, stats.avg_seed, 1)
p = np.poly1d(z)
ax.plot(stats.index,p(stats.index),"r--")
plt.title('Average Seed of 2nd Round Teams')

main.pyplot(fig)

# %%
sortByMean = stats.sort_values(by='avg_seed',ascending=False).head()


# %%
sortByVar = stats.sort_values(by='variance',ascending=False).head()


# %%
with right_col:
    sideContainer = st.beta_container()
    sideContainer.dataframe(stats)

# sortByMean
# sortByVar

