import streamlit as st

# Titre de l'application
st.title("Calculateur de Produit")

# Demander à l'utilisateur d'entrer deux valeurs
valeur1 = st.number_input("Entrez la première valeur :", step=1.0)
valeur2 = st.number_input("Entrez la deuxième valeur :", step=1.0)

# Calculer le produit
produit = valeur1 * valeur2

# Afficher le résultat
st.write(f"Le produit de {valeur1} et {valeur2} est : {produit}")
