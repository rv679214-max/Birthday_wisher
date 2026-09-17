# 🎂 Happy Birthday, Roshini — Streamlit App

A cute, multi-page Streamlit site to wish Roshini a happy birthday, built around
your 7 photos.

## Pages
- **app.py** — Home: big birthday banner + surprise button
- **pages/1_📸_Our_Memories.py** — photo gallery with captions
- **pages/2_💌_Birthday_Wishes.py** — several heartfelt birthday messages
- **pages/3_🎁_Just_For_You.py** — closing note + interactive "blow the candles" wish

Streamlit auto-builds the sidebar navigation from the `pages/` folder (the
number prefixes control the order, the emoji is just decoration).

## How to run

```bash
cd roshini_birthday
pip install -r requirements.txt
streamlit run app.py
```

It'll open in your browser at `http://localhost:8501`.

## Notes
- Your original photos are untouched in `assets/` — all the "look" (rounded
  frames, shadows, captions, layout) is done purely with CSS in `utils.py`, so
  the actual image files are never modified.
- FastAPI wasn't needed: Streamlit can display local images directly (via
  base64-embedded `<img>` tags for the custom frame styling), so there's no
  separate backend to run — just one app.
- Want to personalize further? Easiest edits:
  - Swap/re-order captions in `pages/1_📸_Memories.py`
  - Edit or add messages in the `wishes` list in `pages/2_💌_Birthday_Wishes.py`
  - Change colors/fonts in the `<style>` block inside `utils.py`
