import streamlit as st
import time
from modules_app.st_config import *
from modules_app.data_import import *

page_config()
remove_white_space()
version = fontawesome_import(major=6, minor=5, patch=1)
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")


fontawesome_icon = icon(type="brands", icon_name="font-awesome", color="#74C0FC")
layer_icon = icon(type="solid", icon_name="layer-group")
apple_icon = icon(type="brands", icon_name="apple")
coins_icon = icon(type="solid", icon_name="coins")
list_icon = icon(type="solid", icon_name="list-check")
sparkle_icon = icon(type="solid", icon_name="wand-magic-sparkles", color="#ffd43b")
cc_by_nc_icon = icon(type="brands", icon_name="creative-commons-nc-eu", color="#74C0FC")
external_link_icon = icon(
    type="solid", icon_name="arrow-up-right-from-square", color="#0068c9", size="2xs"
)


df = load_df()

st.title("📱 Smart Specs")
st.header("Un :blue[comparateur], :grey[*amélioré*.]", divider="gray")

with st.sidebar:
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
    with col1:
        st.write("")
    with col2:
        st.image("imgs/logo.png", use_column_width="auto")
    with col2:
        st.write("")
    st.caption("Crée par :")
    with st.container(border=True):
        st.markdown(
            """
            💻 [**Corentin DUCLOUX**](https://github.com/CDucloux) \n
            💻 [**Aybuké BICAT**](https://github.com/CDucloux)
            """
        )

catchphrase = """
    💡 Obtenez **bien plus** qu'une *simple liste* de téléphones !  
    """


def home_stream():
    for word in catchphrase.split():
        yield word + " "
        time.sleep(0.2)


st.write_stream(home_stream)


st.markdown(
    f"""
    - {apple_icon} Choisissez une ou plusieurs marques...
    - {coins_icon} un budget maximum...
    - {list_icon} quelques caractéristiques...
    - {sparkle_icon} laissez-vous guider pour trouver **LE** smartphone de vos rêves !

    **Smart Specs®** utilise un modèle **SFA** pour déterminer l'*efficacité* d'un prix (c'est à dire le rapport *qualité-prix* du téléphone)
    """,
    unsafe_allow_html=True,
)

with st.expander("En savoir plus sur le modèle **SFA**"):
    st.markdown(
        f"""
        La **SFA** ([Stochastic Frontier Analysis {external_link_icon}](https://en.wikipedia.org/wiki/Stochastic_frontier_analysis)),
        est une méthode économétrique permettant d'introduire la notion d'*inefficacité*
        dans le cadre d'un modèle de régression. 

        Initialement, le concept de frontière stochastique repose sur l'idée 
        qu'il existe une frontière théorique, appelée frontière de production,
        qui représente la production maximale qu'une entreprise peut atteindre
        avec les ressources et la technologie à sa disposition.
        Cependant, en raison de divers facteurs, 
        certaines entreprises ne sont pas en mesure d'atteindre cette frontière : elles sont dites inefficaces.

        Si la **SFA** est couramment utilisée dans l'analyse de la production,
        le concept peut aussi être étendu à l'analyse des coûts. 

        $\Rightarrow$ **Dans notre cadre, cela permet de déterminer l'efficacité individuelle par modèle de téléphone.**
        """,
        unsafe_allow_html=True,
    )

col1, col2 = st.columns(2)
with col2:
    st.caption(f"*Dernière date d'actualisation* : {last_update(df)}")

st.write(
    f"""
    > *Icônes* : {fontawesome_icon} **FontAwesome** version **{version[0]}**
    &mdash; *Licence* : {cc_by_nc_icon} **CC-BY-NC**
    """,
    unsafe_allow_html=True,
)

