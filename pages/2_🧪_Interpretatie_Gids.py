import streamlit as st

# Pagina configuratie
st.set_page_config(
    page_title="Interpretatie Gids - RheoApp",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Interpretatie & Validatie Gids")
st.markdown("""
Hoe lees je de grafieken in het dashboard? Gebruik deze gids om te bepalen of je meting betrouwbaar is 
en wat de curves vertellen over de structuur van je TPU.
""")

# Sectie 1: Van Gurp-Palmen (De 'Gouden Standaard' voor TTS)
st.header("1. Van Gurp-Palmen (vGP) Plot")
st.markdown("""
De vGP plot zet de fasehoek ($\delta$) uit tegen de complexe modulus ($|G^*|$). 
Omdat deze plot onafhankelijk is van de frequentie-as, is het de ultieme test voor **thermorheologische eenvoud**.
""")



v_col1, v_col2 = st.columns(2)

with v_col1:
    st.subheader("Wat je wilt zien ✅")
    st.success("""
    **Superpositie**: Alle curves van verschillende temperaturen vallen perfect op één lijn.
    * **Betekenis**: Het materiaal is een homogene smelt.
    * **Conclusie**: Je Master Curve en WLF/Arrhenius fits zijn 100% betrouwbaar.
    """)

with v_col2:
    st.subheader("Red Flags 🚩")
    st.error("""
    **Spreiding/Trappen**: De curves liggen uit elkaar of vertonen 'haken'.
    * **Betekenis**: Fase-heterogeniteit. De harde segmenten zijn nog niet volledig gesmolten of kristalliseren uit.
    * **Conclusie**: TTS is wiskundig geforceerd; de fysieke parameters (zoals $E_a$) zijn minder nauwkeurig.
    """)

st.divider()

# Sectie 2: Han Plot (Detectie van chemische veranderingen)
st.header("2. Han Plot ($\log G'$ vs $\log G''$)")
st.markdown("""
De Han plot wordt gebruikt om te controleren of de structuur van het polymeer verandert *tijdens* de meting, 
bijvoorbeeld door degradatie of na-reactie (crosslinking).
""")

h_col1, h_col2 = st.columns(2)

with h_col1:
    st.info("""
    **Verticale Verschuiving (Omhoog)**:
    Als de curves bij hogere temperaturen *boven* de lagere temperaturen liggen, wijst dit op **thermal crosslinking**.
    In TPU reageren vrije NCO-groepen vaak na bij hoge T, waardoor het netwerk stijver wordt.
    """)

with h_col2:
    st.info("""
    **Verticale Verschuiving (Omlaag)**:
    Dit wijst op **thermische degradatie** of hydrolyse. De ketens breken af, waardoor de elasticiteit ($G'$) 
    sneller daalt dan de viscositeit ($G''$).
    """)

st.divider()

# Sectie 3: Cole-Cole Plot (Moleculaire spreiding)
st.header("3. Cole-Cole Plot ($\eta''$ vs $\eta'$)")
st.markdown("""
Deze plot (vaak een boogvorm) geeft inzicht in de **Molecuulgewichtsverdeling (MWD)**.
""")



c_col1, c_col2 = st.columns(2)

with c_col1:
    st.subheader("Vorm van de boog")
    st.markdown("""
    * **Perfecte halve cirkel**: Zeer smalle MWD (monodispers).
    * **Afgeplatte boog**: Brede MWD. Dit is **normaal** voor commerciële TPU.
    * **Asymmetrische boog**: Bi-modale verdeling (twee populaties ketens).
    """)

with c_col2:
    st.subheader("Proces Relevantie")
    st.warning("""
    Een bredere boog betekent vaak een **stabieler verwerkingsvenster** (betere melt strength), 
    terwijl een smalle boog kan leiden tot plotselinge viscositeitsdalingen bij kleine T-veranderingen.
    """)

st.divider()

# Sectie 4: Crossover Punten
st.header("4. Crossover Analyse ($G' = G''$)")
st.markdown("""
Het punt waar de curves elkaar kruisen is een maat voor de karakteristieke relaxatietijd ($\tau = 1/\omega_{co}$).
""")

st.markdown("""
| Aantal Crossovers | Interpretatie |
| :--- | :--- |
| **1 Crossover** | Klassiek polymeer gedrag. Volledige ontspanning bij lage frequentie. |
| **0 Crossovers** | Materiaal is ofwel puur visceus (zeer laag Mw) of gedraagt zich als een gel/crosslinked netwerk. |
| **2 of meer** | **Let op!** Dit wijst vaak op een complexe morfologie of meetfouten bij extreme frequenties. |
""")

st.sidebar.markdown("---")
st.sidebar.write("📖 **Handleiding**")
st.sidebar.caption("Gebruik de Van Gurp-Palmen plot altijd als eerste check voor je de rest van de data analyseert.")