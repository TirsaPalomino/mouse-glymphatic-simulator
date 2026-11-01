import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Simulador Glinfático y TREM2 en Roedores", layout="wide")

st.title("🧠 Simulador del Sistema Glinfático y Dinámica Microglial (Zhao et al., 2023; Xie et al., 2013)")
st.markdown("""
Esta herramienta interactiva modela dos descubrimientos clave de la neurociencia en roedores:
1. **La expansión del espacio extracelular y el flujo glinfático** durante el sueño profundo (*Xie et al., 2013*).
2. **La acumulación de beta-amiloide y daño lisosomal** bajo privación crónica de sueño evaluada en 6 grupos de ratones según el genotipo y la vía TREM2 (*Zhao et al., 2023*).
""")

tab1, tab2 = st.tabs(["🔬 Fase 1: Biofísica del Sueño (Espacio Glinfático)", "🐀 Fase 2: Matriz Experimental por Grupos (Zhao et al., 2023)"])

with tab1:
    st.header("Dinámica Celular: Vigilia vs. Sueño Profundo")
    st.markdown("Basado en el estudio de imagen de dos fotones en ratones (*Xie et al., 2013*), el volumen del espacio intersticial se expande drásticamente durante el sueño para permitir el aclaramiento de toxinas.")
    
    estado_sueño = st.radio("Selecciona el estado del ratón:", ["Vigilia / Privación de Sueño", "Sueño Profundo (N3 / SWS)"])
    
    if estado_sueño == "Vigilia / Privación de Sueño":
        st.warning("⚠️ **Estado de Vigilia o Privación:** Las neuronas y astrocitos están expandidos. El espacio extracelular se reduce (~14-15%). La resistencia al flujo es alta y el líquido cefalorraquídeo (LCR) **no fluye eficientemente**.")
        volumen_isv = 15
        eficiencia_flujo = "Muy Baja (Aclaramiento bloqueado)"
    else:
        st.success("✨ **Estado de Sueño Profundo:** Las células se contraen, expandiendo el espacio extracelular hasta un **~60%**. Los canales AQP4 en los astrocitos facilitan el paso masivo de LCR barriendo metabolitos de desecho.")
        volumen_isv = 60
        eficiencia_flujo = "Máxima (Flujo advectivo activo)"
        
    st.metric(label="Volumen Estimado del Espacio Intersticial (ISV)", value=f"{volumen_isv}%")
    st.metric(label="Eficiencia del Aclaramiento Glinfático", value=eficiencia_flujo)

with tab2:
    st.header("Simulación por Grupos de Ratones y Privación Crónica")
    st.markdown("Selecciona las condiciones experimentales del estudio de Zhao et al. (2023) para observar el impacto en la acumulación de beta-amiloide y los lisosomas de la microglía.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        grupo_raton = st.selectbox("Selecciona el Grupo Experimental:", [
            "Grupo 1: Alzheimer 5xFAD + Antena Normal (TREM2+/+)",
            "Grupo 2: Alzheimer 5xFAD + Antena Defectuosa (R47H)",
            "Grupo 3: Alzheimer 5xFAD + Sin Antena (Knockout / TREM2-/-)",
            "Grupo 4: Sano (Wild-Type) + Antena Normal",
            "Grupos 5 & 6: Sano (Wild-Type) + Antena Defectuosa o Sin Antena"
        ])
        
    with col2:
        semanas_privacion = st.slider("Semanas de Privación de Sueño:", 1, 6, 6)
        
    if st.button("Ejecutar Simulación del Grupo"):
        st.subheader("📊 Resultados Histológicos y Moleculares Obtenidos:")
        
        if "Grupo 1" in grupo_raton:
            st.error("🚨 **Resultado Crítico (Grupo 1):** Las placas de Beta-amiloide **se duplicaron (~200%)**. Los lisosomas (estómagos celulares) de la microglía colapsaron y se deformaron severamente debido al sobreesfuerzo energético inducido por la falta de descanso.")
            st.markdown("**Explicación:** La privación crónica genera un colapso energético; la 'antena' (TREM2) detecta la alerta y fuerza a la célula a sobretrabajar, agotando su capacidad y disparando el amiloide.")
        elif "Grupo 2" in grupo_raton:
            st.info("⚠️ **Resultado del Grupo 2 (Mutación R47H):** No se acumuló basura extra de forma acelerada a pesar de la privación de sueño.")
            st.markdown("**Explicación:** Al tener una antena defectuosa, las células microgliales se vuelven 'ciegas' y pierden su función fagocítica. Aunque no hay un colapso inmediato, la basura toxica se acumula silenciosamente año tras año sin que la célula responda.")
        elif "Grupo 3" in grupo_raton:
            st.info("⚠️ **Resultado del Grupo 3 (Knockout / Sin TREM2):** La privación de sueño no incrementó de manera extrema los depósitos en comparación con el Grupo 1.")
            st.markdown("**Explicación:** Demuestra que para que la privación de sueño active el daño destructivo en el modelo de Alzheimer, la microglía requiere estrictamente de la señalización funcional de TREM2.")
        elif "Grupo 4" in grupo_raton:
            st.warning("⚠️ **Resultado del Grupo 4 (Sano con Antena Normal):** Se observó daño celular directo: los lisosomas se hincharon, deformaron y perdieron sus enzimas digestivas.")
            st.markdown("**Explicación:** No se necesita tener Alzheimer; la privación crónica de sueño por sí sola hace que los 'estómagos celulares' de un cerebro sano fallen por completo.")
        else:
            st.success("✅ **Resultado Grupos 5 & 6 (Sano sin/con defecto en TREM2):** Las células de limpieza se mantuvieron protegidas contra el colapso inducido por la falta de sueño.")
            st.markdown("**Explicación:** Confirma que TREM2 actúa como el enlace molecular crítico que conecta la falta de descanso con el estrés celular y lisosomal.")
