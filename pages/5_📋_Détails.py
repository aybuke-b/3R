import streamlit as st
import polars as pl
from modules_app.data_import import load_df
from modules_app.selectors import *
from modules_app.st_config import *
from modules_app.st_tables import main_details_table


def main():
    page_config()
    remove_white_space()
    font_import(font="Audiowide")
    font_apply(font="Audiowide", tag="h1")
    version = fontawesome_import(major=6, minor=5, patch=1)
    fontawesome_icon = icon(type="brands", icon_name="font-awesome", color="#74C0FC")
    cc_by_nc_icon = icon(
        type="brands", icon_name="creative-commons-nc-eu", color="#74C0FC"
    )
    st.title("📱 Smart Specs")
    df = load_df()

    with st.sidebar:
        st.header("*Paramètres*")

        selected_brands = st.multiselect(
            "Choisir une ou plusieurs marques :",
            options=ordered_brand_list(df),
            placeholder="Choisir la marque",
        )

        storage_value = st.selectbox(
            "Stockage :",
            ordered_storage_list(df, selected_brands),
            index=None,
            placeholder="Choisir le stockage",
        )

        if storage_value != None:
            storage_value = float(storage_value.replace("Go", ""))

        ram_value = st.selectbox(
            "RAM :",
            ordered_ram_list(df, selected_brands, storage_value),
            placeholder="Choisir la RAM",
            index=None,
        )

        if ram_value != None:
            ram_value = float(ram_value.replace("Go", ""))

        if st.button("🏠 **Retourner à l'accueil**"):
            st.switch_page("Accueil.py")

    if not (ram_value or storage_value or selected_brands):
        mutable_df = df
    else:
        mutable_df = df
        if ram_value:
            mutable_df = mutable_df.filter(pl.col("ram") == ram_value)
        if storage_value:
            mutable_df = mutable_df.filter(pl.col("storage") == storage_value)
        if selected_brands:
            mutable_df = mutable_df.filter(pl.col("brand").is_in(selected_brands))

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.metric("Nombre total de téléphones", value=f"🎰 {len(mutable_df)}")
    with col2:
        with st.container(border=True):
            st.metric(
                "Prix moyen",
                value=f" 💶 {round(mutable_df.select(pl.col('price').mean()).item(),2)} €",
            )
    main_details_table(mutable_df)

    st.write(
        f"""
    > *Icônes* : {fontawesome_icon} **FontAwesome** version **{version[0]}**
    &mdash; *Licence* : {cc_by_nc_icon} **CC-BY-NC**
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
