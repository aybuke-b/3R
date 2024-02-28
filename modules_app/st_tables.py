import polars as pl
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def brand_table(df_brands: pl.DataFrame) -> DeltaGenerator:
    """`brand_table`: (PAGE 2) Génère le tableau du nombre de téléphones par marque.

    ---------
    `Parameters`
    --------- ::

        df_brands (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        _type_

    `Example(s)`
    ---------

    >>> brand_table()
    ... #_test_return_"""
    return st.dataframe(
        df_brands,
        hide_index=True,
        column_order=["brand", "brand_image", "count", "percent_count", "hist_col"],
        column_config={
            "brand": "🏷️ Marque",
            "brand_image": st.column_config.ImageColumn("Logo ™", width="medium"),
            "count": st.column_config.NumberColumn(
                "🛒 Nombre total",
                help="Le nombre de téléphones actuellement commercialisés par la marque",
                format="%.0f 📱",
            ),
            "percent_count": st.column_config.NumberColumn(
                "➗ Pourcentage du total",
                help="La **part de marché** de la marque sur la plateforme",
                format="%.2f %%",
            ),
            "hist_col": st.column_config.BarChartColumn(
                "📊 Diagramme en barres des prix"
            ),
        },
    )


def main_details_table(mutable_df: pl.DataFrame) -> DeltaGenerator:
    """`main_table`: (PAGE 5) Affichage du tableau principal filtrable.

    ---------
    `Parameters`
    --------- ::

        mutable_df (pl.DataFrame): #_description_

    `Returns`
    --------- ::

        DeltaGenerator

    `Example(s)`
    ---------

    >>> main_table()
    ... #_test_return_"""
    return st.dataframe(
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
