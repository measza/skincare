import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="KYMIRA - Wujudkan Kulit Impian", layout="wide")

# --- Sidebar Navigasi (resmi Streamlit multi-page) ---
st.sidebar.page_link("home.py", label="🏠 Beranda")
st.sidebar.page_link("pages/2_produk.py", label="🧴 Produk")
st.sidebar.page_link("pages/1_rekomendasi.py", label="✨ Rekomendasi Skincare")

# --- Fungsi Konversi Gambar ke Base64 ---
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- Gambar Banner ---
banner_base64 = image_to_base64("assets/banner.jpg")

# --- Gambar Slider ---
if "image_index" not in st.session_state:
    st.session_state.image_index = 1

image_paths = [
    "assets/g1.jpg",
    "assets/g2.jpg",
    "assets/g3.jpg",
    "assets/g5.jpg",
    "assets/g6.jpg"
]

# --- Styling CSS ---
st.markdown("""
<style>
    html, body, .stApp {
        margin: 0;
        padding: 0;
        background-color: #ffe6f0;
        font-family: "Arial", sans-serif;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #ffccdd;
        padding: 1rem 2rem;
        border-bottom: 3px solid #e68aa5;
    }

    .navbar-left button {
        background-color: #ff80aa;
        color: white;
        border: none;
        padding: 6px 18px;
        font-size: 13px;
        border-radius: 20px;
        font-weight: 600;
    }

    .navbar-center {
        font-size: 26px;
        font-weight: 900;
        color: #b30059;
    }

    .stButton > button {
        background-color: #ff4080;
        color: white;
        padding: 10px 24px;
        font-size: 15px;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #e6005c;
    }
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown('<div class="navbar-left"><button disabled>Utama</button></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="navbar-center">KYMIRA</div>', unsafe_allow_html=True)

with col3:
    if st.button("🧴 Produk", help="Lihat semua produk", use_container_width=True):
        st.switch_page("pages/2_produk.py")  # Navigasi langsung ke halaman Produk

# --- Banner ---
st.markdown(f"""
<div style='position: relative; margin-top: 1rem;'>
    <img src="data:image/png;base64,{banner_base64}" style="width:100%; border-radius:8px;">
    <div style='position:absolute; top:50%; left:5%; transform:translateY(-50%);
                color:#99004d; font-size:34px; font-weight:900; background:rgba(255,230,240,0.6);
                padding:10px 20px; border-radius:10px;'>
        WUJUDKAN KULIT<br>IMPIAN DENGAN<br>PRODUK KAMI
    </div>
</div>
""", unsafe_allow_html=True)

# --- Teks Promo ---
st.markdown("""
<div style='text-align:center; color:#b30059; font-size:16px; margin-top:2rem;'>
    Perawatan harian yang membantu untuk menyamarkan tanda-tanda<br>
    penuaan pada kulit wajah serta memperbaiki tekstur kulit.<br><br>
</div>
""", unsafe_allow_html=True)

# --- Image Slider ---
center = st.session_state.image_index
left = (center - 1) % len(image_paths)
right = (center + 1) % len(image_paths)

c1, c2, c3, c4, c5 = st.columns([1, 2.5, 3, 2.5, 1])
with c1:
    if st.button("←"):
        st.session_state.image_index = (st.session_state.image_index - 1) % len(image_paths)
with c2:
    st.image(image_paths[left], width=140)
with c3:
    st.image(image_paths[center], width=220)
with c4:
    st.image(image_paths[right], width=140)
with c5:
    if st.button("→"):
        st.session_state.image_index = (st.session_state.image_index + 1) % len(image_paths)

# --- CTA Button ke Rekomendasi (Menggunakan switch_page) ---
st.markdown("<br>", unsafe_allow_html=True)
col_center = st.columns([1, 1, 1])[1]  # Kolom tengah dari 3

with col_center:
    if st.button("✨ find your best skincare!"):
        st.switch_page("pages/1_rekomendasi.py")
