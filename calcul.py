import streamlit as st
import numpy as np

# Personnalisation de l'apparence
st.set_page_config(page_title="Calculateur de Pension", page_icon="📊", layout="centered")

def set_theme(is_dark_mode):
    if is_dark_mode:
        return """
        <style>
        .main {background-color: #1e1e1e; color: #ffffff; font-family: 'Arial';}
        h1, h2, h3 {color: #3498db;}
        .css-1aumxhk {background-color: #2c3e50;}
        .stTextInput > div > div > input {background-color: #333333; color: #ffffff;}
        .stNumberInput > div > div > input {background-color: #333333; color: #ffffff;}
        .stSelectbox > div > div > select {background-color: #333333; color: #ffffff;}
        </style>
        """
    else:
        return """
        <style>
        .main {background-color: #f0f4f8; color: #333333; font-family: 'Arial';}
        h1, h2, h3 {color: #2c3e50;}
        .css-1aumxhk {background-color: #3498db;}
        </style>
        """

# État pour le mode sombre
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Switch pour le mode sombre
dark_mode = st.sidebar.checkbox("Mode sombre", value=st.session_state.dark_mode)

# Mise à jour du thème
st.markdown(set_theme(dark_mode), unsafe_allow_html=True)


# Titre de l'application
st.title("📊 Calculateur de Pension")

# Explication
st.write("""
    ### Veuillez entrer vos données pour calculer la pension.
    Remplissez les champs ci-dessous avec les contributions de chaque année.
    """)

# Créez une liste pour stocker les entrées
values = []
coefficient = [1.037901, 1.03, 1.032, 1.0308, 1.03, 1.0373, 1.032, 1.0349, 1.0337, 1.0304, 
               1.0316, 1.0346, 1.0312, 1.0298, 1.03, 1.0301, 1.0234, 1.0286, 1.0278, 
               1.0316, 1.014, 1.0132, 1.0274]

# Liste des multiplicateurs pour chaque année
list = []
for i in range(22):
    v = np.prod(coefficient[i+1:])
    list.append(v)
list.append(1)

# Interface pour saisir 23 valeurs
st.subheader("Contributions annuelles")
cols = st.columns(3)  # Diviser l'interface en colonnes

for i in range(23):
    with cols[i % 3]:
        value = st.number_input(f"Contribution année {i + 2002}:", value=1.0, step=1.0)
        values.append(value)

# Calculs
sum = []
for i in range(23):
    a = values[i] * list[i] * 100 / 6
    sum.append(a)

sommes = np.sum(sum)
somme=sommes*0.02/12


# Entrée pour le calcul de P2
st.subheader("Calcul de Pension")
val = st.number_input("P1", value=1.0, step=0.1)
PP = (list[0] * val )/ 12
somme1=somme+PP
# Affichage des résultats

st.success(f"💰 La somme est(P1+P2): **{somme1:.2f}**")
st.info(f"🧮 Pension calculée(P1)  : **{PP:.2f}**")
st.info(f"🧮 Pension calculée(P2)  : **{somme:.2f}**")
