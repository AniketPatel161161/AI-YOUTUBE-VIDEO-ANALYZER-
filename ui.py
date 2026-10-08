import streamlit as st
from youtube_analyzer import build_youtube_agent
import streamlit as st

st.set_page_config(
    page_title="YouTube AI Agent",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

/* =========================
   MAIN BACKGROUND
========================= */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 0, 80, 0.18), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(120, 50, 255, 0.20), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(0, 180, 255, 0.12), transparent 35%),
        linear-gradient(135deg, #050816 0%, #0b1026 45%, #12091f 100%);
    color: white;
}

/* Remove default top spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}


/* =========================
   HERO TITLE
========================= */

.hero {
    text-align: center;
    padding: 35px 20px 30px 20px;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 10px;

    background: linear-gradient(
        90deg,
        #ff1744,
        #ff4d8d,
        #9c6cff,
        #4facfe
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 18px;
    color: #b8b9d1;
    margin-bottom: 10px;
}


/* =========================
   GLASS CARD
========================= */

.glass-card {
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 28px;
    margin: 20px 0;

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    box-shadow:
        0 8px 32px rgba(0, 0, 0, 0.35),
        inset 0 1px rgba(255,255,255,0.05);
}


/* =========================
   INPUT BOX
========================= */

.stTextInput > div > div > input {
    background: rgba(255,255,255,0.07) !important;
    color: white !important;

    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 14px !important;

    padding: 15px !important;
    font-size: 16px !important;
}

.stTextInput > div > div > input:focus {
    border: 1px solid #ff3d71 !important;

    box-shadow:
        0 0 0 2px rgba(255,61,113,0.15),
        0 0 20px rgba(255,61,113,0.15) !important;
}


/* =========================
   BUTTON
========================= */

.stButton > button {
    width: 100%;

    background: linear-gradient(
        90deg,
        #ff1744,
        #ff4081
    ) !important;

    color: white !important;

    border: none !important;
    border-radius: 14px !important;

    padding: 14px 20px !important;

    font-size: 17px !important;
    font-weight: 700 !important;

    box-shadow:
        0 8px 25px rgba(255, 23, 68, 0.30);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);

    box-shadow:
        0 12px 35px rgba(255, 23, 68, 0.45);
}


/* =========================
   HEADINGS
========================= */

h1, h2, h3 {
    color: white !important;
}

h2 {
    font-size: 28px !important;
}

h3 {
    color: #ff5c8a !important;
}


/* =========================
   NORMAL TEXT
========================= */

p {
    color: #c7c9df !important;
}


/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #080a18,
            #100b20
        ) !important;

    border-right: 1px solid rgba(255,255,255,0.08);
}


/* =========================
   EXPANDERS
========================= */

.streamlit-expanderHeader {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 12px !important;
    color: white !important;
}


/* =========================
   ALERT BOXES
========================= */

[data-testid="stAlert"] {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.1);
}


/* =========================
   SCROLLBAR
========================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #070914;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(
        #ff1744,
        #8b5cf6
    );

    border-radius: 10px;
}


/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;
    color: #777a96;
    margin-top: 50px;
    padding: 20px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

# input box
video_url = st.text_input("Enter Youtube Video Link") # str
button = st.button("Analyze Video") # True/False

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)