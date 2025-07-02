import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Rekomendasi")
st.title("🔍 Rekomendasi Produk")

st.markdown("""
<div style="display:flex; gap:30px; margin-bottom:20px;">
  <a href="../" style="font-weight:bold;">🏠 Home</a>
  <a href="2_produk" style="font-weight:bold;">📦 Produk</a>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_csv():
    return pd.read_csv("../cosmetic_p.csv")

df = load_csv()
df.columns = df.columns.str.lower()
df["ingredients"] = df["ingredients"].fillna("").str.lower()

rules = {
    "Mencerahkan Wajah": ["niacinamide", "vitamin c", "alpha arbutin"],
    "Mengurangi Jerawat": ["salicylic acid", "benzoyl peroxide", "tea tree"],
    "Anti Aging": ["retinol", "peptide"],
    "Melembapkan Kulit": ["hyaluronic acid", "ceramide", "glycerin"],
}

tujuan = st.selectbox("Tujuan", list(rules.keys()))
jproduk = st.selectbox("Jenis Produk", df["label"].unique())
jk = st.multiselect("Jenis Kulit", ["normal","dry","oily","combination","sensitive"])
bobot = st.slider("Bobot Bahan vs Rating", 0.0, 1.0, 0.7)

if st.button("Cari"):
    subset = df[df["label"].str.lower()==jproduk.lower()].copy()
    news = subset[subset["ingredients"].apply(lambda t: any(k in t for k in rules[tujuan]))]
    for s in jk:
        news = news[news[s]==1]
    if news.empty:
        st.warning("Tidak ada produk cocok.")
    else:
        tfidf = TfidfVectorizer()
        M = tfidf.fit_transform(news["ingredients"])
        vec = tfidf.transform([" ".join(rules[tujuan])])
        sim = cosine_similarity(vec, M).flatten()
        news["score"] = bobot * sim + (1-bobot)*(news["rank"]/5)
        news = news.sort_values("score", ascending=False)
        for _, r in news.iterrows():
            st.subheader(f"{r['name']} ({r['brand']})")
            st.write(f"Harga: ${r['price']} | Rating: {r['rank']}")
            st.write(f"Ingredients: {r['ingredients'][:200]}...")
            st.markdown("---")
