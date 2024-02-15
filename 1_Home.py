import streamlit as st


def page_config() -> None:
    """`page_config`: Configure le titre et le favicon de l'application.

    `Example(s)`
    ---------
    >>> page_config()
    ... None"""
    return st.set_page_config(page_title="Phone Finder", page_icon="📱")


page_config()
st.title("APP")

st.markdown('<a href="Data#telephone" target="_self">Test</a>', unsafe_allow_html=True)

st.markdown('<a href="Détails" target="_self">Détails</a>', unsafe_allow_html=True)
