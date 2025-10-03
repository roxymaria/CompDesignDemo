
import streamlit as st
import base64

def img_tag(path: str, alt: str = "") -> str:
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return (
        f'<img alt="{alt}" loading="lazy" '
        f'style="width:100%;height:auto;border-radius:8px;display:block;" '
        f'src="data:image/png;base64,{b64}"/>'
    )

DOE_URL  = "https://doe-4853.streamlit.app/"
META_URL = "https://metamodels-4853.streamlit.app/"
DOE_IMG  = "assets/day1.png"
META_IMG = "assets/day2.png"

st.set_page_config(page_title="Computational Design", layout="wide")
st.title("Computational Design")
st.caption("Examples for ME 4853 / ID 4850 / MGMT 4853")

def render_card(col, title, button_cap, url, img_path, img_cap):
    with col:
        box = st.container(border=True)
        with box:
            st.subheader(title)
            st.link_button(f"Open {button_cap}", url, use_container_width=True)
            st.markdown(img_tag(img_path, alt=title), unsafe_allow_html=True)
            st.caption(img_cap)

c1, c2 = st.columns(2, gap="large")
render_card(c1, "Day 1: Design of Experiments", "DOE Playground", DOE_URL, DOE_IMG, "doe")
render_card(c2, "Day 2: Metamodeling", "Metamodel Playground", META_URL, META_IMG, "meta")
