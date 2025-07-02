import streamlit as st
import base64

# Page config
st.set_page_config(
    page_title="KYMIRA - Wujudkan Kulit Impian",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load gambar
def get_image_as_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Gambar
hero_bg = get_image_as_base64("assets/banner.jpg")
gallery_imgs = [
    get_image_as_base64("assets/g1.jpg"),
    get_image_as_base64("assets/g2.jpg"),
    get_image_as_base64("assets/g3.jpg"),
    get_image_as_base64("assets/g4.jpg"),
    get_image_as_base64("assets/g5.jpg"),
]

# CSS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #ffe6f0;
        font-family: 'Poppins', sans-serif;
    }}
    header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 50px;
        background-color: #ff99cc;
        color: white;
        font-weight: 600;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .nav-button {{
        background-color: #ff66b2;
        color: white !important;
        padding: 8px 20px;
        border-radius: 20px;
        text-decoration: none;
        margin: 0 10px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }}
    .nav-button:hover {{
        background-color: #e04a99;
    }}
    .logo {{
        font-size: 2.2em;
        font-weight: 700;
        color: white;
    }}
    .hero-section {{
        background-image: url("data:image/png;base64,{hero_bg}");
        background-size: cover;
        background-position: center;
        height: 400px;
        display: flex;
        align-items: center;
        padding-left: 10%;
        color: white;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.6);
    }}
    .hero-section h1 {{
        font-size: 3.5em;
        max-width: 600px;
        line-height: 1.2;
    }}
    .intro-text-section {{
        text-align: center;
        padding: 30px 15%;
        font-size: 1.2em;
        color: #555;
        line-height: 1.6;
    }}
    .carousel-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
        padding: 20px 0;
    }}
    .carousel-item {{
        flex: 0 0 auto;
        width: 200px;
        height: 200px;
        margin: 0 15px;
        scroll-snap-align: center;
        transition: transform 0.3s ease;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }}
    .carousel-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}
    .carousel-item:focus, .carousel-item:target {{
        transform: scale(1.2);
    }}
    .find-skincare-button {{
        background-color: #ff66b2;
        color: white;
        border: none;
        padding: 14px 30px;
        border-radius: 30px;
        font-size: 1.1em;
        cursor: pointer;
        font-weight: 600;
        margin-top: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }}
    .find-skincare-button:hover {{
        background-color: #e04a99;
        transform: scale(1.05);
    }}
    </style>
""", unsafe_allow_html=True)

# --- Navbar ---
st.markdown("""
    <div class="navbar">
        <div class="nav-left">
            <a href="/" class="nav-button">Home</a>
        </div>
        <div class="logo">KYMIRA</div>
        <div class="nav-right">
            <a href="/2_produk" class="nav-button">Products</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class="hero-section">
        <h1>WUJUDKAN KULIT IMPIAN DENGAN PRODUK KAMI</h1>
    </div>
""", unsafe_allow_html=True)

# --- Intro Text ---
st.markdown("""
    <div class="intro-text-section">
        <p>Perawatan harian yang membantu untuk menyamarkan tanda-tanda penuaan pada kulit wajah serta memperbaiki tekstur kulit.</p>
    </div>
""", unsafe_allow_html=True)

# --- Carousel ---
st.markdown('<div class="carousel-container">', unsafe_allow_html=True)
for img in gallery_imgs:
    st.markdown(f"""
        <div class="carousel-item">
            <img src="data:image/png;base64,{img}" />
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Button: Go to Recommendation ---
if st.button("find your best skincare!", key="go_to_recommendation", help="Klik untuk rekomendasi produk"):
    st.switch_page("pages/1_rekomendasi.py")
