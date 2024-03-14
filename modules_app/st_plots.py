"""
# `st_plots`

Le module des plots de l'app.
"""

import plotly.express as px
import polars as pl
import streamlit as st
from PIL import Image
from streamlit.delta_generator import DeltaGenerator


def open_logo() -> Image.Image:
    """`open_logo`: Permet d'accéder au logo de notre application
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
    """`barplot_mean_price`: (PAGE 2) Charge le barplot plotly des prix moyens en fonction de la marque.

    ---------
    `Parameters`
    --------- ::

        df_mean_price (pl.DataFrame): #_description_
        logo (Image.Image): #_description_
        config (dict[str, bool]): #_description_

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------

    >>> barplot_mean_price()
    ... #_test_return_"""
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


def boxplot_ram(
    df_ram: pl.DataFrame, logo: Image.Image, config: dict[str, bool]
) -> DeltaGenerator:
    """`boxplot_ram`: (PAGE 2) Charge le boxplot plotly des prix en fonction de la RAM.

    ---------
    `Parameters`
    --------- ::

        df_ram (pl.DataFrame): #_description_
        logo (Image.Image): #_description_
        config (dict[str, bool]): #_description_

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------

    >>> boxplot_ram()
    ... #_test_return_"""
    fig_ram = px.box(df_ram, x="ram_fmt", y="price", points="all")
    fig_ram.update_traces(
        boxpoints="all",
        hovertemplate="<b>Prix :</b> %{y}<br>" "<b>RAM :</b> %{x}<br>",
    )
    fig_ram.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        yaxis=dict(title="", ticksuffix=" €"),
        xaxis=dict(title=""),
    )
    fig_ram.add_layout_image(
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
    return st.plotly_chart(fig_ram, use_container_width=True, config=config)


def boxplot_storage(
    df_storage: pl.DataFrame, logo: Image.Image, config: dict[str, bool]
) -> DeltaGenerator:
    """`boxplot_storage`: (PAGE 2) Charge le boxplot plotly des prix en fonction de la capacité de stockage.

    ---------
    `Parameters`
    --------- ::

        df_storage (pl.DataFrame): #_description_
        logo (Image.Image): #_description_
        config (dict[str, bool]): #_description_

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------

    >>> boxplot_storage()
    ... #_test_return_"""
    fig_storage = px.box(df_storage, x="stockage_fmt", y="price", points="all")
    fig_storage.update_traces(
        boxpoints="all",
        hovertemplate="<b>Prix :</b> %{y}<br>" "<b>Stockage :</b> %{x}<br>",
    )
    fig_storage.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        yaxis=dict(title="", ticksuffix=" €"),
        xaxis=dict(title=""),
    )
    fig_storage.add_layout_image(
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
    return st.plotly_chart(fig_storage, use_container_width=True, config=config)


def hist_price(
    df: pl.DataFrame,
    color_config: str | bool,
    marginal_config: str | bool,
    logo: Image.Image,
    config: dict[str, bool],
) -> DeltaGenerator:
    """`hist_price`: (PAGE 2) Charge l'histogramme plotly de la distribution des prix.

    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): #_description_
        color_config (str | bool): #_description_
        marginal_config (str | bool): #_description_
        logo (Image.Image): #_description_
        config (dict[str, bool]): #_description_

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------

    >>> hist_price()
    ... #_test_return_"""
    fig_hist = px.histogram(
        df,
        x="price",
        hover_data="model",
        color=color_config,
        marginal=marginal_config,
        opacity=0.85,
    )
    fig_hist.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        yaxis=dict(title=""),
        xaxis=dict(title="", ticksuffix=" €"),
        legend=dict(title="🏷️ Marque"),
    )
    fig_hist.add_layout_image(
        dict(
            source=logo,
            xref="paper",
            yref="paper",
            x=0.9,  # Position horizontale de l'image (0 à gauche, 1 à droite)
            y=0.55,  # Position verticale de l'image (0 en bas, 1 en haut)
            sizex=0.25,  # Largeur de l'image
            sizey=0.25,  # Hauteur de l'image
            xanchor="center",  # Point d'ancrage horizontal (centre)
            yanchor="bottom",  # Point d'ancrage vertical (en bas)
        )
    )
    fig_hist.update_traces(
        hovertemplate="<b>Nombre :</b> %{y} téléphones<br>"
        "<b>Intervalle de prix :</b> %{x}<br>",
        selector="histogram",  # on update les traces uniquement de l'histogramme
    )
    fig_hist.update_traces(
        hovertemplate="<b>Prix :</b> %{x} €<br> "
        "<b>Modèle :</b> <i>%{customdata}</i><br>",
        selector="box",  # on update les traces uniquement du "rug"
    )
    return st.plotly_chart(fig_hist, use_container_width=True, config=config)
