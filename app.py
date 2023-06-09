import streamlit as st
import pandas as pd
import numpy as np
#from sklearn.svm import SVC
#from sklearn.linear_model import LogisticRegression
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.preprocessing import LabelEncoder
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import plot_confusion_matrix, plot_roc_curve_, plot_precision_recall
#from sklearn.metrics import precision_score, recall_score



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

    # Train / test split
    @st.cache_data(persist=True)
    #def split(df):
    #    y = df ['Class']
    #    X = df.drop('Class', axis = 1)
    #    X_train, X_test, y_train, y_test = train_test_split(
    #        X, y,
    #        test_size = 0.2,
    #        random_state = seed,
    #        stratify = y
    #    )
    #    return X_train, X_test, y_train, y_test 

    #X_train, X_test, y_train, y_test = split(df)

if __name__ == '__main__':
     main()