import streamlit as st
import base64

st.set_page_config(page_title="KYMIRA", layout="wide")

def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner = get_image_base64("assets/banner.jpg")

st.markdown(f"""
<div style="
    background-image: url('data:image/jpeg;base64,{banner}');
    background-size: cover; background-position: center;
    height: 350px; border-radius:15px;
    display:flex; align-items:center; justify-content:center;
    color:white; font-size:2.5em; font-weight:bold;
">
WUJUDKAN KULIT IMPIAN
</div>
""", unsafe_allow_html=True)

st.write("Perawatan harian, rekomendasi mudah.")

st.markdown("""
<div style="text-align:center; margin-top:30px;">
    <a href="pages/2_produk" style="padding:12px 25px; background:#ff66b2;
       color:white; border-radius:30px; text-decoration:none; font-weight:bold;">
        📦 Lihat Produk
    </a>
    &nbsp;&nbsp;
    <a href="pages/1_rekomendasi" style="padding:12px 25px; background:#ff66b2;
       color:white; border-radius:30px; text-decoration:none; font-weight:bold;">
        🔍 Rekomendasi
    </a>
</div>
""", unsafe_allow_html=True)
