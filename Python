import streamlit as st
import plotly.graph_objects as go

# Configuración de la página con diseño limpio
st.set_page_config(
    page_title="Simulador Glinfático & TREM2",
    page_icon="🧠",
    layout="wide"
)

# Estilos CSS personalizados para que se vea ultra profesional
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 25px;
    }
    .card-box {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<p class="main-header">🧠 Simulador del Sistema Glinfático y Dinámica Microglial</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Plataforma interactiva basada en los hallazgos de Xie et al. (2013) y Zhao et al. (2023) en modelos de roedores.</p>', unsafe_allow_html=True)

# Pestañas principales con diseño superior
tab1, tab2 = st.tabs(["🔬 Fase 1: Biofísica del Espacio Glinfático", "🐀 Fase 2: Matriz Experimental por Cohortes"])

with tab1:
    st.markdown("### Dinámica del Tejido Cerebral: Vigilia vs. Sueño Profundo")
    st.markdown("Explora cómo cambia físicamente el espacio extracelular y el flujo de líquidos según el estado de descanso (*Xie et al., 2013*).")
    
    col_sel, col_space = st.columns([1, 2])
    with col_sel:
        estado_sueño = st.radio(
            "Selecciona el estado fisiológico:", 
            ["Vigilia / Privación de Sueño", "Sueño Profundo (N3 / SWS)"]
        )
    
    col1, col2 = st.columns(2)
    
    if estado_sueño == "Vigilia / Privación de Sueño":
        volumen_isv = 15
        eficiencia_txt = "Bloqueado (Alta Resistencia)"
        color_hex = "#EF4444" # Rojo moderno
        descripcion = "⚠️ **Estado de Vigilia / Privación:** Las neuronas y astrocitos se encuentran expandidos. El espacio extracelular se reduce drásticamente (~15%), impidiendo el barrido advectivo de metabolitos tóxicos."
    else:
        volumen_isv = 60
        eficiencia_txt = "Máximo (Flujo Advectivo Activo)"
        color_hex = "#10B981" # Verde moderno
        descripcion = "✨ **Estado de Sueño Profundo:** Las células se contraen, expandiendo el espacio extracelular hasta un **60%**. Los canales de Aquaporina-4 (AQP4) facilitan la limpieza masiva de toxinas."

    with col1:
        st.markdown(f"""
            <div class="card-box" style="border-left-color: {color_hex};">
                <h4>📊 Diagnóstico Biofísico</h4>
                <p>{descripcion}</p>
            </div>
        """, unsafe_allow_html=True)
        st.metric(label="Volumen del Espacio Intersticial (ISV)", value=f"{volumen_isv}%")
        st.metric(label="Eficiencia del Aclaramiento Glinfático", value=eficiencia_txt)
        
    with col2:
        # Gráfica de barras moderna simulando el comportamiento del tejido
        fig = go.Figure(go.Bar(
            x=['Espacio Intersticial (ISV)', 'Resistencia al Flujo', 'Aclaramiento de Toxinas'],
            y=[volumen_isv, 100 - volumen_isv, volumen_isv * 1.5],
            marker_color=[color_hex, '#94A3B8', '#3B82F6']
        ))
        fig.update_layout(
            title="<b>Métricas Celulares y Dinámicas del Tejido</b>",
            yaxis_range=[0, 100],
            template="plotly_white",
            height=380,
            margin=dict(t=40, b=20, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("### Panel de Control Experimental de Roedores")
    st.markdown("Simula los resultados histológicos y moleculares del estudio de *Zhao et al. (2023)* evaluando genotipos y semanas de privación.")
    
    c1, c2 = st.columns(2)
    with c1:
        grupo_raton = st.selectbox("Selecciona el Grupo Experimental:", [
            "Grupo 1: Alzheimer 5xFAD + Antena Normal (TREM2+/+)",
            "Grupo 2: Alzheimer 5xFAD + Antena Defectuosa (R47H)",
            "Grupo 3: Alzheimer 5xFAD + Sin Antena (Knockout / TREM2-/-)",
            "Grupo 4: Cerebro Sano (Wild-Type) + Antena Normal",
            "Grupos 5 & 6: Cerebro Sano + Antena Defectuosa o Ausente"
        ])
    with c2:
        semanas_privacion = st.slider("Semanas de Privación Crónica de Sueño:", 1, 6, 6)
        
    st.markdown("---")
    
    # Tarjetas de resultados estilizadas según la elección
    if "Grupo 1" in grupo_raton:
        st.markdown(f"""
            <div class="card-box" style="border-left-color: #EF4444; background-color: #FEF2F2;">
                <h3 style="color: #991B1B; margin-top: 0;">🚨 [GRUPO 1] Resultados tras {semanas_privacion} semanas</h3>
                <p><b>Carga de Beta-amiloide:</b> 🔴 Duplicada (<b>~200% de aumento</b> en placas).</p>
                <p><b>Estado Lisosomal ('Estómagos Celulares'):</b> Colapsados, hinchados y deformes severamente.</p>
                <p><b>Análisis Mecanístico:</b> El estrés energético provocado por la falta de sueño activa la señal TREM2, forzando a la microglía a un sobretrabajo que colapsa su capacidad y dispara el amiloide.</p>
            </div>
        """, unsafe_allow_html=True)
    elif "Grupo 2" in grupo_raton:
        st.markdown(f"""
            <div class="card-box" style="border-left-color: #F59E0B; background-color: #FFFBEB;">
                <h3 style="color: #92400E; margin-top: 0;">⚠️ [GRUPO 2] Resultados tras {semanas_privacion} semanas</h3>
                <p><b>Carga de Beta-amiloide:</b> 🟡 Sin picos agudos extremos inmediatos.</p>
                <p><b>Estado Lisosomal:</b> Células funcionalmente <b>'ciegas'</b> por la mutación R47H.</p>
                <p><b>Análisis Mecanístico:</b> Al tener la antena mutada, la microglía no responde al estrés agudo, pero pierde por completo su capacidad de limpieza, acumulando basura silenciosamente año tras año.</p>
            </div>
        """, unsafe_allow_html=True)
    elif "Grupo 3" in grupo_raton:
        st.markdown(f"""
            <div class="card-box" style="border-left-color: #F59E0B; background-color: #FFFBEB;">
                <h3 style="color: #92400E; margin-top: 0;">⚠️ [GRUPO 3] Resultados tras {semanas_privacion} semanas</h3>
                <p><b>Carga de Beta-amiloide:</b> 🟡 Incremento moderado y limitado en comparación con el Grupo 1.</p>
                <p><b>Estado Lisosomal:</b> Inactivas / No fagocíticas.</p>
                <p><b>Análisis Mecanístico:</b> Demuestra que la privación de sueño necesita obligatoriamente de una vía TREM2 funcional para desencadenar el daño destructivo en el modelo de Alzheimer.</p>
            </div>
        """, unsafe_allow_html=True)
    elif "Grupo 4" in grupo_raton:
        st.markdown(f"""
            <div class="card-box" style="border-left-color: #EF4444; background-color: #FEF2F2;">
                <h3 style="color: #991B1B; margin-top: 0;">⚠️ [GRUPO 4] Resultados tras {semanas_privacion} semanas</h3>
                <p><b>Carga de Beta-amiloide:</b> N/A (Cerebro sano sin sobreproducción patológica).</p>
                <p><b>Estado Lisosomal:</b> 🔴 <b>¡Daño crítico!</b> Lisosomas hinchados, deformes y pérdida total de enzimas digestivas.</p>
                <p><b>Análisis Mecanístico:</b> ¡No se necesita Alzheimer! La privación crónica de sueño por sí sola destruye y colapsa el sistema de limpieza lisosomal de un cerebro sano.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="card-box" style="border-left-color: #10B981; background-color: #ECFDF5;">
                <h3 style="color: #065F46; margin-top: 0;">✅ [GRUPOS 5 & 6] Resultados tras {semanas_privacion} semanas</h3>
                <p><b>Carga de Beta-amiloide:</b> Estables.</p>
                <p><b>Estado Lisosomal:</b> 🟢 <b>Protegidas</b> frente al colapso inducido por la falta de descanso.</p>
                <p><b>Análisis Mecanístico:</b> Confirma que la vía TREM2 es el interruptor molecular exacto que conecta la falta de descanso con el estrés inflamatorio celular.</p>
            </div>
        """, unsafe_allow_html=True)
