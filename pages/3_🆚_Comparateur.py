import streamlit as st
from modules_app.data_import import *


df = load_df()

ctx = pl.SQLContext()

link = (
    ctx.register("df", df)
    .execute("SELECT image FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' ")
    .collect()
    .item()
)

model = (
    ctx.register("df", df)
    .execute("SELECT model FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' ")
    .collect()
    .item()
)

ram = (
    ctx.register("df", df)
    .execute("SELECT ram FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' ")
    .collect()
    .item()
)

brand = (
    ctx.register("df", df)
    .execute("SELECT brand FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' ")
    .collect()
    .item()
)

storage = (
    ctx.register("df", df)
    .execute(
        "SELECT storage FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' "
    )
    .collect()
    .item()
)

flag = (
    ctx.register("df", df)
    .execute("SELECT flag FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' ")
    .collect()
    .item()
)

made_in = (
    ctx.register("df", df)
    .execute(
        "SELECT made_in FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' "
    )
    .collect()
    .item()
)

reviews = (
    ctx.register("df", df)
    .execute(
        "SELECT reviews FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' "
    )
    .collect()
    .item()
)

stars = (
    ctx.register("df", df)
    .execute("SELECT stars FROM df WHERE model = 'iPhone 14 Plus' AND color = 'Jaune' ")
    .collect()
    .item()
)

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.image(link, caption=model, width=200)
        st.markdown(f"- **Marque** : {brand}")
    with col2:
        st.markdown(
            f"""
                    - **RAM** : {ram} Go
                    - **Stockage** : {storage} Go
                    - **Lieu de fabrication** : *{made_in}* {flag} 
                    """
        )
    st.divider()
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"{int(reviews)} personnes ont noté ce téléphone.")
    with col4:
        st.markdown(f"⭐ {round(stars,1)}")
