import streamlit as st
from PIL import Image
import plotly.express as px
from modules_app.st_config import *
from modules_app.data_import import *
from modules_app.st_plots import *

fontawesome_icon = icon(type="brands", icon_name="font-awesome", color="#74C0FC")
cc_by_nc_icon = icon(type="brands", icon_name="creative-commons-nc-eu", color="#74C0FC")

page_config()
remove_white_space()
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")
version = fontawesome_import(major=6, minor=5, patch=1)
config = modebar_config()

logo = open_logo()

df = load_df()

with st.sidebar:
    st.caption("Crée par :")
    with st.container(border=True):
        st.markdown(
            """
            💻 [**Corentin DUCLOUX**](https://github.com/CDucloux) \n
            💻 [**Aybuké BICAT**](https://github.com/CDucloux)
            """
        )
    if st.button("🏠 **Retourner à l'accueil**"):
        st.switch_page("Accueil.py")

st.title("📱 Smart Specs")
st.header("Data Insights 🔎", divider="gray")
st.info("▶️ Découvrez les téléphones sous un nouvel angle !")


with st.expander("✨ **Insight 1) Prix moyen par marque**"):
    df_mean_price = load_mean_price_df(df)
    barplot_mean_price(df_mean_price=df_mean_price, logo=logo, config=config)
    least_expensive_brand = item_getter(
        df_mean_price=df_mean_price, column="brand", min=True
    )
    most_expensive_brand = item_getter(
        df_mean_price=df_mean_price, column="brand", min=False
    )
    least_expensive_price = item_getter(
        df_mean_price=df_mean_price, column="price", min=True
    )
    most_expensive_price = item_getter(
        df_mean_price=df_mean_price, column="price", min=False
    )
    st.markdown(
        f"""
        - **{least_expensive_brand}** propose les téléphones les moins chers avec un prix moyen de ⬇ {least_expensive_price} €.
        - **{most_expensive_brand}** propose les téléphones les plus chers avec un prix moyen de ⬆ {most_expensive_price} €.

        Le différentiel de prix entre les deux marques est considérable : 
        il est en effet ~ {int(most_expensive_price/least_expensive_price)} 
        fois plus important pour **{most_expensive_brand}** !

        INTERPRETATIONS A FAIRE + ajouter le seuil à 500 € pour changer la couleur de certaines barres
        selon téléphones haut/bas de gamme
        Interprétations => qui a les prix moyens les plus hauts, et les plus bas.
        """
    )

with st.expander("✨ **Insight 2) Nombre de modèles vendus par marque**"):
    df_brands = load_brands_df(df)
    st.dataframe(
        df_brands,
        hide_index=True,
        column_order=["brand", "brand_image", "count", "hist_col"],
        column_config={
            "brand": "🏷️ Marque",
            "brand_image": st.column_config.ImageColumn("Logo ™", width="medium"),
            "count": st.column_config.NumberColumn(
                "🛒 Nombre total",
                help="Le nombre de téléphones actuellement commercialisés par la marque",
                format="%.0f 📱",
            ),
            "hist_col": st.column_config.BarChartColumn(
                "📊 Diagramme en barres des prix"
            ),
        },
    )
    st.markdown("**Ajouter aussi le %age de modèles du total**")

df_ram = df.sort(pl.col("ram")).with_columns(
    pl.format("{} Go", pl.col("ram").cast(pl.Int64)).alias("ram_fmt")
)

with st.expander("✨ **Insight 3) Prix en fonction de la RAM**"):
    fig_ram = px.box(df_ram, x="ram_fmt", y="price", points="all")
    fig_ram.update_traces(
        boxpoints="all",
        hovertemplate="<b>Prix :</b> %{y}<br>" "<b>RAM :</b> %{x}<br>",
    )
    fig_ram.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        yaxis=dict(title="", ticksuffix=" €"),
        xaxis=dict(title=""),
    )
    fig_ram.add_layout_image(
        dict(
            source=logo,
            xref="paper",
            yref="paper",
            x=0.9,  # Position horizontale de l'image (0 à gauche, 1 à droite)
            y=0,  # Position verticale de l'image (0 en bas, 1 en haut)
            sizex=0.25,  # Largeur de l'image
            sizey=0.25,  # Hauteur de l'image
            xanchor="center",  # Point d'ancrage horizontal (centre)
            yanchor="bottom",  # Point d'ancrage vertical (en bas)
        )
    )
    st.plotly_chart(fig_ram, use_container_width=True, config=config)


df_stockage = df.sort(pl.col("storage")).with_columns(
    pl.format("{} Go", pl.col("storage").cast(pl.Int64)).alias("stockage_fmt")
)

