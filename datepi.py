# *****************************************************************************************************
# Nom ......... : datepi.py
# Rôle ........ : cherche dans le premier million de décimales de PI 
# ............. : la présence d'une date de naissance saisie par l'utilisateur
# Auteur ...... : Georges Miot
# Version ..... : V0.2 du 28/08/2022
# Licence ..... : réalisé dans le cadre du cours de OC
# Usage : Pour exécuter : streamlit run https://github.com/MrBabayser/datepi.git
#******************************************************************************************************/
 
import streamlit as st

st.title('Recherche date')
d = st.date_input("Entrez votre date de naissance")
