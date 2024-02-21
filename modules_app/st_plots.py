import plotly.express as px
import polars as pl
import streamlit as st
from PIL import Image
from streamlit.delta_generator import DeltaGenerator


def open_logo() -> Image.Image:
    """`logo`: Permet d'accéder au logo de notre application
    et de l'ouvrir pour l'insérer dans des figures `plotly`.

    `Returns`
    --------- ::

        Image

    `Example(s)`
    ---------

    >>> logo()
    ... #_test_return_"""
    return Image.open("imgs/logo.png")


def modebar_config(display: bool = False) -> dict[str, bool]:
    """`modebar_config`: Configure la barre Hover de `plotly`.
    Permet de l'afficher ou bien de la cacher. Par défaut la barre est cachée.

    ---------
    `Parameters`
    --------- ::

        display (bool, optional): # afficher ou non. Par défaut, False.

    `Returns`
    --------- ::

        dict[str, bool]

    `Example(s)`
    ---------

    >>> modebar_config()
    ... #_test_return_"""
    return {"displayModeBar": display}


def barplot_mean_price(
    df_mean_price: pl.DataFrame, logo: Image.Image, config: dict[str, bool]
) -> DeltaGenerator:
    fig_mean_price = px.bar(
        df_mean_price, x="price", y="brand", opacity=0.85, text="price_str"
    )
    fig_mean_price.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        xaxis=dict(title="", ticksuffix=" €", fixedrange=True),
        yaxis=dict(title=""),
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
    return st.plotly_chart(fig_mean_price, use_container_width=True, config=config)
