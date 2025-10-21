import streamlit as st
import numpy as np
import pickle
import pandas as pd

with open('modelo_cancer.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Diagnóstico de Câncer de mama usando IA")
st.write(" saiba se o cancer é maligno ou benigno  ")

features = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
    "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se", "smoothness_se",
    "compactness_se", "concavity_se", "concave points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst",
    "compactness_worst", "concavity_worst", "concave points_worst", "symmetry_worst", "fractal_dimension_worst"
]

valores = []
for feature in features:
    valor = st.number_input(feature, min_value=0.0, format="%.3f")
    valores.append(valor)

if st.button(" saber resultado:  "):
    dados = np.array([valores])
    resultado = model.predict(dados)[0]
    
    if resultado == 1:
        st.success("de acordo com as informações colocadas: TUMOR BENIGNO")
    else:
        st.error("de acordo com as informações colocadas: TUMOR MALIGNO ")
