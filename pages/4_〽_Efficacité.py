import streamlit as st
import plotly.express as px
from modules_app.data_import import *
from modules_app.selectors import *
from modules_app.st_config import *
from modules_app.st_plots import *

page_config()
remove_white_space()
fontawesome_icon = icon(type="brands", icon_name="font-awesome", color="#74C0FC")
cc_by_nc_icon = icon(type="brands", icon_name="creative-commons-nc-eu", color="#74C0FC")
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")
version = fontawesome_import(major=6, minor=5, patch=1)


st.title("📱 Smart Specs")

logo = open_logo()
config = modebar_config()

df = load_df()


@st.cache_data
def load_efficiency_df(_df: pl.DataFrame, selected_brands, price_max) -> pl.DataFrame:
    mutable_df = _df.filter(pl.col("brand").is_in(selected_brands)).filter(
        pl.col("price") < price_max
    )
    return mutable_df


with st.sidebar:
    selected_brands = st.multiselect(
        "Choisir une ou plusieurs marques :",
        sorted(brand_list(df)),
        default=["APPLE", "SAMSUNG"],
        placeholder="Choisir la marque",
    )

    price_max = st.slider(
        "Sélectionner un prix maximal",
        min_value=min_price(df),
        max_value=max_price(df),
        value=500.00,
    )

    on = st.toggle("🎯 Affiner le seuil d'efficacité")

    if not on:
        efficiency_cutoff = 0.8

    if on:
        efficiency_cutoff = st.number_input(
            "Choisir le seuil d'efficacité",
            min_value=0.00,
            max_value=1.00,
            value=0.8,
            placeholder="Entrer entre un nombre décimal entre 0 et 1",
        )

efficiency_df = load_efficiency_df(df, selected_brands, price_max)

st.header("Efficacité globale des téléphones", divider="gray")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.metric(
            ":grey[Nombre de téléphones *efficaces*]",
            f"""
            🔺 {efficiency_df.filter(pl.col("efficiency") >= efficiency_cutoff)
            .select(pl.col("model").count()).item()}
            """,
            help=f"Les téléphones au-dessus du seuil d'efficacité spécifié **({round(efficiency_cutoff,2)})**",
        )

with col2:
    with st.container(border=True):
        st.metric(
            ":grey[Nombre de téléphones *inefficaces*]",
            f"""
            🔻 {efficiency_df.filter(pl.col("efficiency") < efficiency_cutoff)
            .select(pl.col("model").count()).item()}
            """,
            help=f"Les téléphones sous le seuil d'efficacité spécifié **({round(efficiency_cutoff,2)})**",
        )


if len(efficiency_df) < 1:
    st.warning("Aucun téléphone n'a été trouvé avec ces filtres")
else:

    fig_efficiency = px.scatter(
        efficiency_df,
        x="price",
        y="efficiency",
        color="brand",
        custom_data=["brand", "model"],
    )

    fig_efficiency.add_shape(
        type="line",
        x0=efficiency_df.select(pl.col("price")).min().item() - 120,
        x1=efficiency_df.select(pl.col("price")).max().item() + 125,
        y0=efficiency_cutoff,
        y1=efficiency_cutoff,
        line=dict(
            color="red",
            width=2,
            dash="dash",
        ),
    )

    min_eff_selection = efficiency_df.select(pl.col("efficiency")).min().item()

    if min_eff_selection < efficiency_cutoff:
        fig_efficiency.add_hrect(
            y0=min_eff_selection,
            y1=efficiency_cutoff,
            line_width=0,
            fillcolor="red",
            opacity=0.1,
        )
    else:
        pass

    fig_efficiency.update_traces(
        hovertemplate="<b>Marque :</b> %{customdata[0]}<br>"
        "<b>Modèle :</b> %{customdata[1]}<br>"
        "<b>Prix :</b> %{x}<br>"
        "<b>Efficacité :</b> %{y:.2f}<extra></extra>"
    )
    fig_efficiency.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        yaxis=dict(title=""),
        xaxis=dict(
            title="",
            ticksuffix=" €",
        ),
        hovermode="x unified",
        hoverlabel=dict(bgcolor="rgba(255,255,255,0.95)"),
        legend=dict(title="🏷️ Marque"),
    )

    fig_efficiency.add_layout_image(
        dict(
            source=logo,
            xref="paper",
            yref="paper",
            x=0.95,  # Position horizontale de l'image (0 à gauche, 1 à droite)
            y=0,  # Position verticale de l'image (0 en bas, 1 en haut)
            sizex=0.25,  # Largeur de l'image
            sizey=0.25,  # Hauteur de l'image
            xanchor="center",  # Point d'ancrage horizontal (centre)
            yanchor="bottom",  # Point d'ancrage vertical (en bas)
        )
    )

    st.plotly_chart(fig_efficiency, use_container_width=True, config=config)
    

st.info(
    """
    ℹ **Note** : Dans le graphique ci-dessous, les téléphones compris dans la zone en surbrillance sont considérés
    comme étant trop chers par rapport à leurs caractéristiques.
    """
)


st.write(
    f"""
    > *Icônes* : {fontawesome_icon} **FontAwesome** version **{version[0]}**
    &mdash; *Licence* : {cc_by_nc_icon} **CC-BY-NC**
    """,
    unsafe_allow_html=True,
)
