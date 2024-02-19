import polars as pl


def ram_list(df: pl.DataFrame) -> list:
    """Sélectionne les valeurs distinctes de la RAM et la transforme en liste."""
    return df.select(pl.col("ram")).unique().to_series().to_list()


def storage_list(df: pl.DataFrame) -> list:
    """Sélectionne les valeurs distinctes du stockage et la transforme en liste."""
    return df.select(pl.col("storage")).unique().to_series().to_list()


def brand_list(df: pl.DataFrame) -> list:
    """Sélectionne les valeurs distinctes de la marque et la transforme en liste."""
    return df.select(pl.col("brand")).unique().to_series().to_list()


def min_price(df: pl.DataFrame) -> float:
    """Sélectionne le prix minimal du dataframe."""
    return df.select(pl.col("price")).min().item()


def max_price(df: pl.DataFrame) -> float:
    """Sélectionne le prix maximal du dataframe."""
    return df.select(pl.col("price")).max().item()
