import streamlit as st
from modules_app.data_import import *
from modules_app.st_config import *
from modules_app.queries import *

page_config()
remove_white_space()
font_import(font="Audiowide")
font_apply(font="Audiowide", tag="h1")

df_1 = load_df()
df_2 = load_df()

st.title("📱 Smart Specs")
st.header("Comparateur", divider="gray")

with st.sidebar:
    with st.expander("**Modèle 1**"):
        model_1 = st.selectbox(
            "Choisir le modèle",
            df_1.select("model").unique().sort("model").to_series().to_list(),
            index=0,
            key="model_1_selectbox",
        )
        storage_user_1 = st.selectbox(
            "Choisir le stockage",
            (
                df_1.filter(pl.col("model") == model_1)
                .select(pl.col("storage"))
                .unique()
                .cast(pl.Int64)
                .sort("storage")
                .to_series()
                + " Go"
            ).to_list(),
            key="storage_1_selectbox",
        )

        storage_1 = float(storage_user_1.replace("Go", ""))

        color_1 = st.selectbox(
            "Choisir la couleur",
            df_1.filter((pl.col("model") == model_1) & (pl.col("storage") == storage_1))
            .select(pl.col("color"))
            .unique()
            .sort("color")
            .to_series()
            .to_list(),
            key="color_1_selectbox",
        )

    with st.expander("**Modèle 2**"):
        model_2 = st.selectbox(
            "Choisir le modèle du téléphone",
            df_2.select("model").unique().sort("model").to_series().to_list(),
            index=1,
            key="model_2_selectbox",
        )
        storage_user_2 = st.selectbox(
            "Choisir le stockage",
            (
                df_2.filter(pl.col("model") == model_2)
                .select(pl.col("storage"))
                .unique()
                .cast(pl.Int64)
                .sort("storage")
                .to_series()
                + " Go"
            ).to_list(),
            key="storage_2_selectbox",
        )

        storage_2 = float(storage_user_2.replace("Go", ""))

        color_2 = st.selectbox(
            "Choisir la couleur",
            df_2.filter((pl.col("model") == model_2) & (pl.col("storage") == storage_2))
            .select(pl.col("color"))
            .unique()
            .sort("color")
            .to_series()
            .to_list(),
            key="color_2_selectbox",
        )


def resolution_description(
    sensor: float | None, cam_1: float, cam_2: float, cam_3: float
) -> str:
    match sensor:
        case 1.0:
            cams_resolution = f"{int(cam_1)} mpx"
        case 2.0:
            cams_resolution = f"{int(cam_1)} mpx + {int(cam_2)} mpx"
        case 3.0:
            cams_resolution = f"{int(cam_1)} mpx + {int(cam_2)} mpx + {int(cam_3)} mpx"
        case 4.0:
            cams_resolution = f"{int(cam_1)} mpx + {int(cam_2)} mpx + {int(cam_3)} mpx"
        case _:
            cams_resolution = "Aucune information disponible"
    return cams_resolution


def format_sensor(sensor: float | None) -> str | int:
    if sensor is None:
        sensor = "Aucune information disponible"
    else:
        sensor = int(sensor)
    return sensor


def note_description(reviews: float | None, stars: float) -> str | int:
    nb_stars = ""
    if reviews is not None:
        if reviews > 0.0:
            nb_stars = f"⭐ {round(stars, 2)}"
    return nb_stars


ctx = create_context()

