import streamlit as st

# Pagina configuratie
st.set_page_config(
    page_title="Theorie & Modellen - RheoApp",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Theoretische Achtergrond & Modellen")
st.markdown("""
Deze pagina bevat de wetenschappelijke basis van de RheoApp. Hier vind je de achterliggende formules 
en de interpretatie van de thermische en visco-elastische modellen.
""")

# We splitsen de README secties op in logische tabs
tab_tts, tab_therm, tab_struc = st.tabs([
    "🕒 Time-Temperature Superposition", 
    "🔥 Thermische Modellen (Arrhenius/WLF/VFT)", 
    "🏗️ Structurele Parameters"
])

with tab_tts:
    st.header("Time-Temperature Superposition (TTS)")
    st.markdown("""
    Het fundamentele principe achter TTS is dat de rheologische respons van een polymeer bij verschillende temperaturen **equivalent** is, 
    mits gecorrigeerd voor een verschuivingsfactor $a_T$.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Fysische basis")
        st.info("""
        * **Hoge T**: Ketens bewegen sneller → equivalent aan lage frequentie.
        * **Lage T**: Ketens bewegen trager → equivalent aan hoge frequentie.
        """)
        st.markdown("**Verschoven Frequentie:**")
        st.latex(r"\omega_{shifted} = \omega \cdot a_T")
    
    with col2:
        st.subheader("Voorwaarde voor geldigheid")
        st.warning("""
        Het materiaal moet **thermorheologisch simpel** zijn (homogene smelt). 
        Voor TPU betekent dit dat de harde segmenten volledig gesmolten moeten zijn.
        """)

with tab_therm:
    st.header("Thermische Modellen")
    
    # Arrhenius
    st.subheader("1. Arrhenius Vergelijking")
    st.markdown("Gebruikt voor homogene smelten ver boven de overgangstemperatuur.")
    st.latex(r"\log_{10}(a_T) = \frac{-E_a}{2.303 \cdot R} \cdot \left(\frac{1}{T} - \frac{1}{T_{ref}}\right)")
    st.markdown("""
    * **$E_a$ < 50 kJ/mol**: Lage temperatuurgevoeligheid.
    * **$E_a$ 50-150 kJ/mol**: Typisch voor polymeersmelten.
    * **$E_a$ > 150 kJ/mol**: Zeer sterke gevoeligheid (kritisch procesvenster).
    """)

    st.divider()

    # WLF
    st.subheader("2. WLF (Williams-Landel-Ferry)")
    st.markdown("Beschrijft het vrije-volume effect nabij de glasovergang ($T_g$).")
    st.latex(r"\log_{10}(a_T) = \frac{-C_1(T - T_{ref})}{C_2 + (T - T_{ref})}")
    st.markdown("""
    * **$C_1$**: Vrije volume parameter (typisch 8-17).
    * **$C_2$**: Temperatuurconstante; vaak gerelateerd aan de afstand tot $T_g$.
    * **$T_g \approx T_{ref} - C_2$** (vuistregel).
    """)

    st.divider()

    # VFT
    st.subheader("3. VFT (Vogel-Fulcher-Tammann)")
    st.latex(r"\log_{10}(a_T) = A + \frac{B}{T - T_0}")
    st.markdown("""
    * **$T_0$ (Vogel-temperatuur)**: De theoretische temperatuur waarbij alle moleculaire beweging stopt.
    * Voor TPU ligt $T_0$ vaak tussen de -100°C en -50°C.
    """)

with tab_struc:
    st.header("Structurele Parameters")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Plateau Modulus ($G_N^0$)")
        st.markdown("""
        Maat voor de netwerkdichtheid en entanglements (verstrikkingen).
        """)
        st.latex(r"G_N^0 \propto \frac{\rho R T}{M_e}")
        st.info("**Interpretatie**: Een daling in $G_N^0$ wijst vaak op een lagere entanglement-dichtheid.")

    with col_b:
        st.subheader("Zero-Shear Viscosity ($\eta_0$)")
        st.markdown("""
        De viscositeit bij een afschuifsnelheid van nul. Dit is de meest gevoelige indicator voor molecuulgewicht.
        """)
        st.latex(r"\eta_0 \propto M_w^{3.4}")
        st.success("**Hydrolyse detectie**: Een plotselinge daling in $\eta_0$ tussen batches wijst op degradatie van de ketenlengte.")

    st.divider()
    
    st.subheader("Terminal Slope")
    st.markdown("""
    In de terminale zone (lage frequentie) moet een lineair polymeer vloeien als een vloeistof.
    * **Ideale helling $G'$**: 2.0
    * **Helling < 1.7**: Wijst op incomplete smelt, vloeiproblemen of beginnende crosslinking.
    """)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip**: Gebruik deze pagina om de metrics in het Dashboard te valideren.")