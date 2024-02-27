import streamlit as st
import polars as pl
from streamlit.delta_generator import DeltaGenerator
from pathlib import Path
from modules_app.data_import import *
from modules_app.selectors import *
from modules_app.st_config import *


def main():
    page_config()
    remove_white_space()
    version = fontawesome_import(major=6, minor=5, patch=1)
    font_import(font="Audiowide")
    font_apply(font="Audiowide", tag="h1")
    st.title("📱 Smart Specs")
    df = load_df()

    # st.write(df.columns)

    with st.sidebar:
        # Configure l'ensemble de la sidebar de paramètres
        st.header("*Paramètres*")

        selected_brands = st.multiselect(
            "Choisir une ou plusieurs marques :",
            options=sorted(brand_list(df)),
            placeholder="Choisir la marque",
        )

        storage_value = st.selectbox(
            "Stockage :",
            (
                df.filter(pl.col("brand").is_in(selected_brands))
                .select(pl.col("storage"))
                .unique()
                .cast(pl.Int64)
                .sort("storage")
                .to_series()
                + " Go"
            ).to_list(),
            index=None,
            placeholder="Choisir le stockage",
        )

        if storage_value != None:
            storage_value = float(storage_value.replace("Go", ""))

        ram_value = st.selectbox(
            "RAM :",
            (
                df.filter(pl.col("brand").is_in(selected_brands))
                .filter(pl.col("storage").is_in(storage_value))
                .select(pl.col("ram"))
                .unique()
                .cast(pl.Int64)
                .sort("ram")
                .to_series()
                + " Go"
            ).to_list(),
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

    st.dataframe(
        mutable_df,
        hide_index=True,
        column_order=[
            "model",
            "image",
            "brand",
            "price",
            "efficiency",
            "prediction_sfa",
            "prediction_loghedonic",
            "ram",
            "storage",
            "induction",
            "screen_size",
            "resolution",
            "made_in",
            "upgrade_storage",
            "das_head",
            "das_limbs",
            "das_chest",
            "fast_charging",
            "network",
            "ppi",
            "battery",
            "color",
            "repairability_index",
            "usb_type_c",
            "screen_type",
        ],
        column_config={
            "model": "📱 Modèle de téléphone",
            "image": st.column_config.ImageColumn("📷 Image"),
            "brand": "🏷️ Marque",
            "price": st.column_config.NumberColumn(
                "💲 Prix Affiché",
                help="Le prix du téléphone en euros",
                format="%.2f €",
            ),
            "efficiency": st.column_config.ProgressColumn(
                "🥇 Efficacité du prix", min_value=0, max_value=1, format="%.2f"
            ),
            "prediction_sfa": st.column_config.NumberColumn(
                "💰 Prix prédit (SFA)",
                format="%.2f €",
            ),
            "prediction_loghedonic": st.column_config.NumberColumn(
                "💰 Prix prédit (OLS)",
                format="%.2f €",
            ),
            "ram": st.column_config.NumberColumn(
                "RAM",
                format="%.0f Go",
            ),
            "storage": st.column_config.NumberColumn(
                "💽 Stockage",
                format="%.0f Go",
            ),
            "induction": st.column_config.CheckboxColumn("♨️ Charge à induction"),
            "screen_size": st.column_config.NumberColumn(
                "📐 Taille de l'écran",
                format="%.1f pouces",
            ),
            "made_in": st.column_config.TextColumn("🗺️ Lieu de fabrication"),
            "upgrade_storage": st.column_config.CheckboxColumn(
                "⏫ Augmentation du stockage"
            ),
            "das_head": st.column_config.NumberColumn("⚠️ DAS Tête", format="%.2f W/kg"),
            "das_limbs": st.column_config.NumberColumn(
                "⚠️ DAS Membres", format="%.2f W/kg"
            ),
            "das_chest": st.column_config.NumberColumn(
                "⚠️ DAS Poitrine", format="%.2f W/kg"
            ),
            "fast_charging": st.column_config.CheckboxColumn("⚡ Charge Rapide"),
            "network": st.column_config.TextColumn("📶 Réseau"),
            "battery": st.column_config.NumberColumn("🔋 Batterie", format="%.0f mAh"),
            "color": st.column_config.TextColumn("🎨 Coloris"),
            "repairability_index": st.column_config.NumberColumn(
                "👨‍🔧 Indice de réparabilité", format="%.1f /10"
            ),
            "usb_type_c": st.column_config.CheckboxColumn("🔌 USB Type C"),
            "screen_type": st.column_config.TextColumn("🤳 Type d'écran"),
            "resolution": st.column_config.TextColumn("💡 Résolution"),
        },
    )


if __name__ == "__main__":
    main()


fontawesome_icon = icon(type="brands", icon_name="font-awesome", color="#74C0FC")
cc_by_nc_icon = icon(type="brands", icon_name="creative-commons-nc-eu", color="#74C0FC")
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")
version = fontawesome_import(major=6, minor=5, patch=1)


st.write(
    f"""
    > *Icônes* : {fontawesome_icon} **FontAwesome** version **{version[0]}**
    &mdash; *Licence* : {cc_by_nc_icon} **CC-BY-NC**
    """,
    unsafe_allow_html=True,
)
