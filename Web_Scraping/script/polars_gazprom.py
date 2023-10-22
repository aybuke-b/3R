# polars_gazprom


import polars as pl


def drop_and_filter(df: pl.DataFrame) -> pl.DataFrame:
    df = df.drop("warranty", "refresh_rate", "cpu_details")
    df = df.filter(pl.col("repairability_index").is_not_null())
    df = df.filter((pl.col("ram").is_not_null()) & (pl.col("ram") != "Non communiqué"))
    return df


def fill_usb_c(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("usb_type_c") == "Oui")
        .then(pl.lit(True))
        .when((pl.col("usb_type_c").is_null()) & (pl.col("brand") != "APPLE"))
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        # les valeurs nulls sont majoritairement chez apple CAR ils n'ont pas d'USB-C !
        .alias("usb_type_c")
    )
    return df


def get_valid_price(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("price").str.replace(",", ".").str.replace("€", "").cast(pl.Float64)
    )
    return df


def get_valid_reviews(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("reviews").str.replace("\(", "").str.replace("\)", "").cast(pl.Int64)
    )
    return df


def get_stars(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("stars").str.extract(r'<bl-rating rating="([\d.]+)">').cast(pl.Float64)
    )
    return df


def NordStream(df: pl.DataFrame) -> pl.DataFrame:
    df = (
        df.pipe(drop_and_filter)
        .pipe(fill_usb_c)
        .pipe(get_valid_price)
        .pipe(get_valid_reviews)
        .pipe(get_stars)
    )
    return df
