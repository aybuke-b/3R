import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import chain
import pandas as pd
import polars as pl
import random


def hedonic_graph_loader() -> go.Figure:
    num_points = 6
    random.seed(42)  # fix a seed.
    x = [random.randint(0, 10) for _ in range(num_points)]
    y = [random.randint(0, 10) for _ in range(num_points)]
    products = ["bien 1", "bien 2", "bien 3", "bien 4", "bien 5", "bien 6"]

    fig = px.scatter(
        x=x,
        y=y,
        color=products,
        title="$\\text{Plan }(z_1, z_2)\\text{ de differents biens avec 2 caracteristiques.}$",
    )

    fig.update_layout(
        xaxis=dict(title=r"$z_1$", title_font=dict(size=22)),
        yaxis=dict(title=r"$z_2$", title_font=dict(size=22)),
        paper_bgcolor="#222222",
        font_color="white",
        margin=dict(l=30, r=30, b=30, t=30, pad=3),
    )

    fig.update_traces(marker=dict(size=15))

    return fig


def smartphone_graph_loader() -> go.Figure:
    source = pd.DataFrame(
        [
            {
                "technologie": "Motorola – MicroTAC 9800X 📠",
                "start": "1989-04-01",
                "end": "1996-01-01",
                "catégorie": "Téléphone à clapet",
            },
            {
                "technologie": "Nokia – 1011 ⌨",
                "start": "1992-11-01",
                "end": "1994-01-01",
                "catégorie": "Téléphone à clavier",
            },
            {
                "technologie": "Apparition des SMS 💬",
                "start": "1992-01-01",
                "end": "2024-01-01",
                "catégorie": "Autres",
            },
            {
                "technologie": "IBM – Simon 📱",
                "start": "1994-08-01",
                "end": "1995-02-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Motorola – StarTAC 📠",
                "start": "1996-01-01",
                "end": "1998-01-01",
                "catégorie": "Téléphone à clapet",
            },
            {
                "technologie": "Apparition des Emojis 😀",
                "start": "1998-01-01",
                "end": "2024-01-01",
                "catégorie": "Autres",
            },
            {
                "technologie": "Nokia – 3210 ⌨",
                "start": "1999-03-01",
                "end": "2002-04-01",
                "catégorie": "Téléphone à clavier",
            },
            {
                "technologie": "Sharp – J-SH04 📷",
                "start": "1999-01-01",
                "end": "2000-01-01",
                "catégorie": "Téléphone à appareil photo",
            },
            {
                "technologie": "Blackberry Quark ⌨",
                "start": "2003-01-01",
                "end": "2005-01-01",
                "catégorie": "Téléphone à clavier",
            },
            {
                "technologie": "Apple – Iphone 📱",
                "start": "2007-06-01",
                "end": "2008-07-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Android OS 🤖",
                "start": "2005-01-01",
                "end": "2024-01-01",
                "catégorie": "Autres",
            },
            {
                "technologie": "HTC – Dream 📱",
                "start": "2008-01-01",
                "end": "2010-07-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Apple – Iphone 4 📱",
                "start": "2010-06-01",
                "end": "2013-09-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Samsung Galaxy S 📱",
                "start": "2010-06-01",
                "end": "2012-03-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Samsung Galaxy Note 📱",
                "start": "2011-10-01",
                "end": "2012-09-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "One Plus One 📱",
                "start": "2014-04-01",
                "end": "2016-04-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Apple Iphone X 📱",
                "start": "2017-11-01",
                "end": "2018-09-01",
                "catégorie": "Smartphone",
            },
            {
                "technologie": "Samsung Galaxy Fold 📱",
                "start": "2019-09-01",
                "end": "2018-12-01",
                "catégorie": "Smartphone",
            },
        ]
    )

    source["start"] = pd.to_datetime(source["start"])
    source["end"] = pd.to_datetime(source["end"])

    timeline = px.timeline(
        source.sort_values("start"),
        x_start="start",
        x_end="end",
        y="technologie",
        text="technologie",
        color="catégorie",
        color_discrete_sequence=["#4E6766", "#E4572E", "#A5C882", "#1E152A", "#5AB1BB"],
    )
    timeline.update_yaxes(title="y", visible=False, showticklabels=False)

    timeline.update_layout(
        xaxis_range=["1989", "2027"],
        paper_bgcolor="#222222",
        font_color="black",
        legend_font_color="white",
        title_font_color="white",
        xaxis=dict(color="white"),
        margin=dict(l=30, r=30, b=30, t=30, pad=3),
    )

    return timeline


