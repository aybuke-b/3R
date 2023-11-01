# polars_gazprom


import polars as pl
from itertools import chain


def drop_and_filter(df: pl.DataFrame) -> pl.DataFrame:
    BRAND_ARRAY = (
        df.group_by("brand")
        .count()
        .sort("count", descending=True)
        .filter(pl.col("count") > 5)
        .select("brand")
        .to_numpy()
    )  # filtre df pour marque avec + de 5 modeles initialement
    BRAND_SET = set(list(chain.from_iterable(BRAND_ARRAY.tolist())))
    df = df.filter(pl.col("brand").is_in(BRAND_SET))
    df = df.drop(
        "warranty",
        "refresh_rate",
        "cpu_details",
        "sim_number",
        "bluetooth",
        "os",
        "sim_type",
    )
    # note : on dégage la garantie car c'est tout le temps 2 ans, et 2 cartes sim tt le temps
    # df = df.filter(pl.col("repairability_index").is_not_null())
    df = df.filter((pl.col("ram").is_not_null()) & (pl.col("ram") != "Non communiqué"))
    df = df.filter(pl.col("screen_resolution") != "Non communiqué")
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


def get_upgrade_storage(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("upgrade_storage").is_in({"Non", "Non communiqué"}))
        .then(pl.lit(False))
        .otherwise(pl.lit(True))
        .alias("upgrade_storage")
    )
    return df


def valid_battery(df: pl.DataFrame) -> pl.DataFrame:
    """battery will be an int but measured as milli-amper/hour"""
    df = df.with_columns(
        pl.when(pl.col("battery") == "Li-ion 5100 mAh")
        .then(pl.lit("5100 mAh"))
        .otherwise(pl.col("battery"))
        .str.replace(" mAh", "")
        .cast(pl.Int64)
        .alias("battery")
    )
    return df


def get_screen_type(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("screen_type") == "Pliable avec Stylet")
        .then(pl.lit("Pliable"))
        .when(pl.col("screen_type").is_in({"Bord à bord avec Stylet", "Bord à bord"}))
        .then(pl.lit("Borderless"))
        .otherwise(pl.col("screen_type"))
        .alias("screen_type")
    )
    return df


