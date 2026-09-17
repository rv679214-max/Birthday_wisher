import streamlit as st
from utils import load_css, floating_decor, heart_divider, cute_photo, ASSETS

st.set_page_config(page_title="Memories 📸", page_icon="📸", layout="centered")
load_css()
floating_decor()

st.markdown('<div class="section-title">Our Little Gallery of You 📸</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="cute-subtitle" style="font-size:1.2em;">every picture, a piece of your magic ✨</div>',
    unsafe_allow_html=True,
)
heart_divider()

captions = [
    "that smile could stop time ❤️",
    "twirling into another beautiful year 💃",
    "effortlessly you 🌸",
    "shining brighter than the lights around you ✨",
    "grace, even from the back 🥹",
    "chasing views as beautiful as your soul 🏞️",
    "always finding the light, wherever you go ☀️",
]

images = [f"img{i}.jpg" for i in range(1, 8)]

# Show in a clean 2-column masonry-style layout
for i in range(0, len(images), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(images):
            with col:
                cute_photo(ASSETS / images[idx], captions[idx])

heart_divider()

st.markdown(
    """
    <div class="wish-card">
        <span class="wish-emoji">📷</span>
        Every single photo of you tells its own little story — but they all say
        the same thing: you light up every room, every frame, every moment you're
        in. Here's to many, many more memories with you in them. 💕
    </div>
    """,
    unsafe_allow_html=True,
)
