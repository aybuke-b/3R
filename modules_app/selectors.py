import polars as pl


def ordered_brand_list(df: pl.DataFrame) -> list:
    """
    Sélectionne les valeurs distinctes de la marque,
    la transforme en liste
    et la trie par ordre alphabétique.
    """
    return sorted(df.select(pl.col("brand")).unique().to_series().to_list())


def ordered_storage_list(df: pl.DataFrame, selected_brands: list) -> list:
    """
    Sélectionne les valeurs distinctes du stockage,
    les formatte pour l'UI,
    les transforme en liste triée par stockage ascendant,
    et les filtre en fonction des marques sélectionnées.
    """
    return (
        df.filter(pl.col("brand").is_in(selected_brands))
        .select(pl.col("storage"))
        .unique()
        .cast(pl.Int64)
        .sort("storage")
        .to_series()
        + " Go"
    ).to_list()


def ordered_ram_list(
    df: pl.DataFrame, selected_brands: list, storage_value: list
) -> list:
    """
    Sélectionne les valeurs distinctes de la RAM,
    les formatte pour l'UI,
    les transforme en liste triée par RAM ascendante,
    et les filtre en fonction des marques sélectionnées
    et de la liste des stockages.
    """
    return (
        df.filter(pl.col("brand").is_in(selected_brands))
        .filter(pl.col("storage").is_in(storage_value))
        .select(pl.col("ram"))
        .unique()
        .cast(pl.Int64)
        .sort("ram")
        .to_series()
        + " Go"
    ).to_list()


def min_price(df: pl.DataFrame) -> float:
    """Sélectionne le prix minimal du dataframe."""
    return df.select(pl.col("price")).min().item()


def max_price(df: pl.DataFrame) -> float:
    """Sélectionne le prix maximal du dataframe."""
    return df.select(pl.col("price")).max().item()
