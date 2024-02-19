import streamlit as st
import polars as pl
from pathlib import Path


@st.cache_data
def load_df() -> pl.DataFrame:
    """`load_df`: Charge notre DataFrame clean statique utilisé dans
    la page de Statistiques Descriptives.

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> load_df()
    ... shape: (4_006, 40)
    """
    root = Path(".").resolve()
    data_folder = root / "Web_Scraping" / "data"
    df = pl.read_parquet(data_folder / "sfa_results_app.parquet")
    return df


@st.cache_data
def link_column(_df: pl.DataFrame) -> pl.DataFrame:
    APP_URL = "http://localhost:8501"

    return _df.with_columns()


@st.cache_data
def load_mutable_df(
    _df: pl.DataFrame, selected_ram, selected_storage, selected_brands
) -> pl.DataFrame:
    mutable_df = (
        _df.filter(pl.col("ram") == selected_ram)
        .filter(pl.col("storage") == selected_storage)
        .filter(pl.col("brand").is_in(selected_brands))
    )
    return mutable_df


def last_update(df: pl.DataFrame) -> str:
    """`last_update`: Permet de récupérer la dernière date de scraping

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
