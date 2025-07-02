import streamlit as st
import base64

st.set_page_config(page_title="KYMIRA - Skincare", layout="wide")

def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

hero_img = get_image_as_base64("assets/banner.jpg")

st.markdown(f"""
    <style>
    .hero {{
        background-image: url("data:image/jpeg;base64,{hero_img}");
        height: 350px;
        background-size: cover;
        background-position: center;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-shadow: 2px 2px 4px #000;
        font-size: 2.5em;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero">WUJUDKAN KULIT IMPIAN DENGAN PRODUK KAMI</div>', unsafe_allow_html=True)
st.markdown("Perawatan harian yang membantu menyamarkan tanda penuaan serta memperbaiki tekstur kulit.")

st.page_link("pages/1_rekomendasi.py", label="✨ Find your best skincare", icon="🔍")
st.page_link("pages/2_produk.py", label="📦 Lihat Semua Produk", icon="📦")
