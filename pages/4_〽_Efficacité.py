import streamlit as st
import plotly.express as px
from modules_app.data_import import *
from modules_app.selectors import *
from modules_app.st_config import *

page_config()
remove_white_space()
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")

st.title("📱 Smart Specs")

df = load_df()


@st.cache_data
def load_mutable_df(_df: pl.DataFrame, selected_brands, price_max) -> pl.DataFrame:
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

mutable_df = load_mutable_df(df, selected_brands, price_max)

st.header("Efficacité globale des téléphones", divider="gray")

if len(mutable_df) < 1:
    st.warning("Aucun téléphone n'a été trouvé avec ces filtres")
else:

    fig_efficiency = px.scatter(
        mutable_df,
        x="price",
        y="efficiency",
        color="brand",
        custom_data=["brand", "model"],
    )

    fig_efficiency.update_layout(
        hovermode="x unified",
        xaxis=dict(
            title="",
            ticksuffix=" €",
        ),
        yaxis=dict(title=""),
    )

    fig_efficiency.add_shape(
        type="line",
        x0=mutable_df.select(pl.col("price")).min().item() - 120,
        x1=mutable_df.select(pl.col("price")).max().item() + 125,
        y0=efficiency_cutoff,
        y1=efficiency_cutoff,
        line=dict(
            color="red",
            width=2,
            dash="dash",
        ),
    )

    min_eff_selection = mutable_df.select(pl.col("efficiency")).min().item()

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

    fig_efficiency.add_layout_image(
        dict(
            # source="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
            xref="paper",
            yref="paper",
            x=0.5,  # Position horizontale de l'image (0 à gauche, 1 à droite)
            y=1.05,  # Position verticale de l'image (0 en bas, 1 en haut)
            sizex=0.5,  # Largeur de l'image
            sizey=0.5,  # Hauteur de l'image
            xanchor="center",  # Point d'ancrage horizontal (centre)
            yanchor="bottom",  # Point d'ancrage vertical (en bas)
        )
    )

    st.plotly_chart(fig_efficiency, use_container_width=True)

st.info(
    """
    ℹ **Note** : Dans le graphique ci-dessous, les téléphones compris dans la zone en surbrillance sont considérés
    comme étant trop chers par rapport à leurs caractéristiques.
    """
)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.metric(
            "Téléphones efficaces",
            mutable_df.filter(pl.col("efficiency") >= efficiency_cutoff)
            .select(pl.col("model").count())
            .item(),
        )

with col2:
    with st.container(border=True):
        st.metric(
            "Téléphones inefficients",
            mutable_df.filter(pl.col("efficiency") < efficiency_cutoff)
            .select(pl.col("model").count())
            .item(),
        )
