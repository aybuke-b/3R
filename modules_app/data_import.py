import streamlit as st
import polars as pl
from pathlib import Path


@st.cache_data
def load_df() -> pl.DataFrame:
    """`load_df`: Charge le DataFrame principal.

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


# @st.cache_data
# def link_column(_df: pl.DataFrame) -> pl.DataFrame:
#    APP_URL = "http://localhost:8501"
#
#    return _df.with_columns()


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


@st.cache_data
def load_brands_df(_df: pl.DataFrame) -> pl.DataFrame:
    df_brands = (
        _df.group_by(pl.col("brand"))
        .agg(pl.col("brand").count().alias("count"), pl.col("price").alias("hist_col"))
        .sort("count", descending=True)
        .with_columns(
            pl.when(pl.col("brand") == "XIAOMI")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/a/ae/Xiaomi_logo_%282021-%29.svg"
                )
            )
            .when(pl.col("brand") == "SAMSUNG")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/b/b4/Samsung_wordmark.svg"
                )
            )
            .when(pl.col("brand") == "APPLE")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"
                )
            )
            .when(pl.col("brand") == "MOTOROLA")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/4/45/Motorola-logo-black-and-white.png"
                )
            )
            .when(pl.col("brand") == "GOOGLE")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"
                )
            )
            .when(pl.col("brand") == "HONOR")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/5/5a/Huawei_Honor_Logo.svg"
                )
            )
            .when(pl.col("brand") == "SONY")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/c/ca/Sony_logo.svg"
                )
            )
            .when(pl.col("brand") == "OPPO")
            .then(
                pl.lit(
                    "https://upload.wikimedia.org/wikipedia/commons/0/0a/OPPO_LOGO_2019.svg"
                )
            )
            .otherwise(pl.lit(""))
            .alias("brand_image")
        )
    )
    return df_brands


@st.cache_data
def load_mean_price_df(_df: pl.DataFrame) -> pl.DataFrame:
    """`load_mean_price_df`: DataFrame statique des prix moyens par marque.

    ---------
    `Parameters`
    --------- ::

        _df (pl.DataFrame): # Le DataFrame sratique initial

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> load_mean_price_df()
    ... #_test_return_"""
    df_mean_price = (
        _df.group_by("brand").agg(pl.col("price").mean().round(2)).sort("price")
    )
    return df_mean_price.with_columns(
        pl.format("{} €", pl.col("price")).alias("price_str")
    )


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


def item_getter(
    df_mean_price: pl.DataFrame, column: str, min: bool = True
) -> str | float:
    if min:
        item = (
            df_mean_price.filter(pl.col("price") == pl.col("price").min())
            .select(column)
            .item()
        )
    if not min:
        item = (
            df_mean_price.filter(pl.col("price") == pl.col("price").max())
            .select(column)
            .item()
        )
    return item
