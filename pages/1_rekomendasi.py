import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Rekomendasi Skincare")
st.title("🔍 Rekomendasi Produk Skincare")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("cosmetic_p.csv")
    df.columns = df.columns.str.lower()
    df["ingredients"] = df["ingredients"].fillna("").str.lower()
    return df

df = load_data()

# Aturan Rule-Based
rules = {
    "Mencerahkan Wajah": ["niacinamide", "vitamin c", "alpha arbutin"],
    "Mengurangi Jerawat": ["salicylic acid", "benzoyl peroxide", "tea tree"],
    "Anti Aging": ["retinol", "peptide", "coenzyme q10"],
    "Melembapkan Kulit": ["hyaluronic acid", "ceramide", "glycerin"],
}

# Input dari pengguna
tujuan = st.selectbox("Tujuan Skincare", list(rules.keys()))
jenis_produk = st.selectbox("Jenis Produk", df["label"].unique())
jenis_kulit = st.multiselect("Jenis Kulit", ["combination", "dry", "normal", "oily", "sensitive"])
bobot_bahan = st.slider("Bobot Ingredient vs Rating", 0.0, 1.0, 0.7)

# Proses Rekomendasi
if st.button("🔎 Tampilkan Rekomendasi"):
    keywords = rules[tujuan]
    data = df[df["label"].str.lower() == jenis_produk.lower()].copy()

    # Filter berdasarkan keyword
    def cocok(text):
        return any(k in text for k in keywords)

    data = data[data["ingredients"].apply(cocok)]

    # Filter jenis kulit
    for jk in jenis_kulit:
        data = data[data[jk] == 1]

    if data.empty:
        st.warning("Tidak ditemukan produk yang cocok.")
    else:
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(data["ingredients"])
        query = tfidf.transform([" ".join(keywords)])
        similarity = cosine_similarity(query, tfidf_matrix).flatten()
        data["similarity"] = similarity
        data["score"] = bobot_bahan * data["similarity"] + (1 - bobot_bahan) * (data["rank"] / 5)
        data = data.sort_values("score", ascending=False)

        for _, row in data.iterrows():
            st.subheader(f"{row['name']} ({row['brand']})")
            st.write(f"Harga: ${row['price']} | Rating: {row['rank']}")
            st.write(f"Ingredients: {row['ingredients'][:250]}...")
            st.markdown("---")
