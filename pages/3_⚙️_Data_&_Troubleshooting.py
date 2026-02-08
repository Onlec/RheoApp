import streamlit as st
import pandas as pd

# Pagina configuratie
st.set_page_config(
    page_title="Data & Troubleshooting - RheoApp",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Data Specificaties & Troubleshooting")
st.markdown("""
Zorg ervoor dat je data correct is geformatteerd om fouten in de berekeningen te voorkomen. 
Deze pagina helpt je bij het voorbereiden van je bestanden en het oplossen van veelvoorkomende problemen.
""")

# Sectie 1: Data Formaat
st.header("1. Data Format Specificaties")
st.markdown("""
De app accepteert `.csv` of `.txt` bestanden (tab- of puntkomma-gescheiden). 
De volgende kolommen zijn **verplicht** voor een volledige analyse:
""")

# Voorbeeld tabel van gewenste data
example_data = {
    "T (°C)": [170, 170, 180],
    "omega (rad/s)": [0.1, 0.25, 0.1],
    "G' (Pa)": [1250, 2100, 850],
    "G'' (Pa)": [3400, 4800, 2100],
    "eta* (Pa·s)": [36220, 21000, 22600]
}
df_example = pd.DataFrame(example_data)

st.subheader("Voorbeeld van de juiste structuur:")
st.table(df_example)

with st.expander("Gids voor kolomnamen"):
    st.markdown("""
    De app zoekt naar specifieke trefwoorden in de headers. Zorg dat je kolommen namen hebben zoals:
    * **Temperatuur**: `Temperature`, `Temp`, `T`
    * **Frequentie**: `Angular Frequency`, `omega`, `rad/s`
    * **Storage Modulus**: `Storage Modulus`, `G'`, `Gp`
    * **Loss Modulus**: `Loss Modulus`, `G''`, `Gpp`
    * **Complexe Viscositeit**: `Complex Viscosity`, `eta*`, `Eta_star`
    """)

st.divider()

# Sectie 2: Veelvoorkomende Foutmeldingen
st.header("2. Troubleshooting (Probleemoplosser)")

col_err, col_sol = st.columns(2)

with col_err:
    st.subheader("Wat gaat er mis?")
    
    st.error("**Fout: 'Negative C1 found' (WLF)**")
    st.warning("**Waarschuwing: 'R² < 0.90'**")
    st.error("**Fout: 'Fit failed' bij Zero-Shear**")
    st.info("**Probleem: Master Curve 'trapt' (sluit niet aan)**")

with col_sol:
    st.subheader("Hoe los ik het op?")
    
    st.markdown("- **C1 Check**: Je referentietemperatuur ligt waarschijnlijk te dicht bij een fase-overgang of de shift-factors zijn te extreem. Kies een andere $T_{ref}$.")
    st.markdown("- **R² Verbeteren**: Verwijder uiterste temperaturen die niet voldoen aan TTS (bijv. waar kristallisatie begint).")
    st.markdown("- **Fit Succes**: Het Cross-model heeft meer data nodig in de lage frequentie (terminale zone).")
    st.markdown("- **Trapping**: Gebruik de **Handmatige Shift** in Tab 1 om de curves handmatig op elkaar te schuiven.")

st.divider()

# Sectie 3: Tips voor TPU Rheologie
st.header("3. Tips voor TPU Metingen")
st.info("""
**Wist je dat?** TPU is zeer gevoelig voor vocht (hydrolyse). Als je metingen niet reproduceerbaar zijn, 
controleer dan of het granulaat minimaal 3 uur op 80°C gedroogd is (vacuüm aanbevolen).
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🌡️ Thermal Stability")
    st.caption("Voer altijd een 'Time Sweep' uit bij de hoogste meettemperatuur om te checken of het materiaal stabiel blijft tijdens de frequentie-sweep.")

with col2:
    st.markdown("### 💧 Hydrolyse")
    st.caption("Een snelle daling van G' over de tijd bij constante T en $\omega$ wijst meestal op vocht in het sample.")

with col3:
    st.markdown("### 🌀 Strain")
    st.caption("Zorg dat je binnen de Linear Visco-Elastic (LVE) regio meet (meestal < 5% strain voor TPU smelten).")

# Voetnoot
st.sidebar.markdown("---")
st.sidebar.caption("RheoApp Versie 1.0.0")