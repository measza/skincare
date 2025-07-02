import streamlit as st
import pandas as pd

st.set_page_config(page_title="📦 Daftar Produk Skincare", layout="wide")
st.title("📦 Daftar Produk Skincare")

# Navigasi (tanpa st.page_link agar aman)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown("[🏠 Home](../)")
with col2:
    st.page_link("pages/1_rekomendasi.py", label="🔍 Ke Rekomendasi", icon="✨")
with col3:
    st.markdown("📄 Halaman Ini")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("cosmetic_p.csv")
    df.columns = df.columns.str.lower()
    return df

df = load_data()

# Sidebar filter
with st.sidebar:
    st.header("🔍 Filter Produk")

    search_query = st.text_input("Cari nama produk atau bahan aktif...", "")
    skin_types = ["normal", "dry", "oily", "combination", "sensitive"]
    selected_skin = st.multiselect("Jenis Kulit", skin_types)

# Filter logic
filtered_df = df.copy()

if search_query:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(search_query, case=False, na=False) |
        filtered_df["ingredients"].str.contains(search_query, case=False, na=False)
    ]

if selected_skin:
    for skin in selected_skin:
        if skin in filtered_df.columns:
            filtered_df = filtered_df[filtered_df[skin] == 1]

st.write(f"Menampilkan **{len(filtered_df)}** produk yang sesuai.")

for index, row in filtered_df.iterrows():
    with st.container():
        st.markdown(f"""
        <div style="background-color: #fff0f5; padding: 15px; border-radius: 15px; margin-bottom: 15px;">
            <h4 style="margin-bottom: 5px;">{row['name']} <span style='color:gray;'>({row['brand']})</span></h4>
            <p><strong>Harga:</strong> ${row['price']} | <strong>Rating:</strong> {row['rank']}</p>
            <p><strong>Ingredients:</strong> {row['ingredients'][:300]}...</p>
        </div>
        """, unsafe_allow_html=True)
