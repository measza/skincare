import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🔍 Rekomendasi Produk Skincare")

@st.cache_data
def load_data():
    df = pd.read_csv("cosmetic_p.csv")
    df.columns = df.columns.str.lower().str.strip()
    df["ingredients"] = df["ingredients"].str.lower()
    return df

data = load_data()

rules = {
    "Mencerahkan Wajah": ["niacinamide", "vitamin c", "alpha arbutin"],
    "Mengurangi Jerawat": ["salicylic acid", "benzoyl peroxide", "tea tree"],
    "Anti Aging": ["retinol", "peptide", "coenzyme q10"],
    "Melembapkan Kulit": ["hyaluronic acid", "ceramide", "glycerin"],
}

kebutuhan = st.selectbox("🎯 Tujuan skincare:", list(rules.keys()))
produk_type = st.selectbox("🧴 Jenis produk:", data["label"].unique())

jenis_kulit = st.multiselect("💧 Jenis Kulit:", ["combination", "dry", "normal", "oily", "sensitive"])
sim_weight = st.slider("⚖️ Prioritas bahan vs rating", 0.0, 1.0, 0.7)
rating_weight = 1.0 - sim_weight

if st.button("Tampilkan Rekomendasi"):
    keywords = rules[kebutuhan]
    produk_subset = data[data["label"].str.lower() == produk_type.lower()]

    def contains_keywords(text):
        return any(kw in text for kw in keywords)

    filtered = produk_subset[produk_subset["ingredients"].apply(contains_keywords)]

    if filtered.empty:
        st.warning("Tidak ditemukan produk dengan bahan tersebut.")
        return

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(filtered["ingredients"])
    query_vec = tfidf.transform([" ".join(keywords)])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    filtered["similarity"] = similarities

    for skin in jenis_kulit:
        filtered = filtered[filtered[skin] == 1]

    filtered["score"] = sim_weight * filtered["similarity"] + rating_weight * (filtered["rank"] / 5)
    result = filtered.sort_values("score", ascending=False)

    for _, row in result.iterrows():
        st.markdown(f"### {row['name']} ({row['brand']})")
        st.write(f"Harga: ${row['price']} | Rating: {row['rank']}")
        st.write(f"Ingredients: {row['ingredients'][:250]}...")
        st.markdown("---")
