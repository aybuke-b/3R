import streamlit as st
import polars as pl
from modules_app.st_config import (
    page_config,
    remove_white_space,
    fontawesome_import,
    font_import,
    font_apply,
    icon,
    underline_decoration,
)
from modules_app.data_import import (
    load_df,
    load_mean_price_df,
    load_brands_df,
    load_ram_df,
    load_storage_df,
    item_getter,
)
from modules_app.st_plots import (
    modebar_config,
    open_logo,
    barplot_mean_price,
    boxplot_ram,
    boxplot_storage,
    hist_price,
)
from modules_app.st_tables import brand_table

fontawesome_icon = icon(type="brands", icon_name="font-awesome", color="#74C0FC")
cc_by_nc_icon = icon(type="brands", icon_name="creative-commons-nc-eu", color="#74C0FC")
github_icon = icon(type="brands", icon_name="github", size="lg")

page_config()
remove_white_space()
underline_decoration()
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
            f"""
            {github_icon} [**Corentin DUCLOUX**](https://github.com/CDucloux) \n
            {github_icon} [**Aybuké BICAT**](https://github.com/aybuke-b)
            """,
            unsafe_allow_html=True,
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
        """
    )

with st.expander("✨ **Insight 2) Nombre de modèles vendus par marque**"):
    df_brands = load_brands_df(df)
    brand_table(df_brands=df_brands)


with st.expander("✨ **Insight 3) Prix en fonction de la RAM**"):
    df_ram = load_ram_df(df)
    boxplot_ram(df_ram=df_ram, logo=logo, config=config)


with st.expander("✨ **Insight 4) Prix en fonction du stockage**"):
    df_storage = load_storage_df(df)
    boxplot_storage(df_storage=df_storage, logo=logo, config=config)

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

    hist_price(
        df=df,
        color_config=color_config,
        marginal_config=marginal_config,
        logo=logo,
        config=config,
    )

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

st.write(
    f"""
    > *Icônes* : {fontawesome_icon} **FontAwesome** version **{version[0]}**
    &mdash; *Licence* : {cc_by_nc_icon} **CC-BY-NC**
    """,
    unsafe_allow_html=True,
)
