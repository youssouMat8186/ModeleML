import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title("Application de machine learning pour la détection de fraude par carte bancaire")
    st.subheader("Auteur : Youssoupha Marega")
    
    # Fonction d'importation des données

    # Pour sauvegarder une variable en mémoire st.cache
    @st.cache_data(persist=True)
    def load_data():
        data = pd.read_csv('creditcard.csv')
        return data
    
    # Affichage de la table de données
    df = load_data()
    df_sample = df.sample(100)
    #st.write(df)

    #st.sidebar pour aller dans la barre laterale
    if st.sidebar.checkbox("Afficher les données brutes", False):
        st.subheader("Jeu de données 'creditcard' : Echantillon de 100 observations")
        st.write(df_sample)
    
    seed = 123

   

if __name__ == '__main__':
    main()
