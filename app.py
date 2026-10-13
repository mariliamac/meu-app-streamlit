import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulador de lançamentos de moeda 🪙")

# Widget para escolher número de lançamentos
num_lancamentos = st.number_input("Quantos lançamentos?", min_value=1, max_value=100, value=10)

# Botão para iniciar
if st.button("Lançar moeda"):
    resultados = np.random.choice([0, 1], size=num_lancamentos)  # 0 = coroa, 1 = cara
    media = np.mean(resultados)

    st.write(f"Média dos resultados: {media:.2f}")

    # Mostrar gráfico
    st.line_chart(resultados)

    # Mostrar tabela
    df = pd.DataFrame({"Resultado": resultados})
    st.write("Tabela de resultados:")
    st.dataframe(df)