link_model_1 = execute_query_phone(ctx, df_1, "image", model_1, storage_1, color_1)
model_model_1 = execute_query_phone(ctx, df_1, "model", model_1, storage_1, color_1)
ram_model_1 = execute_query_phone(ctx, df_1, "ram", model_1, storage_1, color_1)
price_model_1 = execute_query_phone(ctx, df_1, "price", model_1, storage_1, color_1)
efficiency_model_1 = execute_query_phone(
    ctx, df_1, "efficiency", model_1, storage_1, color_1
)
brand_model_1 = execute_query_phone(ctx, df_1, "brand", model_1, storage_1, color_1)
storage_model_1 = execute_query_phone(ctx, df_1, "storage", model_1, storage_1, color_1)
cpu_model_1 = execute_query_phone(ctx, df_1, "cpu", model_1, storage_1, color_1)
network_model_1 = execute_query_phone(ctx, df_1, "network", model_1, storage_1, color_1)
flag_model_1 = execute_query_phone(ctx, df_1, "flag", model_1, storage_1, color_1)
made_in_model_1 = execute_query_phone(ctx, df_1, "made_in", model_1, storage_1, color_1)
reviews_model_1 = execute_query_phone(ctx, df_1, "reviews", model_1, storage_1, color_1)
stars_model_1 = execute_query_phone(ctx, df_1, "stars", model_1, storage_1, color_1)
screen_type_model_1 = execute_query_phone(
    ctx, df_1, "screen_type", model_1, storage_1, color_1
)
screen_tech_model_1 = execute_query_phone(
    ctx, df_1, "screen_tech", model_1, storage_1, color_1
)
screen_size_model_1 = execute_query_phone(
    ctx, df_1, "screen_size", model_1, storage_1, color_1
)
resolution_model_1 = execute_query_phone(
    ctx, df_1, "resolution", model_1, storage_1, color_1
)
ppi_model_1 = execute_query_phone(ctx, df_1, "ppi", model_1, storage_1, color_1)
battery_model_1 = execute_query_phone(ctx, df_1, "battery", model_1, storage_1, color_1)
color_model_1 = execute_query_phone(ctx, df_1, "color", model_1, storage_1, color_1)

fast_charging_model_1 = execute_query_phone(
    ctx, df_1, "fast_charging", model_1, storage_1, color_1
)
induction_model_1 = execute_query_phone(
    ctx, df_1, "induction", model_1, storage_1, color_1
)
usb_type_c_model_1 = execute_query_phone(
    ctx, df_1, "usb_type_c", model_1, storage_1, color_1
)

height_model_1 = execute_query_phone(ctx, df_1, "height", model_1, storage_1, color_1)
width_model_1 = execute_query_phone(ctx, df_1, "width", model_1, storage_1, color_1)
thickness_model_1 = execute_query_phone(
    ctx, df_1, "thickness", model_1, storage_1, color_1
)
net_weight_model_1 = execute_query_phone(
    ctx, df_1, "net_weight", model_1, storage_1, color_1
)

das_head_model_1 = execute_query_phone(
    ctx, df_1, "das_head", model_1, storage_1, color_1
)
das_chest_model_1 = execute_query_phone(
    ctx, df_1, "das_chest", model_1, storage_1, color_1
)
das_limbs_model_1 = execute_query_phone(
    ctx, df_1, "das_limbs", model_1, storage_1, color_1
)

sensor_model_1 = execute_query_phone(ctx, df_1, "sensor", model_1, storage_1, color_1)

cam_1_model_1 = execute_query_phone(ctx, df_1, "cam_1", model_1, storage_1, color_1)

cam_2_model_1 = execute_query_phone(ctx, df_1, "cam_2", model_1, storage_1, color_1)

cam_3_model_1 = execute_query_phone(ctx, df_1, "cam_3", model_1, storage_1, color_1)
######## MODEL 2

link_model_2 = execute_query_phone(ctx, df_2, "image", model_2, storage_2, color_2)
model_model_2 = execute_query_phone(ctx, df_2, "model", model_2, storage_2, color_2)
ram_model_2 = execute_query_phone(ctx, df_2, "ram", model_2, storage_2, color_2)
price_model_2 = execute_query_phone(ctx, df_2, "price", model_2, storage_2, color_2)
efficiency_model_2 = execute_query_phone(
    ctx, df_2, "efficiency", model_2, storage_2, color_2
)
brand_model_2 = execute_query_phone(ctx, df_2, "brand", model_2, storage_2, color_2)
storage_model_2 = execute_query_phone(ctx, df_2, "storage", model_2, storage_2, color_2)
cpu_model_2 = execute_query_phone(ctx, df_2, "cpu", model_2, storage_2, color_2)
network_model_2 = execute_query_phone(ctx, df_2, "network", model_2, storage_2, color_2)
flag_model_2 = execute_query_phone(ctx, df_2, "flag", model_2, storage_2, color_2)
made_in_model_2 = execute_query_phone(ctx, df_2, "made_in", model_2, storage_2, color_2)
reviews_model_2 = execute_query_phone(ctx, df_2, "reviews", model_2, storage_2, color_2)
stars_model_2 = execute_query_phone(ctx, df_2, "stars", model_2, storage_2, color_2)
screen_type_model_2 = execute_query_phone(
    ctx, df_2, "screen_type", model_2, storage_2, color_2
)
screen_tech_model_2 = execute_query_phone(
    ctx, df_2, "screen_tech", model_2, storage_2, color_2
)
screen_size_model_2 = execute_query_phone(
    ctx, df_2, "screen_size", model_2, storage_2, color_2
)
resolution_model_2 = execute_query_phone(
    ctx, df_2, "resolution", model_2, storage_2, color_2
)
ppi_model_2 = execute_query_phone(ctx, df_2, "ppi", model_2, storage_2, color_2)
battery_model_2 = execute_query_phone(ctx, df_2, "battery", model_2, storage_2, color_2)
color_model_2 = execute_query_phone(ctx, df_2, "color", model_2, storage_2, color_2)

