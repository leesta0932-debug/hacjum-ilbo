from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="학점일보 근거 자료", page_icon="📰", layout="centered")

# Streamlit 기본 여백·메뉴 숨기기
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 0.5rem; padding-bottom: 0; max-width: 760px;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("page.html").read_text(encoding="utf-8")
components.html(html, height=1900, scrolling=True)
