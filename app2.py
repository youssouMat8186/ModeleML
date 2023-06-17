### control + C Pour Stopper l'exécution

import streamlit as  st

import pandas as pd

import numpy as  np

import matplotlib.pyplot  as plt



data = np.random.normal(size= 1000)

data  = pd.DataFrame(data,columns= ["Dist_norm"])

#dat





st.write(data.head())

st.dataframe(data.head())



# Rien ne s'affiche

#plt.hist(data.Dist_norm)

#plt.show()



# Pour Afficher

#st.pyplot()



# Pour enlever le warning



fig, ax = plt.subplots()

ax.hist(data.Dist_norm)

st.pyplot(fig)