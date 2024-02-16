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
    df = pl.read_csv(data_folder / "sfa_results.csv")
    return df


## Cette fonction sera à inclure dans le pipeline plutot


@st.cache_data
def better_countries(_df: pl.DataFrame) -> pl.DataFrame:
    return _df.with_columns(
        pl.when(pl.col("made_in") == "Chine")
        .then(pl.lit("🇨🇳"))
        .when(pl.col("made_in") == "Japon")
        .then(pl.lit("🇯🇵"))
        .when(pl.col("made_in") == "Viêt Nam")
        .then(pl.lit("🇻🇳"))
        .when(pl.col("made_in") == "Inde")
        .then(pl.lit("🇮🇳"))
        .when(pl.col("made_in") == "Taïwan")
        .then(pl.lit("🇹🇼"))
        .when(pl.col("made_in") == "Thaïlande")
        .then(pl.lit("🇹🇭"))
        .otherwise(pl.lit(""))
        .alias("flag")
    ).with_columns(pl.concat_str(["flag", "made_in"], separator=" ").alias("made_in"))


@st.cache_data
def link_column(_df: pl.DataFrame) -> pl.DataFrame:
    APP_URL = "http://localhost:8501"

    return _df.with_columns(

    )

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


def ram_list(df: pl.DataFrame) -> list:
    return df.select(pl.col("ram")).unique().to_series().to_list()

def storage_list(df: pl.DataFrame) -> list:
    return df.select(pl.col("storage")).unique().to_series().to_list()

def brand_list(df: pl.DataFrame) -> list:
    return df.select(pl.col("brand")).unique().to_series().to_list()
