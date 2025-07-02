import streamlit as st
import pandas as pd

# --- Judul Halaman ---
st.title("📦 Daftar Produk Skincare")

# --- Load Dataset ---
@st.cache_data
def load_data():
    return pd.read_csv("cosmetic_p.csv")

df = load_data()

# --- Sidebar Filter ---
with st.sidebar:
    st.header("🔍 Filter Produk")

    search_query = st.text_input("Cari nama atau bahan...", "")

    skin_types = ["Normal", "Dry", "Oily", "Combination", "Sensitive"]
    selected_skin = st.multiselect("Jenis Kulit", skin_types)

# --- Filter Berdasarkan Input User ---
filtered_df = df.copy()

# Filter by search
if search_query:
    filtered_df = filtered_df[
        df["name"].str.contains(search_query, case=False, na=False) |
        df["ingredients"].str.contains(search_query, case=False, na=False)
    ]

# Filter by skin type (binary flags in columns)
if selected_skin:
    for skin in selected_skin:
        filtered_df = filtered_df[filtered_df[skin] == 1]

# --- Tampilkan Produk ---
st.write(f"Menampilkan **{len(filtered_df)}** produk yang sesuai.")

for index, row in filtered_df.iterrows():
    with st.container():
        st.markdown(f"""
        <div style="background-color: #fff0f5; padding: 15px; border-radius: 15px; margin-bottom: 15px;">
            <h4 style="margin-bottom: 5px;">{row['name']} <span style='color:gray;'>({row['brand']})</span></h4>
            <p><strong>Harga:</strong> ${row['price']} | <strong>Rating:</strong> {row['rank']}</p>
            <p><strong>Ingredients:</strong> {row['ingredients']}</p>
        </div>
        """, unsafe_allow_html=True)
