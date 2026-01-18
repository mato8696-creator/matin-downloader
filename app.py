import streamlit as st
import yt_dlp
import os

# ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="Matin Downloader", page_icon="📥")

# ستایلێ سایتێ
st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; text-align: center; }
    h1 { color: #FF4B4B; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("📥 Matin Video Downloader")
st.write("لینکێ ڤیدیۆیێ ل ڤێرە دانە (Instagram, Facebook, TikTok)")

# وەرگرتنا لینکی
url = st.text_input("URL:", placeholder="https://...")

if st.button("Download / داونلۆد"):
    if url:
        with st.spinner('چەند چرکەکێ چەبەرێ بە...'):
            try:
                ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video.mp4"):
                    with open("video.mp4", "rb") as f:
                        st.video(f.read())
                        st.download_button("📥 Save Video / پاشکەفت بکە", f, "video.mp4")
                    os.remove("video.mp4")
            except:
                st.error("کێشەیەک هەیە، تکایە لینکێ ڕاست بدە")
    else:
        st.warning("تکایە لینکەکێ بنویسە!")

st.write("---")
st.markdown("<p style='color:#bf953f;'>Matin A. Muhammed - 2026</p>", unsafe_allow_html=True)

