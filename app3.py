import streamlit as st
import pickle
### python --version
### La version de pickle est la version de python
#st.write(pickle.__version__)

# Charger le modèle préalablement entraîné
loaded_model = pickle.load(open('iris_model.pkl', 'rb'))

# Fonction pour effectuer des prédictions
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    new_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = loaded_model.predict(new_data)
    return prediction[0]

# Interface utilisateur Streamlit
def main():
    # Titre de l'application
    st.title("Prédiction de la classe d'une fleur Iris")

    # Saisie des caractéristiques de la fleur
    sepal_length = st.number_input("Longueur du sépale")
    sepal_width = st.number_input("Largeur du sépale")
    petal_length = st.number_input("Longueur du pétale")
    petal_width = st.number_input("Largeur du pétale")

    # Bouton de prédiction
    if st.button("Prédire"):
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width)
        st.write(f"Classe prédite : {prediction}")

# Appel de la fonction principale
if __name__ == "__main__":
    main()
