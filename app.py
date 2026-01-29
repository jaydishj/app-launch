import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Leaf X-Ray | AI Plant Diagnostics",
    page_icon="🌿",
    layout="centered"
)

# ================= LOTTIE LOADER =================
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None

launch_anim = load_lottie("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
success_anim = load_lottie("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")

# ================= ANIMATED GREEN BACKGROUND =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #0b3d0b, #1b5e20, #2e7d32, #66bb6a);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.leaf {
    position: fixed;
    top: -10%;
    width: 40px;
    opacity: 0.25;
    animation: fall linear infinite;
    z-index: 0;
}

@keyframes fall {
    0% { transform: translateX(0) rotate(0deg); top: -10%; }
    100% { transform: translateX(140px) rotate(360deg); top: 110%; }
}

.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: #e8f5e9;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    color: #c8e6c9;
}

.info {
    font-size: 18px;
    text-align: center;
    color: #e8f5e9;
}

.launch-text {
    font-size: 26px;
    text-align: center;
    color: #ffffff;
    font-weight: bold;
}

.block-container {
    position: relative;
    z-index: 1;
}
</style>
""", unsafe_allow_html=True)

# ================= FLOATING LEAVES =================
st.markdown("""
<img class="leaf" src="https://pngimg.com/uploads/leaf/leaf_PNG3681.png" style="left:8%; animation-duration:20s;">
<img class="leaf" src="https://pngimg.com/uploads/leaf/leaf_PNG3686.png" style="left:35%; animation-duration:26s;">
<img class="leaf" src="https://pngimg.com/uploads/leaf/leaf_PNG3693.png" style="left:65%; animation-duration:22s;">
<img class="leaf" src="https://pngimg.com/uploads/leaf/leaf_PNG3701.png" style="left:85%; animation-duration:30s;">
""", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "launch" not in st.session_state:
    st.session_state.launch = False

# ================= INTRO SCREEN =================
if not st.session_state.launch:
    st.markdown('<div class="title">🌿 Leaf X-Ray</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">AI-Assisted Digital Reconstruction of Leaf Anatomy</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="info">
    🔬 AI-powered leaf anatomy visualization<br>
    🌱 No physical cross-sectioning required<br>
    🧠 Designed for students, researchers & educators<br>
    🌍 Digital & sustainable plant science learning
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # -------- CENTERED BUTTON --------
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Launch Leaf X-Ray", use_container_width=True):
            st.session_state.launch = True
            st.rerun()

# ================= LAUNCH SEQUENCE =================
else:
    st.markdown('<div class="launch-text">Launching Leaf X-Ray...</div>', unsafe_allow_html=True)

    if launch_anim is not None:
        st_lottie(launch_anim, height=300)

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.08)  # ~8 seconds
        progress.progress(i + 1)

    # ================= SUCCESS SCREEN =================
    st.markdown('<div class="launch-text">✅ Successfully Launched!</div>', unsafe_allow_html=True)

    if success_anim is not None:
        st_lottie(success_anim, height=250)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= VIEW APP BUTTON =================
    st.markdown("""
    <div style="text-align:center;">
        <a href="https://your-official-website.com" target="_blank">
            <button style="
                background-color:#2E7D32;
                color:white;
                padding:14px 32px;
                font-size:18px;
                border:none;
                border-radius:14px;
                cursor:pointer;
            ">
                🌿 View Leaf X-Ray App
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
