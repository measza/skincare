import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Navigasi ---
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.page_link("app.py", label="🏠 Home", icon="🏡")
with col2:
    st.title("🔍 Rekomendasi Produk Skincare")
with col3:
    st.page_link("pages/2_produk.py", label="📦 Produk", icon="📦")

# --- Styling background ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Load dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv("cosmetic_p.csv")
    df.columns = df.columns.str.lower().str.strip()
    df["ingredients"] = df["ingredients"].str.lower()
    return df

data = load_data()

# --- Aturan sistem pakar ---
rules = {
    "Mencerahkan Wajah": ["niacinamide", "vitamin c", "alpha arbutin"],
    "Mengurangi Jerawat": ["salicylic acid", "benzoyl peroxide", "tea tree", "azelaic acid", "sulfur"],
    "Anti Aging": ["retinol", "peptide", "coenzyme q10",]()
