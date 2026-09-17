import time
import streamlit as st
from utils import load_css, floating_decor, heart_divider, cute_photo, ASSETS

st.set_page_config(
    page_title="Happy Birthday Roshini 🎂",
    page_icon="🎂",
    layout="centered",
)

load_css()
floating_decor()

st.markdown('<div class="cute-title">Happy Birthday</div>', unsafe_allow_html=True)
st.markdown('<div class="cute-title" style="font-size:4.4em; margin-top:-10px;">Roshini 🎀</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="cute-subtitle">today the world got a little brighter, again ✨</div>',
    unsafe_allow_html=True,
)

heart_divider()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    cute_photo(ASSETS / "img4.jpg", "my favourite person 💚")

st.markdown(
    """
    <div class="wish-card">
        <span class="wish-emoji">🎉</span>
        Happy Birthday, Roshini! Another year has arrived, and with it, another year
        of your laugh, your warmth, and that stubborn, wonderful spirit of yours
        lighting up everyone around you. Today isn't just about you turning a year
        older — it's a celebration of everything you are and everything you're
        still becoming.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

center = st.columns([1, 1.2, 1])[1]
with center:
    if st.button("🎁 Click for a Birthday Surprise!"):
        st.balloons()
        st.snow()
        st.markdown(
            """
            <div class="wish-card" style="text-align:center; font-size:1.3em;">
                🌸 You are so, so loved, Roshini. 🌸<br>
                Go check the <b>"Just For You"</b> page in the sidebar 💌
            </div>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(0.2)

st.markdown(
    """
    <div class="footer-note">
        use the menu on the left to see our memories & more wishes 🌷
    </div>
    """,
    unsafe_allow_html=True,
)
