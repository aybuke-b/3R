import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
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

    fig = px.timeline(
        source.sort_values("start"),
        x_start="start",
        x_end="end",
        y="technologie",
        text="technologie",
        color="catégorie",
        color_discrete_sequence=["#4E6766", "#E4572E", "#A5C882", "#1E152A", "#5AB1BB"],
    )
    fig.update_yaxes(title="y", visible=False, showticklabels=False)

    fig.update_layout(
        xaxis_range=["1989", "2027"],
        paper_bgcolor="#222222",
        font_color="black",
        legend_font_color="white",
        title_font_color="white",
        xaxis=dict(color="white"),
        margin=dict(l=30, r=30, b=30, t=30, pad=3),
    )

    return fig