with st.expander("✨ **Insight 4) Prix en fonction du stockage**"):
        fig_stockage = px.box(df_stockage, x="stockage_fmt", y="price", points="all")
        fig_stockage.update_traces(
            boxpoints="all",
            hovertemplate="<b>Prix :</b> %{y}<br>" "<b>Stockage :</b> %{x}<br>",
        )
        fig_stockage.update_layout(
            height=300,
            margin=dict(t=1, b=1, l=1, r=1),
            yaxis=dict(title="", ticksuffix=" €"),
            xaxis=dict(title=""),
        )
        fig_stockage.add_layout_image(
            dict(
                source=logo,
                xref="paper",
                yref="paper",
                x=0.9,  # Position horizontale de l'image (0 à gauche, 1 à droite)
                y=0,  # Position verticale de l'image (0 en bas, 1 en haut)
                sizex=0.25,  # Largeur de l'image
                sizey=0.25,  # Hauteur de l'image
                xanchor="center",  # Point d'ancrage horizontal (centre)
                yanchor="bottom",  # Point d'ancrage vertical (en bas)
            )
        )
        st.plotly_chart(fig_stockage, use_container_width=True, config=config)

with st.expander("✨ **Insight 5) Distribution des prix**"):
    st.subheader("⚙️ *Réglages*")
    col1, col2 = st.columns(2)
    with col1:
        marginal = st.checkbox(
            "Distribution marginale",
            help="Permet de visualiser la distribution des données **non-agrégées**.",
        )
    with col2:
        brand_color = st.checkbox(
            "Distribution par marque",
            help="Permet de subdiviser la distribution générale par **marque**",
        )

    if marginal and not brand_color:
        marginal_config = "rug"
        color_config = None
    if brand_color and not marginal:
        color_config = "brand"
        marginal_config = None
    if marginal and brand_color:
        marginal_config = "rug"
        color_config = "brand"
    if not marginal and not brand_color:
        color_config, marginal_config = None, None

    fig_hist = px.histogram(
        df,
        x="price",
        hover_data="model",
        color=color_config,
        marginal=marginal_config,
        opacity=0.85,
    )
    fig_hist.update_layout(
        height=300,
        margin=dict(t=1, b=1, l=1, r=1),
        yaxis=dict(title=""),
        xaxis=dict(title="", ticksuffix=" €"),
        legend=dict(title="🏷️ Marque"),
    )
    fig_hist.add_layout_image(
        dict(
            source=logo,
            xref="paper",
            yref="paper",
            x=0.9,  # Position horizontale de l'image (0 à gauche, 1 à droite)
            y=0.55,  # Position verticale de l'image (0 en bas, 1 en haut)
            sizex=0.25,  # Largeur de l'image
            sizey=0.25,  # Hauteur de l'image
            xanchor="center",  # Point d'ancrage horizontal (centre)
            yanchor="bottom",  # Point d'ancrage vertical (en bas)
        )
    )
    fig_hist.update_traces(
        hovertemplate="<b>Nombre :</b> %{y} téléphones<br>"
        "<b>Intervalle de prix :</b> %{x}<br>",
        selector="histogram",  # on update les traces uniquement de l'histogramme
    )
    fig_hist.update_traces(
        hovertemplate="<b>Prix :</b> %{x} €<br> "
        "<b>Modèle :</b> <i>%{customdata}</i><br>",
        selector="box",  # on update les traces uniquement du "rug"
    )
    st.plotly_chart(fig_hist, use_container_width=True, config=config)
    st.warning(
        """
        ⚠️ **Remarque** : On distingue deux *pics* dans la distribution des prix,
        il est donc très probable que la distribution soit **bimodale**, c'est à dire qu'elle résulte d'un mélange 
        de deux populations dans l'ensemble de données.
        """
    )
    st.markdown(
        """
        En effet, on peut facilement segmenter l'ensemble de données :

        - **Population 1** $\Rightarrow$ Téléphones *"bas de gamme"*
        - **Population 2** $\Rightarrow$ Téléphones *"haut de gamme"*
        """
    )

with st.expander("✨ **Insight 6) Corrélations**"):
    st.markdown(
        "**COMING SOON -- voir si il faut pas les bouger ailleurs dans d'autres graphs plus haut**"
    )
    df.select(pl.corr("ram", "storage"))

with st.expander("✨ **Insight 6) Variance, std ?**"):
    st.markdown("**A explorer**")


st.write(
    f"""
    > *Icônes* : {fontawesome_icon} **FontAwesome** version **{version[0]}**
    &mdash; *Licence* : {cc_by_nc_icon} **CC-BY-NC**
    """,
    unsafe_allow_html=True,
)
