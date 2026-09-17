import streamlit as st
from utils import load_css, floating_decor, heart_divider, cute_photo, ASSETS

st.set_page_config(page_title="Just For You 🎁", page_icon="🎁", layout="centered")
load_css()
floating_decor()

st.markdown('<div class="section-title">Just For You, Roshini 🎁</div>', unsafe_allow_html=True)
heart_divider()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    cute_photo(ASSETS / "img2.jpg", "still the same warm heart 🌹")

st.markdown(
    """
    <div class="wish-card" style="font-size:1.12em;">
        <span class="wish-emoji">🕰️</span>
        If I could give you anything today, it would be the certainty that you are
        exactly where you're meant to be — loved fully, seen clearly, and appreciated
        more than words can really say. <br><br>
        So today, let yourself be celebrated. Let people spoil you a little. Eat the
        cake first if you want to. You've earned every candle on it, and every wish
        that comes with it. 🕯️
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

center = st.columns([1, 1.4, 1])[1]
with center:
    if "candles_blown" not in st.session_state:
        st.session_state.candles_blown = False

    if not st.session_state.candles_blown:
        if st.button("🕯️ Blow the candles & make a wish"):
            st.session_state.candles_blown = True

if st.session_state.candles_blown:
    st.balloons()
    st.markdown(
        """
        <div class="wish-card" style="text-align:center;">
            🌠 Whatever you wished for — I hope it comes true, quietly and completely.<br>
            Happy Birthday, Roshini. Today and always, you are so deeply loved. 💗
        </div>
        """,
        unsafe_allow_html=True,
    )

heart_divider()
st.markdown(
    '<div class="footer-note">with all my love, today and every day 🎀</div>',
    unsafe_allow_html=True,
)
