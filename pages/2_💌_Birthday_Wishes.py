import streamlit as st
from utils import load_css, floating_decor, heart_divider

st.set_page_config(page_title="Birthday Wishes 💌", page_icon="💌", layout="centered")
load_css()
floating_decor()

st.markdown('<div class="section-title">A Few Things I Want You To Know 💌</div>', unsafe_allow_html=True)
heart_divider()

wishes = [
    ("🌷", "May this new year of your life be softer than the last — more laughter, "
           "less worry, more moments that make your heart feel full. You deserve every "
           "single bit of good coming your way."),
    ("🕯️", "You have this quiet strength that most people never notice, but I do. "
           "Every time life got hard, you kept going with grace, and that is one of "
           "the most beautiful things about you."),
    ("🌙", "I hope you know how much joy you bring into the lives of everyone around "
           "you, without even trying. The world is simply better with you in it."),
    ("🎂", "Here's to your dreams — the big loud ones and the quiet secret ones. "
           "May this year bring you closer to every single one of them."),
    ("💖", "No matter how old you get or how far life takes you, some things will "
           "never change: you will always be loved, always be cherished, and always, "
           "always be celebrated on this day."),
    ("🦋", "Happy Birthday, Roshini. Thank you for being exactly who you are — "
           "kind, real, a little chaotic, endlessly lovable. Never change that."),
]

for emoji, text in wishes:
    st.markdown(
        f"""
        <div class="wish-card">
            <span class="wish-emoji">{emoji}</span>{text}
        </div>
        """,
        unsafe_allow_html=True,
    )

heart_divider()

st.markdown(
    '<div class="footer-note">happy birthday, again and again 🎀</div>',
    unsafe_allow_html=True,
)
