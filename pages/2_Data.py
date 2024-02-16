import streamlit as st
import polars as pl
from streamlit.delta_generator import DeltaGenerator
from pathlib import Path
from modules_app.data_import import *


def remove_white_space() -> DeltaGenerator:
    """`remove_white_space`: Utilise du CSS pour retirer de l'espace non-utilisé.

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------
    >>> remove_white_space(df)
    ... DeltaGenerator()"""
    return st.markdown(
        """
        <style>
                .st-emotion-cache-1y4p8pa {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
                .st-emotion-cache-16txtl3{
                    padding-top: 1.5rem;
                    padding-right: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                }
        </style>
        """,
        unsafe_allow_html=True,
    )





def main():
    remove_white_space()
    st.title("📱 Phone Finder")
    df = load_df()
    df = better_countries(df)

    # st.write(df.columns)

    with st.sidebar:
        # Configure l'ensemble de la sidebar de paramètres
        st.header("*Paramètres*")
        ram_value = st.selectbox(
            "RAM :",
            sorted(ram_list(df)),
            placeholder="Choisir la RAM",
            index=None,
        )

        storage_value = st.selectbox(
            "Stockage :",
            sorted(storage_list(df)),
            index=None,
            placeholder="Choisir le stockage",
        )

        selected_brands = st.multiselect(
            "Choisir une ou plusieurs marques :",
            sorted(brand_list(df)),
            placeholder="Choisir la marque",
        )

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

    st.header("Telephone")


if __name__ == "__main__":
    main()
