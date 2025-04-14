import streamlit as st

# Título do app
st.set_page_config(page_title="Calculadora de Consumo de Ar-Condicionado", layout="centered")
st.title("❄ Calculadora de Consumo de Ar-Condicionado")
st.markdown("Estime o consumo mensal do ar-condicionado com base no EER e no Inmetro.")

# Campos de entrada
potencia = st.number_input("Potência do ar-condicionado (W)", min_value=0.0, value=1000.0, step=100.0)
eer = st.number_input("Taxa de eficiência energética (EER)", min_value=0.1, value=3.0, step=0.1)
consumo_anual = st.number_input("Consumo anual informado pelo Inmetro (kWh/ano)", min_value=0.0, value=400.0, step=10.0)
btus = st.number_input("Capacidade do ar-condicionado (BTUs)", min_value=0.0, value=9000.0, step=500.0)
horas_uso = st.number_input("Horas de uso diário", min_value=0.0, value=8.0, step=0.5)

# Botão de cálculo
if st.button("Calcular Consumo"):
    # Cálculo com base no EER
    potencia_kw_eer = (btus / eer) / 3412
    consumo_mensal_eer = potencia_kw_eer * horas_uso * 30

    # Cálculo com base no Inmetro
    consumo_mensal_inmetro = consumo_anual / 12

    # Média entre os dois métodos
    consumo_mensal_medio = (consumo_mensal_eer + consumo_mensal_inmetro) / 2

    # Exibição dos resultados
    st.subheader("🔍 Resultados:")
    st.write(f"*Consumo mensal estimado com base no EER:* {consumo_mensal_eer:.2f} kWh/mês")
    st.write(f"*Consumo mensal com base no Inmetro:* {consumo_mensal_inmetro:.2f} kWh/mês")
    st.success(f"*Média estimada:* {consumo_mensal_medio:.2f} kWh/mês")

    st.markdown("---")
    st.caption("Desenvolvido por Luciano & ChatGPT — Liberty Energia Solar")