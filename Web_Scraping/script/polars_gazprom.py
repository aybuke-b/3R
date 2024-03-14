# polars_gazprom


import polars as pl
import polars.selectors as cs
from itertools import chain
import random


def fill_iphone_15(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("model") == "iPhone 15")
        .then(pl.lit("6 Go"))
        .when(pl.col("model") == "iPhone 15 Plus")
        .then(pl.lit("6 Go"))
        .when(pl.col("model") == "iPhone 15 Pro")
        .then(pl.lit("8 Go"))
        .when(pl.col("model") == "iPhone 15 Pro Max")
        .then(pl.lit("8 Go"))
        .otherwise(pl.col("ram"))
        .alias("ram")
    )
    df = df.with_columns(
        pl.when(pl.col("model") == "iPhone 15")
        .then(pl.lit("3877 mAh"))
        .when(pl.col("model") == "iPhone 15 Plus")
        .then(pl.lit("4912 mAh"))
        .when(pl.col("model") == "iPhone 15 Pro")
        .then(pl.lit("3650 mAh"))
        .when(pl.col("model") == "iPhone 15 Pro Max")
        .then(pl.lit("4852 mAh"))
        .otherwise(pl.col("battery"))
        .alias("battery")
    )
    df = df.with_columns(
        pl.when(pl.col("model").str.contains("iPhone 15"))
        .then(pl.lit("Chine"))
        .otherwise(pl.col("made_in"))
        .alias("made_in")
    )
    return df


def fill_weight(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("model") == "Google Pixel 8")
        .then(pl.lit("187,00 g"))
        .when(pl.col("model") == "Google Pixel 8 Pro")
        .then(pl.lit("213,00 g"))
        .when(pl.col("model") == "Sony Xperia 1 V")
        .then(pl.lit("187,00 g"))
        .when(pl.col("model") == "SONY Xperia 5 V")
        .then(pl.lit("182,00 g"))
        .when(pl.col("model") == "SONY Xperia 10 V")
        .then(pl.lit("159,00 g"))
        .when(pl.col("model") == "Sony Xperia 5 IV")
        .then(pl.lit("172,00 g"))
        .otherwise(pl.col("net_weight"))
        .alias("net_weight")
    )
    return df


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
    df = df.filter((pl.col("ram").is_not_null()) & (pl.col("ram") != "Non communiqué"))
    df = df.filter(pl.col("screen_resolution") != "Non communiqué")
    df = df.filter(pl.col("das_head").is_not_null())
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


def get_valid_battery(df: pl.DataFrame) -> pl.DataFrame:
    """battery will be an int but measured as milli-amper/hour"""
    df = df.with_columns(
        pl.when(pl.col("battery") == "Li-ion 5100 mAh")
        .then(pl.lit("5100 mAh"))
        .when(pl.col("battery") == "Li-Po 4600 mAh")
        .then(pl.lit("4600 mAh"))
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


def get_logprice(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(pl.col("price").log().alias("logprice"))
    return df


def network_cleaner(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(pl.col("network").str.replace("\+", ""))
    return df


def get_das_chest(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("das_chest")
        .str.replace(" W/kg", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def get_das_head(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("das_head")
        .str.replace(" W/kg", "")
        .str.replace(",", ".")
        .cast(pl.Float64)
    )
    return df


def get_das_limbs(df: pl.DataFrame) -> pl.DataFrame:
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


def get_fast_charging(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.when(pl.col("fast_charging") == "Oui")
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        .alias("fast_charging")
    )
    return df


def get_diagonal_pixels(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("screen_resolution")
        .str.replace(" pixels", "")
        .str.split_exact("x", 1)
        .struct.rename_fields(["resolution_1", "resolution_2"])
    ).unnest("screen_resolution")
    df = df.with_columns(
        pl.col("resolution_1", "resolution_2").str.strip_chars().cast(pl.Int64)
    )
    df = df.with_columns(
        (
            pl.col("resolution_1").pow(2).alias("diagonal_pixels")
            + pl.col("resolution_2").pow(2)
        ).sqrt()
    )  # correspond à sqrt(field_0**2 + field_1**2)
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


def get_mpx_cams(df: pl.DataFrame) -> pl.DataFrame:
    df = (
        df.with_columns(
            pl.col("sensor_resolution")
            .str.extract_all(r"(\d+)")
            .list.to_struct(fields=["cam_1", "cam_2", "cam_3"])
        )
        .unnest("sensor_resolution")
        .with_columns(
            pl.col("cam_1", "cam_2", "cam_3")
            .cast(pl.Float64)
            .fill_null(strategy="zero")
        )
        .with_columns(
            pl.col("cam_1")
            .add(pl.col("cam_2").add(pl.col("cam_3")))
            .alias("mpx_backward_cam")
        )
    )
    return df


def get_scraping_date(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(pl.col("scraping_time").str.to_datetime().cast(pl.Datetime))
    return df


def get_flag(df: pl.DataFrame) -> pl.DataFrame:
    """`get_flag`: _summary_

    - Allows to map a flag to a country name.

    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> get_flag()
    ... #_test_return_"""
    df = df.with_columns(
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
    )
    return df


def random_feature(df: pl.DataFrame) -> pl.DataFrame:
    """`random_feature`:

    - Add a completely random feature
    - Especially useful for variable importance and in the selection phase

    ---------
    `Parameters`
    --------- ::

        df (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        pl.DataFrame

    `Example(s)`
    ---------

    >>> random_feature()
    ... #_test_return_"""
    df = df.with_columns(random_col=pl.lit(0)).with_columns(
        pl.col("random_col").map_elements(lambda x: random.randint(-1000, 1000))
    )
    return df


def drop_col_nulls(df: pl.DataFrame) -> pl.DataFrame:
    df = df.drop_nulls(subset=cs.contains({"made_in"}))
    return df


def get_resolution(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.concat_str([df["resolution_1"], pl.lit(" x "), df["resolution_2"]]).alias(
            "resolution"
        )
    )
    return df


def NordStream(df: pl.DataFrame) -> pl.DataFrame:
    df = (
        df.pipe(fill_iphone_15)
        .pipe(fill_weight)
        .pipe(drop_and_filter)
        .pipe(fill_usb_c)
        .pipe(get_valid_price)
        .pipe(get_valid_reviews)
        .pipe(get_stars)
        .pipe(get_upgrade_storage)
        .pipe(get_valid_battery)
        .pipe(get_screen_type)
        .pipe(get_fast_charging)
        .pipe(get_diagonal_pixels)
        .pipe(get_valid_screen_size)
        .pipe(get_valid_storage)
        .pipe(get_valid_ram)
        .pipe(get_valid_repairability)
        .pipe(get_valid_weight)
        .pipe(get_valid_height)
        .pipe(get_valid_width)
        .pipe(get_valid_thickness)
        .pipe(get_logprice)
        .pipe(network_cleaner)
        .pipe(get_das_chest)
        .pipe(get_das_head)
        .pipe(get_das_limbs)
        .pipe(get_valid_induction)
        .pipe(get_ppi)
        .pipe(get_scraping_date)
        .pipe(get_flag)
        .pipe(get_resolution)
        .pipe(get_mpx_cams)
        .pipe(format_colors)
        .pipe(random_feature)
        .pipe(drop_col_nulls)
    )
    return df
