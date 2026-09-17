"""
Shared styling + small helpers for Roshini's Birthday Streamlit app.
Keep all the 'cute aesthetic' CSS here so every page looks consistent.
"""

import streamlit as st
import base64
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"


def img_to_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def load_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500;700&family=Poppins:wght@300;400;500;600&display=swap');

        /* Page background - soft pastel gradient */
        .stApp {
            background: linear-gradient(160deg, #fff0f3 0%, #ffe4ec 35%, #ffe9d6 70%, #fff6ea 100%);
            font-family: 'Poppins', sans-serif;
        }

        /* Hide default streamlit chrome, header, footer, menus, and repo information */
        header[data-testid="stHeader"] { visibility: hidden !important; height: 0 !important; }
        #MainMenu { visibility: hidden !important; display: none !important; }
        footer { visibility: hidden !important; display: none !important; }
        div[data-testid="stToolbar"] { visibility: hidden !important; height: 0 !important; display: none !important; }
        div[data-testid="stDecoration"] { visibility: hidden !important; height: 0 !important; display: none !important; }
        div[data-testid="stStatusWidget"] { visibility: hidden !important; height: 0 !important; display: none !important; }
        .viewerBadge_container__1S12D, .viewerBadge_link__1S12D { display: none !important; }
        button[title="View app source"] { display: none !important; }
        [data-testid="stAppDeployButton"] { display: none !important; }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffd6e0 0%, #ffe9d6 100%);
        }
        /* Style sidebar text WITHOUT touching icon fonts (fixes the
           collapse-arrow icon showing as literal text like
           "keyboard_double_arrow_right") */
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span:not([data-testid="stIconMaterial"]),
        section[data-testid="stSidebar"] a,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] li {
            color: #6b3d4d !important;
            font-family: 'Poppins', sans-serif;
        }
        /* Make sure any material icon keeps its own icon font & isn't hidden */
        [data-testid="stIconMaterial"] {
            font-family: 'Material Symbols Rounded', 'Material Icons', sans-serif !important;
        }

        /* ---------- Mobile responsiveness ---------- */
        @media (max-width: 600px) {
            .cute-title { font-size: 2.1em !important; }
            .cute-title + .cute-title { font-size: 2.6em !important; }
            .cute-subtitle { font-size: 1.2em !important; }
            .section-title { font-size: 1.6em !important; }
            .wish-card {
                padding: 18px 16px !important;
                font-size: 0.98em !important;
                margin: 12px 0 !important;
            }
            .photo-caption { font-size: 1.05em !important; }
            .footer-note { font-size: 1.05em !important; }
            .floaty { font-size: 1.3em !important; opacity: 0.35 !important; }
            div.stButton > button {
                width: 100%;
                padding: 0.7em 1em !important;
            }
            div[data-testid="column"] {
                width: 100% !important;
                flex: 1 1 100% !important;
                min-width: 100% !important;
            }
        }
        /* Block main content shouldn't be too cramped on small screens */
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 900px;
            padding-top: 2rem !important;
        }

        /* Headings in cute script font */
        .cute-title {
            font-family: 'Dancing Script', cursive;
            font-weight: 700;
            color: #d6336c;
            text-align: center;
            font-size: 3.4em;
            line-height: 1.1;
            margin-bottom: 0;
            text-shadow: 2px 2px 8px rgba(214, 51, 108, 0.15);
        }
        .cute-subtitle {
            font-family: 'Dancing Script', cursive;
            color: #e8598a;
            text-align: center;
            font-size: 1.8em;
            margin-top: -10px;
        }

        .section-title {
            font-family: 'Dancing Script', cursive;
            color: #d6336c;
            font-size: 2.2em;
            text-align: center;
            margin-bottom: 0.2em;
        }

        /* Cute message card */
        .wish-card {
            background: rgba(255, 255, 255, 0.65);
            border: 2px dashed #f7a8c4;
            border-radius: 22px;
            padding: 26px 30px;
            margin: 18px 0;
            box-shadow: 0 8px 22px rgba(230, 130, 160, 0.18);
            font-family: 'Poppins', sans-serif;
            color: #6b3d4d;
            font-size: 1.08em;
            line-height: 1.7;
        }
        .wish-emoji {
            font-size: 1.4em;
            margin-right: 6px;
        }

        /* Photo frame */
        .photo-frame {
            background: #fffaf7;
            border-radius: 18px;
            padding: 8px;
            box-shadow: 0 10px 24px rgba(214, 51, 108, 0.18);
            border: 4px solid #ffffff;
            outline: 2px solid #f7c6d9;
            margin-bottom: 6px;
        }
        .photo-frame img {
            border-radius: 12px;
            width: 100%;
            display: block;
        }
        .photo-caption {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #c94277;
            font-size: 1.3em;
            margin-top: -4px;
        }

        /* Divider hearts */
        .heart-divider {
            text-align: center;
            font-size: 1.4em;
            color: #f2789f;
            margin: 10px 0 26px 0;
            letter-spacing: 10px;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(135deg, #ff8fab, #ffb3c6);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 0.6em 1.6em;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
            box-shadow: 0 6px 14px rgba(255, 143, 171, 0.4);
            transition: transform 0.15s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-2px) scale(1.03);
            background: linear-gradient(135deg, #ff6f91, #ff9eb5);
            color: white;
        }

        /* Footer note */
        .footer-note {
            text-align: center;
            color: #b56576;
            font-family: 'Dancing Script', cursive;
            font-size: 1.3em;
            margin-top: 40px;
        }

        /* Floating balloons/emoji decoration */
        .floaty {
            position: fixed;
            font-size: 2em;
            opacity: 0.55;
            animation: floatUp 9s linear infinite;
            z-index: 0;
            pointer-events: none;
        }
        @keyframes floatUp {
            0%   { transform: translateY(0) rotate(0deg); opacity: 0; }
            10%  { opacity: 0.55; }
            90%  { opacity: 0.55; }
            100% { transform: translateY(-110vh) rotate(25deg); opacity: 0; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def floating_decor():
    """A few floating emoji (balloons/hearts) drifting up the page for ambience."""
    decor_html = ""
    items = [
        ("🎈", "6%", "0s"), ("💗", "18%", "2s"), ("🎂", "32%", "4s"),
        ("✨", "48%", "1s"), ("🎈", "63%", "3s"), ("💕", "77%", "5s"),
        ("🎉", "90%", "2.5s"),
    ]
    for emoji, left, delay in items:
        decor_html += (
            f'<div class="floaty" style="left:{left}; animation-delay:{delay};">{emoji}</div>'
        )
    st.markdown(decor_html, unsafe_allow_html=True)


def heart_divider():
    st.markdown('<div class="heart-divider">♡ ⋆｡˚ ♡ ⋆｡˚ ♡</div>', unsafe_allow_html=True)


def cute_photo(path: Path, caption: str = ""):
    """Render an image inside a soft rounded frame using raw HTML/CSS (image bytes untouched)."""
    b64 = img_to_base64(path)
    st.markdown(
        f"""
        <div class="photo-frame">
            <img src="data:image/jpeg;base64,{b64}" />
        </div>
        {f'<div class="photo-caption">{caption}</div>' if caption else ''}
        """,
        unsafe_allow_html=True,
    )