import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Leaf X-Ray | AI Plant Diagnostics",
    page_icon="🌿",
    layout="centered"
)

# ------------------ Lottie Loader ------------------
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

launch_anim = load_lottie("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
success_anim = load_lottie("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")

# ------------------ Styling ------------------
st.markdown("""
<style>
.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: #2E7D32;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: #555;
}
.info {
    font-size: 18px;
    text-align: center;
}
.launch-text {
    font-size: 26px;
    text-align: center;
    color: #1B5E20;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "launch" not in st.session_state:
    st.session_state.launch = False

# ------------------ Intro Page ------------------
if not st.session_state.launch:
    st.markdown('<div class="title">🌿 Leaf X-Ray</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-Powered Leaf Health & Disease Diagnosis</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="info">
    🔬 Uses advanced AI & computer vision<br>
    🌱 Detects plant diseases from leaf images<br>
    🧠 Supports farmers, researchers & agronomists<br>
    🌍 Promotes sustainable agriculture
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("🚀 Launch Leaf X-Ray"):
        st.session_state.launch = True
        st.rerun()

# ------------------ Launch Animation ------------------
else:
    st.markdown('<div class="launch-text">Launching Leaf X-Ray...</div>', unsafe_allow_html=True)

    if launch_anim is not None:
        st_lottie(launch_anim, height=300)

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.08)  # ~8 seconds
        progress.progress(i + 1)

    # ------------------ Success Screen ------------------
    st.markdown('<div class="launch-text">✅ Successfully Launched!</div>', unsafe_allow_html=True)

    if success_anim is not None:
        st_lottie(success_anim, height=250)

    st.markdown("<br>", unsafe_allow_html=True)

    # View Leaf X-Ray App Button
    st.markdown(
        """
        <div style="text-align:center;">
            <a href="https://your-official-website.com" target="_blank">
                <button style="
                    background-color:#2E7D32;
                    color:white;
                    padding:14px 30px;
                    font-size:18px;
                    border:none;
                    border-radius:12px;
                    cursor:pointer;
                ">
                    🌿 View Leaf X-Ray App
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
