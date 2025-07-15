import streamlit as st
import pandas as pd

# --- Load Data ---
df = pd.read_csv("cosmetic_p.csv")

# --- Page Configuration ---
st.set_page_config(page_title="Produk - KYMIRA", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        html, body, .main, .stApp {
            background-color: #ffe6f0 !important;
            font-family: "Arial", sans-serif;
        }

        .block-container {
            padding: 2rem 4rem;
        }

        .title {
            text-align: center;
            font-size: 28px;
            color: #b30059;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }

        .button-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2rem;
        }

        .stButton>button {
            background-color: #ff80aa;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: 500;
            font-size: 14px;
        }

        .stButton>button:hover {
            background-color: #f7bcd4;
        }

        .product-card {
            background-color: white;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            margin-bottom: 1.2rem;
        }

        .product-title {
            font-size: 16px;
            color: #b30059;
            font-weight: bold;
        }

        .product-brand {
            font-size: 14px;
            color: #555;
        }

        .product-price {
            font-size: 14px;
            color: #800040;
        }

        .product-ingredients {
            font-size: 13px;
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)

# --- Navbar Navigasi Atas (Home kiri, Rekomendasi kanan) ---
st.markdown("""
    <style>
    .top-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem 0 2rem;
    }

    .top-navbar .stButton > button {
        background-color: #ff80aa;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: 500;
        font-size: 14px;
        transition: background-color 0.3s;
    }

    .top-navbar .stButton > button:hover {
        background-color: #f7bcd4;
    }
    </style>

    <div class="top-navbar">
        <div id="nav-home"></div>
        <div id="nav-rekom"></div>
    </div>
""", unsafe_allow_html=True)

# Render tombol di posisi yang diatur oleh HTML/CSS
col1, col2, col3 = st.columns([2, 8, 4])

with col1:
    if st.button("← 🏠", key="btn_home"):
        st.switch_page("home.py")

with col3:
    if st.button("✨ Rekomendasi Skincare →", key="btn_rekom"):
        st.switch_page("pages/1_rekomendasi.py")



# --- Title ---
st.markdown('<div class="title">Daftar Produk Skincare</div>', unsafe_allow_html=True)

# --- Display Product List ---
for index, row in df.iterrows():
    st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{row['name']}</div>
            <div class="product-brand">{row['brand']}</div>
            <div class="product-price">Rp {row['price']} | ⭐ {row['rank']}</div>
            <div class="product-ingredients"><b>Ingredients:</b> {row['ingredients']}</div>
        </div>
    """, unsafe_allow_html=True)