def logprice(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(pl.col("price").log().alias("logprice"))
    return df


def network_cleaner(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(pl.col("network").str.replace("\+", ""))
    return df


def valid_das_chest(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("das_chest")
        .str.replace(" W/kg", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def valid_das_head(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("das_head")
        .str.replace(" W/kg", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def valid_das_limbs(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("das_limbs")
        .str.replace(" W/kg", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def format_colors(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("color").is_in({"Graphite Black", "Noir Volcanique"}))
        .then(pl.lit("Noir"))
        .when(
            pl.col("color").is_in(
                {"Vert Citron", "Vert Sauge", "Vert Emeraude", "Bleu/vert", "Sauge"}
            )
        )
        .then(pl.lit("Vert"))
        .when(
            pl.col("color").is_in(
                {"Bleu clair", "Bleu Azur", "Bleu foncé", "Bleu d'encre"}
            )
        )
        .then(pl.lit("Bleu"))
        .when(pl.col("color").is_in({"Noir / Gris Sidéral", "Gris ciel", "Anthracite"}))
        .then(pl.lit("Gris"))
        .when(pl.col("color").is_in({"Neige", "Crème", "Porcelaine"}))
        .then(pl.lit("Blanc"))
        .when(pl.col("color") == "Silver Blue")
        .then(pl.lit("Argent"))
        .when(pl.col("color") == "Lavande")
        .then(pl.lit("Violet"))
        .when(pl.col("color") == "Rose doré")
        .then(pl.lit("Rose"))
        .otherwise(pl.col("color"))
        .alias("color")
    )
    return df


def valid_fast_charging(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("fast_charging") == "Oui")
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        .alias("fast_charging")
    )
    return df


def get_diagonal_pixels(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("screen_resolution").str.replace(" pixels", "").str.split_exact("x", 1)
    ).unnest("screen_resolution")
    df = df.with_columns(pl.col("field_0", "field_1").str.strip_chars().cast(pl.Int64))
    df = df.with_columns(
        (
            pl.col("field_0").pow(2).alias("diagonal_pixels") + pl.col("field_1").pow(2)
        ).sqrt()
    )  # correspond à sqrt(field_0**2 + field_1**2)
    df = df.drop(
        "field_0", "field_1"
    )  # a voir, on peut les garder plus tard pour la resolution
    return df


def get_valid_screen_size(df: pl.DataFrame) -> pl.DataFrame:
    """On obtient la screen_size en inch"""
    df = df.with_columns(
        pl.col("screen_size")
        .str.split(" soit")
        .map_elements(
            lambda x: x[0]
        )  # extrait uniquement la première partie avant le délimiteur
        .str.replace('"', "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def get_ppi(df: pl.DataFrame) -> pl.DataFrame:
    """On obtient les pixels per inch"""
    df = df.with_columns(
        pl.col("diagonal_pixels").truediv(pl.col("screen_size")).alias("ppi")
    )
    return df


def get_valid_storage(df: pl.DataFrame) -> pl.DataFrame:
    """`get_valid_storage`:

    - Transforms the storage from 1000 Go to 1000
    - Unit of measurement : Go

    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): # polars DataFrame

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> get_valid_storage()
    ... #_test_return_"""
    df = df.with_columns(
        pl.when(pl.col("storage") == "1 To")
        .then(pl.lit("1000 Go"))
        .when(pl.col("storage") == "512 Go (UFS 3.1)")
        .then(pl.lit("512 Go"))
        .otherwise(pl.col("storage"))
        .alias("storage")
        .str.replace(" Go", "")
        .cast(pl.Int64)
    )
    return df


def get_valid_ram(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(pl.col("ram").str.replace(" Go", "").cast(pl.Int64))
    return df


def get_valid_induction(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("charging_type") == "Possibilité de charger par induction")
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        .alias("induction")
    ).drop("charging_type")
    return df


def get_valid_height(df: pl.DataFrame) -> pl.DataFrame:
    """`get_valid_height`:

    - Transforms the height
    - Unit of measurement : millimeters
    """
    df = df.with_columns(
        pl.col("height").str.replace(" mm", "").str.replace(",", ".").cast(pl.Float64)
    )
    return df


def get_valid_width(df: pl.DataFrame) -> pl.DataFrame:
    """`get_valid_width`:

    - Transforms the width
    - Unit of measurement : millimeters
    """
    df = df.with_columns(
        pl.col("width").str.replace(" mm", "").str.replace(",", ".").cast(pl.Float64)
    )
    return df


def get_valid_thickness(df: pl.DataFrame) -> pl.DataFrame:
    """`get_valid_thickness`:

    - Transforms the width
    - Unit of measurement : millimeters
    """
    df = df.with_columns(
        pl.col("thickness")
        .str.replace(" mm", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def get_valid_repairability(df: pl.DataFrame) -> pl.DataFrame:
    """`get_valid_repairability`:

    - Transforms the repairability index from 8,6 /10 to 8.6
    - Unit of measurement : /10


    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): # polars DataFrame

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> get_valid_repairability()
    ... #_test_return_"""
    df = df.with_columns(
        pl.col("repairability_index")
        .str.replace(" /10", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def get_valid_weight(df: pl.DataFrame) -> pl.DataFrame:
    """`get_valid_weight`:

    - Transforms the net weight from 192,8 g to 192.8
    - Unit of measurement : grams

    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): # polars DataFrame

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> get_valid_weight()
    ... #_test_return_"""
    df = df.with_columns(
        pl.col("net_weight")
        .str.replace(" g", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def NordStream(df: pl.DataFrame) -> pl.DataFrame:
    df = (
        df.pipe(drop_and_filter)
        .pipe(fill_usb_c)
        .pipe(get_valid_price)
        .pipe(get_valid_reviews)
        .pipe(get_stars)
        .pipe(get_upgrade_storage)
        .pipe(valid_battery)
        .pipe(get_screen_type)
        .pipe(format_colors)
        .pipe(valid_fast_charging)
        .pipe(get_diagonal_pixels)
        .pipe(get_valid_screen_size)
        .pipe(get_ppi)
        .pipe(get_valid_storage)
        .pipe(get_valid_ram)
        .pipe(get_valid_repairability)
        .pipe(get_valid_weight)
        .pipe(get_valid_height)
        .pipe(get_valid_width)
        .pipe(get_valid_thickness)
        .pipe(logprice)
        .pipe(network_cleaner)
        .pipe(valid_das_chest)
        .pipe(valid_das_head)
        .pipe(valid_das_limbs)
        .pipe(get_valid_induction)
    )
    return df
