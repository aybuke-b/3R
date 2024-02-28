"""
# `data_import`

Le module d'import des donnéees de l'app.
"""

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
def load_efficiency_df(
    _df: pl.DataFrame, selected_brands: list, price_max
) -> pl.DataFrame:
    """`load_efficiency_df`: (PAGE 4) DataFrame mutable de l'efficacité SFA.

    ---------
    `Parameters`
    --------- ::

        _df (pl.DataFrame): #_description_
        selected_brands (list): #_description_
        price_max (_type_): #_description_

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> load_efficiency_df()
    ... #_test_return_"""
    efficiency_df = _df.filter(pl.col("brand").is_in(selected_brands)).filter(
        pl.col("price") < price_max
    )
    return efficiency_df


@st.cache_data
def load_brands_df(_df: pl.DataFrame) -> pl.DataFrame:
    """`load_brands_df`: (PAGE 2) DataFrame du count et pourcentage de téléphones par marque.

    ---------
    `Parameters`
    --------- ::

        _df (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> load_brands_df()
    ... #_test_return_"""
    df_brands = (
        _df.group_by(pl.col("brand"))
        .agg(pl.col("brand").count().alias("count"), pl.col("price").alias("hist_col"))
        .sort("count", descending=True)
        .with_columns(
            (pl.col("count") / pl.sum("count")).alias("percent_count").mul(100)
        )
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
    """`load_mean_price_df`: (PAGE 2) DataFrame statique des prix moyens par marque.

    ---------
    `Parameters`
    --------- ::

        _df (pl.DataFrame): # Le DataFrame statique initial

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


@st.cache_data
def load_ram_df(_df: pl.DataFrame) -> pl.DataFrame:
    """`load_ram_df`: (PAGE 2) DataFrame formattant la RAM.

    ---------
    `Parameters`
    --------- ::

        _df (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> load_ram_df()
    ... #_test_return_"""
    df_ram = _df.sort(pl.col("ram")).with_columns(
        pl.format("{} Go", pl.col("ram").cast(pl.Int64)).alias("ram_fmt")
    )
    return df_ram


@st.cache_data
def load_storage_df(_df: pl.DataFrame) -> pl.DataFrame:
    """`load_storage_df`: (PAGE 2) DataFrame formattant le stockage.

    ---------
    `Parameters`
    --------- ::

        _df (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> load_storage_df()
    ... #_test_return_"""
    df_storage = _df.sort(pl.col("storage")).with_columns(
        pl.format("{} Go", pl.col("storage").cast(pl.Int64)).alias("stockage_fmt")
    )
    return df_storage


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