fast_charging_model_2 = execute_query_phone(
    ctx, df_2, "fast_charging", model_2, storage_2, color_2
)
induction_model_2 = execute_query_phone(
    ctx, df_2, "induction", model_2, storage_2, color_2
)
usb_type_c_model_2 = execute_query_phone(
    ctx, df_2, "usb_type_c", model_2, storage_2, color_2
)

height_model_2 = execute_query_phone(ctx, df_2, "height", model_2, storage_2, color_2)
width_model_2 = execute_query_phone(ctx, df_2, "width", model_2, storage_2, color_2)
thickness_model_2 = execute_query_phone(
    ctx, df_2, "thickness", model_2, storage_2, color_2
)
net_weight_model_2 = execute_query_phone(
    ctx, df_2, "net_weight", model_2, storage_2, color_2
)

das_head_model_2 = execute_query_phone(
    ctx, df_2, "das_head", model_2, storage_2, color_2
)
das_chest_model_2 = execute_query_phone(
    ctx, df_2, "das_chest", model_2, storage_2, color_2
)
das_limbs_model_2 = execute_query_phone(
    ctx, df_2, "das_limbs", model_2, storage_2, color_2
)

sensor_model_2 = execute_query_phone(ctx, df_2, "sensor", model_2, storage_2, color_2)

cam_1_model_2 = execute_query_phone(ctx, df_2, "cam_1", model_2, storage_2, color_2)

cam_2_model_2 = execute_query_phone(ctx, df_2, "cam_2", model_2, storage_2, color_2)

cam_3_model_2 = execute_query_phone(ctx, df_2, "cam_3", model_2, storage_2, color_2)


##### COMPARATEUR

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Modèle 1️⃣", divider="rainbow")
        col3, col4 = st.columns(2)
        with col3:
            st.metric(
                "Prix", value=f"{price_model_1} €", delta=round(efficiency_model_1, 2)
            )
        with col4:
            st.metric("Position", value="🥇")

        st.image(link_model_1, caption=model_model_1, width=200)
        st.markdown(
            f"""
                - **Marque** : {brand_model_1}
                - **RAM** : {int(ram_model_1)} Go
                - **Stockage** : {int(storage_model_1)} Go
                - **CPU** : {cpu_model_1}
                - **Réseau** : {network_model_1}
                - **Lieu de fabrication** : {flag_model_1} *{made_in_model_1}* 
            """
        )
        st.markdown("#### 📲 Écran")
        st.markdown(
            f"""
                - **Type d'écran** : {screen_type_model_1}
                - **Taille de l'écran** : {screen_size_model_1} pouces ({round(screen_size_model_1*2.54,2)} cm)
                - **Technologie** : {screen_tech_model_1}
                - **Résolution** : {resolution_model_1} pixels
                - **PPI** : {round(ppi_model_1,2)} pixels par pouce
            """
        )
        st.markdown("#### 🔋 Batterie")
        st.markdown(
            f"""
                - **Capacité** : {int(battery_model_1)} mAh
                - **Charge Rapide** : {fast_charging_model_1}
                - **Charge à induction** : {induction_model_1}
                - **USB Type-C** : {usb_type_c_model_1}
            """
        )
        st.markdown("#### 📏 Dimensions")
        st.markdown(
            f"""
                - **Hauteur** : {height_model_1} mm
                - **Largeur** : {width_model_1} mm
                - **Epaisseur** : {thickness_model_1} mm
                - **Poids** : {int(net_weight_model_1)} grammes
            """
        )

        st.markdown("#### 📷 Appareil photo")
        st.markdown(
            f"""
                - **Nombre de capteurs** : {format_sensor(sensor_model_1)}
                - **Résolution** : {resolution_description(sensor_model_1, cam_1_model_1, cam_2_model_1, cam_3_model_1)}
            """
        )

        st.markdown(
            "#### 📡 Débit d'absorption spécifique (DAS)",
            help="Le **DAS** est un indice indiquant la quantité d’énergie électromagnétique absorbée par le corps humain lors de l’utilisation d’un téléphone.",
        )
        st.markdown(
            f"""
                - **DAS Tête** : {das_head_model_1} W/kg
                - **DAS Tronc** : {das_chest_model_1} W/kg
                - **DAS Membres** : {das_limbs_model_1} W/kg
            """
        )
        st.markdown(f"> :rainbow[*Coloris*] : {color_model_1}")
        st.divider()
        col3, col4 = st.columns(2)
        with col3:
            st.markdown(f"{int(reviews_model_1)} personnes ont noté ce téléphone.")
        with col4:
            st.markdown(f"{note_description(reviews_model_1, stars_model_1)}")

