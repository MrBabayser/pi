# ***********************************************************************************************
# Nom ......... : pi.py
# Rôle ........ : réalisation de l'exercice 4.3 du cours OC sur streamlit
# Auteur ...... : Georges Miot
# Version ..... : V0.2 du 28/08/2022
# Licence ..... : réalisé dans le cadre du cours de OC
# Usage : Pour exécuter : streamlit run https://github.com/MrBabayser/datepi/blob/main/pi.py
#************************************************************************************************/
 
import streamlit as st
from sympy import pi
import datetime

def trouve_date(date, texte) :
  st.text("Rercherche de : " + date)
  if texte.find(date) >= 0 :
    st.text("Trouvé !")
  else :
    st.text("Pas trouvé !")

def jour(nb):
  switcher={
    0:'Lundi',
    1:'Mardi',
    2:'Mercredi',
    3:'Jeudi',
    4:'Vendredi',
    5:'Samedi',
    6:'Dimanche'
      }
  return switcher.get(nb,"Jour invalide")

def somme_texte(texte) :
  somme = 0
  for nb in texte :
    somme += int(nb)
  return somme

st.title("Consigne 1")
st.header("Créez une Application Streamlit (la même que 4.2 ou une autre) qui recherche dans le premier million de décimales de PI la présence d'une date de naissance saisie par l'utilisateur.")
date = st.date_input("Entrez votre date de naissance : ", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2030, 12, 31))
d = str(date)
nbpi = str(pi.evalf(10**6)) # 1 million de décimal de PI
date1 = d[8:10] + d[5:7] + d[0:4] # date au format jjmmaaaa
trouve_date(date1, nbpi)
date2 = d[8:10] + d[5:7] + d[2:4] # date au format jjmmaa
trouve_date(date2, nbpi)

st.title("Consigne 2")
st.header("Dans un champ texte, après l'avoir calculé avec Python ou obtenu en ligne, affichez le jour de naissance correspondant.")
date3 = d[8:10] + "/" + d[5:7] + "/" + d[0:4] # date au format jj/mm/aaaa
st.text("Le " + date3 + " est un " + jour(date.weekday()))

st.title("Consigne 3")
st.header("Dans un autre champ texte, calculez la somme des 20 premières décimales de PI, puis dans un second la somme des 12^2 premières décimales ? Que remarquez-vous ?")
vdecpi = nbpi[2:22]
somme_vdecpi = somme_texte(vdecpi)
st.text("Les 20 premières décimales de PI sont : " + vdecpi)
st.text("La somme des 20 premières décimales de PI est : " + str(somme_vdecpi))
st.text("La somme des 12² premières décimales de PI est : " + str(somme_texte(nbpi[2:12**2])))

st.title("Consigne 4")
st.header("Insérez dans votre application une vidéo prise en ligne qui montre que la somme de tous les nombres entiers naturels est égal à -1/12.")



