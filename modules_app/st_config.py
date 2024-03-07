"""
# `st_config`

Le module de configuration de l'app avec : 

- Configuration du Favicon
- Imports de fonts
- Import de FontAwesome
- CSS personnalisé
"""

import streamlit as st
import polars as pl
from streamlit.delta_generator import DeltaGenerator


def page_config() -> None:
    """`page_config`: Configure le titre et le favicon de l'application.

    `Example(s)`
    ---------
    >>> page_config()
    ... None"""
    return st.set_page_config(page_title="Smart Specs", page_icon="📱")


def background_style() -> DeltaGenerator:
    return st.markdown(
        """
        <style>
                .stApp > header {
                    background-color: transparent;
                }
                .stApp {
                    margin: auto;
                    overflow: auto;
                    background: linear-gradient(315deg, white 3%, white 38%, white 68%, #00d5c6 90%);
                    animation: gradient 15s ease infinite;
                    background-size: 400% 400%;
                    background-attachment: fixed;
                }
        </style>
        """,
        unsafe_allow_html=True,
    )


def remove_white_space() -> DeltaGenerator:
    """`remove_white_space`: Utilise du CSS pour retirer de l'espace non-utilisé.

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------
    >>> remove_white_space()
    ... DeltaGenerator()"""
    return st.markdown(
        """
        <style>
                .st-emotion-cache-1y4p8pa {
                    padding-top: 0rem;
                    padding-bottom: 1rem;
                    padding-left: 1.25rem;
                    padding-right: 1.25rem;
                }
                .st-emotion-cache-16txtl3 {
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                }
        </style>
        """,
        unsafe_allow_html=True,
    )


def underline_decoration() -> DeltaGenerator:
    """`underline_decoration`: Utilise du CSS pour retirer la barre de soulignement d'un lien `<a href ="">`

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------
    >>> remove_white_space()
    ... DeltaGenerator()"""
    return st.markdown(
        """
        <style>
                a {
                    text-decoration: none;
                }
        </style>
        """,
        unsafe_allow_html=True,
    )


def fontawesome_version(major: int, minor: int, patch: int) -> str:
    """`fontawesome_version`: Permet de sélectionner la version de FontAwesome à utiliser

    ---------
    `Parameters`
    --------- ::

        major (int): # La version majeure (6)
        minor (int): # La version mineure (5)
        patch (int): # Le patch (0)

    `Returns`
    --------- ::

        str # La version complète

    `Example(s)`
    ---------

    >>> fontawesome_version()
    ... #_test_return_"""
    return f"{major}.{minor}.{patch}"


def fontawesome_import(major: int, minor: int, patch: int) -> tuple[str, None]:
    """`fontawesome_import`: Permet d'importer la feuille de style des icônes FontAwesome.

    ---------
    `Parameters`
    --------- ::

        major (int): # La version majeure (6)
        minor (int): # La version mineure (5)
        patch (int): # Le patch (0)

    `Returns`
    --------- ::

        _type_

    `Example(s)`
    ---------

    >>> fontawesome_import()
    ... #_test_return_"""
    version = fontawesome_version(major=major, minor=minor, patch=patch)
    return version, st.write(
        f"""
        <link rel="stylesheet" 
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/{version}/css/all.min.css"/>
        """,
        unsafe_allow_html=True,
    )


def font_import(font: str) -> None:
    return st.write(
        f"""
        <link href="https://fonts.googleapis.com/css2?family={font}&family=Bungee+Shade&display=swap" 
        rel="stylesheet">
        """,
        unsafe_allow_html=True,
    )


def font_apply(font: str, tag: str) -> None:
    return st.write(
        f"""
        <style>
        {tag} {{
            font-family: {font};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def icon(
    type: str, icon_name: str, color: str = "black", size: str | None = None
) -> str:
    """`icon`: Génère un icône FontAwesome.

    ---------
    `Parameters`
    --------- ::

        type (str): # Le type de l'icône : brands/solid, etc.
        icon_name (str): # Le nom de l'icône : facebook, database, etc.

    `Returns`
    --------- ::

        str

    `Example(s)`
    ---------

    >>> icon()
    ... #_test_return_"""
    if size == None:
        icon = f'<i class="fa-{type} fa-{icon_name}" style="color: {color};"></i>'
    else:
        icon = f'<i class="fa-{type} fa-{icon_name} fa-{size}" style="color: {color};"></i>'
    return icon


def last_update(df: pl.DataFrame) -> str:
    """`last_update`: Permet de récupérer la dernière date de scraping.

    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): # Le DataFrame statique

    `Returns`
    --------- ::

        str

    `Example(s)`
    ---------

    >>> last_update()
    ... #_test_return_"""
    last_updated = df.select(pl.col("scraping_time")).item(1, 0)
    day, month, year = last_updated.day, last_updated.month, last_updated.year
    if last_updated.day < 10:
        day = f"0{last_updated.day}"
    if last_updated.month < 10:
        month = f"0{last_updated.month}"
    return f"`{day}/{month}/{year}`"
