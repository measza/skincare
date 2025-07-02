import streamlit as st
import pandas as pd

st.set_page_config(page_title="Daftar Produk", layout="wide")
st.title("📦 Produk Skincare")

# Navigasi manual
st.markdown("""
<div style="display:flex; gap:30px; margin-bottom:20px;">
  <a href="../" style="font-weight:bold;">🏠 Home</a>
  <a href="1_rekomendasi" style="font-weight:bold;">🔍 Rekomendasi</a>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_csv():
    return pd.read_csv("../cosmetic_p.csv")  # note: ../ to go back to root

df = load_csv()
df.columns = df.columns.str.lower()

# Sidebar filter
with st.sidebar:
    st.header("Filter Produk")
    q = st.text_input("Nama / Bahan aktif")
    types = ["normal","dry","oily","combination","sensitive"]
    sel = st.multiselect("Jenis Kulit", types)

filtered = df.copy()
if q:
    filtered = filtered[
        filtered["name"].str.contains(q, case=False, na=False) |
        filtered["ingredients"].str.contains(q, case=False, na=False)
    ]
if sel:
    for s in sel:
        filtered = filtered[filtered[s] == 1]

st.write(f"Menampilkan **{len(filtered)}** produk")

for _, r in filtered.iterrows():
    st.markdown(f"""
    <div style="background:#fff0f5; padding:12px; border-radius:15px; margin-bottom:15px;">
      <h4>{r['name']} <span style="color:gray;">({r['brand']})</span></h4>
      <p>Harga: ${r['price']} | Rating: {r['rank']}</p>
      <p><strong>Ingredients:</strong> {r['ingredients'][:200]}...</p>
    </div>
    """, unsafe_allow_html=True)
