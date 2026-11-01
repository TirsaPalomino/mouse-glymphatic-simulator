import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Simulador Glinfático y TREM2 en Roedores", layout="wide")

st.title("🧠 Simulador del Sistema Glinfático y Dinámica Microglial")
st.markdown("""
*Basado en los estudios de Xie et al. (2013) y Zhao et al. (2023).* Esta herramienta modela la relación entre el ciclo de sueño, la biofísica del espacio intersticial y la respuesta inmunológica de la microglía (vía TREM2) en modelos de roedores.
""")

tab1, tab2 = st.tabs(["🔬 Fase 1: Simulación Biofísica (Espacio Glinfático)", "🐀 Fase 2: Matriz Experimental de Roedores (Zhao et al., 2023)"])

with tab1:
    st.header("Dinámica del Espacio Intersticial: Vigilia vs. Sueño Profundo")
    st.markdown("Utiliza el selector para observar cómo cambia el volumen del espacio extracelular (ISV) y la eficiencia del flujo de líquido cefalorraquídeo (LCR).")
    
    estado_sueño = st.radio(
        "Selecciona el estado fisiológico del ratón:", 
        ["Vigilia / Privación de Sueño", "Sueño Profundo (N3 / SWS)"]
    )
    
    col_a, col_b = st.columns([1, 1])
    
    if estado_sueño == "Vigilia / Privación de Sueño":
        volumen_isv = 15
        eficiencia = "Baja (Flujo bloqueado)"
        descriction_text = "⚠️ **Estado de Vigilia:** Las neuronas y astrocitos están expandidos. El espacio extracelular se reduce a ~15%, impidiendo el barrido eficiente de toxinas."
        color_grafica = "#ff4b4b"
    else:
        volumen_isv = 60
        eficiencia = "Máxima (Flujo advectivo activo)"
        descriction_text = "✨ **Sueño Profundo:** Las células se contraen, expandiendo el espacio extracelular hasta un 60%. Los canales AQP4 facilitan la limpieza masiva."
        color_grafica = "#00cc96"
        
    with col_a:
        st.info(descriction_text)
        st.metric(label="Volumen del Espacio Intersticial (ISV)", value=f"{volumen_isv}%")
        st.metric(label="Eficiencia del Aclaramiento Glinfático", value=eficiencia)
        
    with col_b:
        # Gráfica interactiva simulando el comportamiento del tejido con Plotly
        fig = go.Figure(go.Bar(
            x=['Espacio Intersticial (ISV)', 'Resistencia al Flujo', 'Aclaramiento de Toxinas'],
            y=[volumen_isv, 100 - volumen_isv, volumen_isv * 1.5],
            marker_color=[color_grafica, '#ffa15a', '#636efa']
        ))
        fig.update_layout(
            title="Métricas Biofísicas del Tejido Cerebral",
            yaxis_range=[0, 100],
            template="plotly_white",
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Panel de Control de Cohortes de Roedores")
    st.markdown("Selecciona el grupo experimental y las semanas de privación de sueño para proyectar el daño celular y la acumulación de amiloide.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        grupo_raton = st.selectbox("Selecciona el Grupo Experimental:", [
            "Grupo 1: Alzheimer 5xFAD + Antena Normal (TREM2+/+)",
            "Grupo 2: Alzheimer 5xFAD + Antena Defectuosa (R47H)",
            "Grupo 3: Alzheimer 5xFAD + Sin Antena (Knockout / TREM2-/-)",
            "Grupo 4: Sano (Wild-Type) + Antena Normal",
            "Grupos 5 & 6: Sano (Wild-Type) + Antena Defectuosa/Knockout"
        ])
        
    with col2:
        semanas_privacion = st.slider("Semanas de Privación Crónica de Sueño:", 1, 6, 6)
        
    st.markdown("---")
    
    # Visualización estilo tarjetas de resultados según el grupo
    if "Grupo 1" in grupo_raton:
        st.error(f"🚨 **[GRUPO 1] Resultado tras {semanas_privacion} semanas:** Carga de Beta-amiloide **duplicada (~200%)**. Colapso severo de los lisosomas microgliales.")
        st.markdown("**Análisis Mecanístico:** El estrés energético provocado por la falta de sueño activa la señal TREM2, forzando a la microglía a un sobretrabajo que colapsa su capacidad digestiva y acelera las placas.")
    elif "Grupo 2" in grupo_raton:
        st.warning(f"⚠️ **[GRUPO 2] Resultado tras {semanas_privacion} semanas:** Ausencia de picos agudos de amiloide, pero acumulación silenciosa a largo plazo.")
        st.markdown("**Análisis Mecanístico:** La mutación R47H deja 'ciega' a la antena TREM2. La célula no colapsa por sobreesfuerzo, pero pierde por completo su función de limpieza.")
    elif "Grupo 3" in grupo_raton:
        st.warning(f"⚠️ **[GRUPO 3] Resultado tras {semanas_privacion} semanas:** Incremento moderado/limitado de depósitos amiloides en comparación con el Grupo 1.")
        st.markdown("**Análisis Mecanístico:** Confirma que la vía TREM2 es estrictamente necesaria para que la privación de sueño desencadene la respuesta destructiva típica del Alzheimer.")
    elif "Grupo 4" in grupo_raton:
        st.error(f"⚠️ **[GRUPO 4] Resultado tras {semanas_privacion} semanas:** Lisosomas hinchados, deformes y pérdida de enzimas digestivas en cerebros sanos.")
        st.markdown("**Análisis Mecanístico:** Demuestra que el daño lisosomal y el estrés celular no son exclusivos del Alzheimer; la privación crónica de sueño por sí sola destruye el sistema de limpieza.")
    else:
        st.success(f"✅ **[GRUPOS 5 & 6] Resultado tras {semanas_privacion} semanas:** Células microgliales protegidas frente al colapso inducido por la falta de descanso.")
        st.markdown("**Análisis Mecanístico:** La ausencia o alteración completa de la vía TREM2 aísla a la célula de la cascada de estrés inflamatorio dependiente del sueño.")