def table_null_values(df: pl.DataFrame) -> pl.DataFrame:
    null_count = list(
        chain.from_iterable(df.select(pl.all().is_null().sum()).to_numpy().tolist())
    )
    df_missing_values = pl.DataFrame(
        {
            "variables": df.columns,
            "somme_nulls": null_count,
        }
    )

    df_missing_values = df_missing_values.with_columns(
        pl.col("somme_nulls")
        .truediv(df.shape[0])
        .mul(100)
        .round(2)
        .alias("%age valeurs manquantes")
    )

    return df_missing_values.sort("somme_nulls", descending=True).limit(9)


def prices_graph_loader(df: pl.DataFrame) -> go.Figure:
    df_prices = (
        df.group_by("brand")
        .agg([pl.mean("price").round(2).alias("avg_price")])
        .sort("avg_price", descending=True)
    )
    mean_price = df.select("price").mean().item()
    bar = px.bar(
        x="brand",
        y="avg_price",
        title="Prix moyen des smartphones par marque",
        height=375,
        color_discrete_sequence=["white"],
        data_frame=df_prices,
    )

    bar.add_hline(
        mean_price,
        line_dash="dash",
        line_color="#ffa07a",
        annotation_text=f"prix moyen de la sélection : {round(mean_price,2)} €",
        annotation_position="top right",
    )
    bar.update_layout(
        yaxis=dict(ticksuffix=" €"),
        paper_bgcolor="#222222",
        plot_bgcolor="#222222",
        font_color="white",
        margin=dict(l=30, r=30, b=30, pad=3),
    )
    bar.update_yaxes(title="")
    bar.update_xaxes(title="")
    return bar


def count_graph_loader(df: pl.DataFrame) -> go.Figure:
    df_models = (
        df.group_by(pl.col("brand"))
        .count()
        .sort("count", descending=True)
        .with_columns(
            pl.col("count").truediv(len(df)).mul(100).alias("part relative").round(2)
        )
        .with_columns(pl.cumsum("part relative").alias("cumsum"))
    )

    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    bar = px.bar(
        x="brand",
        y="count",
        text="count",
        color_discrete_sequence=["white"],
        data_frame=df_models,
    )
    bar.update_yaxes(title="")
    bar.update_xaxes(title="")

    line = px.line(
        x="brand",
        y="cumsum",
        color_discrete_sequence=["green"],
        data_frame=df_models,
    )
    line.update_traces(yaxis="y2")

    subfig.add_traces(bar.data + line.data)
    subfig.update_layout(
        paper_bgcolor="#222222",
        plot_bgcolor="#222222",
        font_color="white",
        margin=dict(l=30, r=30, b=30, pad=3),
        title="Nombre de smartphones proposés par marque",
        yaxis2=dict(ticksuffix=" %"),
        height=375,
    )
    subfig.update_yaxes(showgrid=False)
    return subfig


def hist_prices_loader(df: pl.DataFrame) -> go.Figure:
    hist = px.histogram(
        x="price",
        opacity=0.8,
        data_frame=df,
        histnorm="probability density",
        title="Distribution des prix - fonction de densité de probabilité",
        height=400,
    )
    hist.update_layout(
        xaxis=dict(ticksuffix=" €"),
        paper_bgcolor="#222222",
        plot_bgcolor="#222222",
        font_color="white",
        margin=dict(l=30, r=30, b=30, pad=3),
    )
    hist.update_yaxes(title="")
    hist.update_xaxes(title="")
    return hist