with col2:
    with st.container(border=True):
        st.subheader("Modèle 2️⃣", divider="rainbow")
        col3, col4 = st.columns(2)
        with col3:
            st.metric(
                "Prix", value=f"{price_model_2} €", delta=round(efficiency_model_2, 2)
            )
        with col4:
            st.metric("Position", value="🥇")

        st.image(link_model_2, caption=model_model_2, width=200)

        st.markdown(
            f"""
                - **Marque** : {brand_model_2}
                - **RAM** : {int(ram_model_2)} Go
                - **Stockage** : {int(storage_model_2)} Go
                - **CPU** : {cpu_model_2}
                - **Réseau** : {network_model_2}
                - **Lieu de fabrication** : {flag_model_2} *{made_in_model_2}* 
            """
        )
        st.markdown("#### 📲 Écran")
        st.markdown(
            f"""
                - **Type d'écran** : {screen_type_model_2}
                - **Taille de l'écran** : {screen_size_model_2} pouces ({round(screen_size_model_2*2.54,2)} cm)
                - **Technologie** : {screen_tech_model_2}
                - **Résolution** : {resolution_model_2} pixels
                - **PPI** : {round(ppi_model_2,2)} pixels par pouce
            """
        )
        st.markdown("#### 🔋 Batterie")
        st.markdown(
            f"""
                - **Capacité** : {int(battery_model_2)} mAh
                - **Charge Rapide** : {fast_charging_model_2}
                - **Charge à induction** : {induction_model_2}
                - **USB Type-C** : {usb_type_c_model_2}
            """
        )
        st.markdown("#### 📏 Dimensions")
        st.markdown(
            f"""
                - **Hauteur** : {height_model_2} mm
                - **Largeur** : {width_model_2} mm
                - **Epaisseur** : {thickness_model_2} mm
                - **Poids** : {int(net_weight_model_2)} grammes
            """
        )

        st.markdown("#### 📷 Appareil photo")
        st.markdown(
            f"""
                - **Nombre de capteurs** : {format_sensor(sensor_model_2)}
                - **Résolution** : {resolution_description(sensor_model_2, cam_1_model_2, cam_2_model_2, cam_3_model_2)}
            """
        )

        st.markdown(
            "#### 📡 Débit d'absorption spécifique (DAS)",
            help="Le **DAS** est un indice indiquant la quantité d’énergie électromagnétique absorbée par le corps humain lors de l’utilisation d’un téléphone.",
        )
        st.markdown(
            f"""
                - **DAS Tête** : {das_head_model_2} W/kg
                - **DAS Tronc** : {das_chest_model_2} W/kg
                - **DAS Membres** : {das_limbs_model_2} W/kg
            """
        )
        st.markdown(f"> :rainbow[*Coloris*] : {color_model_2}")
        st.divider()
        col3, col4 = st.columns(2)
        with col3:
            st.markdown(f"{int(reviews_model_2)} personnes ont noté ce téléphone.")
        with col4:
            st.markdown(f"{note_description(reviews_model_2, stars_model_2)}")


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
