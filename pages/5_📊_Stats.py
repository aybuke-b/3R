import streamlit as st
from PIL import Image
import plotly.express as px
from modules_app.st_config import *
from modules_app.data_import import *

logo = Image.open("imgs/logo.png")

page_config()
remove_white_space()
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")

df = load_df()
df_mean_price = df.group_by("brand").agg(pl.col("price").mean().round(2)).sort("price")
df_mean_price = df_mean_price.with_columns(
    pl.format("{} €", pl.col("price")).alias("price_str")
)

with st.sidebar:
    if st.button("🏠 **Retourner à l'accueil**"):
        st.switch_page("Home.py")

st.title("📱 Smart Specs")
st.header("Data Insights 🔎", divider="gray")
st.info("Passons nos données à la loupe")


with st.expander("**Insight 1) Prix moyen par marque**"):
    # st.subheader("Prix moyen par marque", help="test")
    config = {"displayModeBar": False}
    mean_price = df.select("price").mean().item()
    fig_mean_price = px.bar(
        df_mean_price, x="price", y="brand", opacity=0.85, text="price_str"
    )
    fig_mean_price.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        xaxis=dict(title="", ticksuffix=" €", fixedrange=True),
        yaxis=dict(title=""),
        modebar_add=[
            "drawline",
            "drawrect",
            "eraseshape",
        ],
    )
    fig_mean_price.update_traces(
        hovertemplate="<b>Marque :</b> %{y}<br>" "<b>Prix Moyen :</b> %{x}<br>"
    )
    fig_mean_price.add_layout_image(
        dict(
            source=logo,
            xref="paper",
            yref="paper",
            x=0.9,  # Position horizontale de l'image (0 à gauche, 1 à droite)
            y=0,  # Position verticale de l'image (0 en bas, 1 en haut)
            sizex=0.25,  # Largeur de l'image
            sizey=0.25,  # Hauteur de l'image
            xanchor="center",  # Point d'ancrage horizontal (centre)
            yanchor="bottom",  # Point d'ancrage vertical (en bas)
        )
    )
    st.plotly_chart(fig_mean_price, use_container_width=True, config=config)

with st.expander("**Insight 2) Nombre de modèles vendus par marque**"):
    st.write("test test")

df_ram = df.sort(pl.col("ram")).with_columns(
    pl.format("{} Go", pl.col("ram").cast(pl.Int64)).alias("ram_fmt")
)

fig_ram = px.box(df_ram, x="ram_fmt", y="price", points="all")
st.plotly_chart(fig_ram, use_container_width=True)
