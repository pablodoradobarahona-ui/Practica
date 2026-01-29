import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Rebajas 3º ESO", page_icon="🛍️")

# Título y descripción
st.title("🏷 Calculadora de Rebajas")
st.markdown("Introduce el precio original y el descuento para saber el precio final.")
st.write("---")

# 2. Entrada de datos (Barra lateral)
st.sidebar.header("Datos del producto")

precio_original = st.sidebar.number_input(
    "Precio original (€)",
    min_value=0.0,
    max_value=1000000.0,
    value=50.0,
    step=0.5
)

descuento = st.sidebar.slider(
    "Descuento (%)",
    min_value=0,
    max_value=99,
    value=20
)

# 3. Botón de cálculo y lógica
if st.button("Calcular ahora"):
    
    # Cálculos
    ahorro = precio_original * descuento / 100
    precio_final = precio_original - ahorro

    # 4. Mostrar resultados con diseño
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Precio final (€)", f"{precio_final:.2f}")

    with col2:
        st.metric("Ahorras (€)", f"{ahorro:.2f}")

        if descuento == 0:
            st.info("ℹ️ No hay descuento aplicado")
        elif descuento < 20:
            st.warning("🟡 no hay mucha diferencia")
        elif descuento < 50:
            st.success("✅ ¡Buen descuento!")
            st.balloons()
        else:
            st.success("🔥 ¡Compralo ya!")

    # Extra: fórmula matemática
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r'''
    Precio\ Final = Precio\ Original - \frac{Precio\ Original \cdot Descuento}{100}
    ''')

