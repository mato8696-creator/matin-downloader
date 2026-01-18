import streamlit as st
import yt_dlp
import os

# 1. ڕێکخستنا لاپەڕەی
st.set_page_config(page_title="Matin Downloader", page_icon="📥")

# 2. سیستەمێ هەژمارکرنا بینەران (وەک سایتێ بۆڕسێ)
counter_file = "visitors_dl.txt"

def get_visitors():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f: f.write("150") # دەسپێک ژ ١٥٠
        return 150
    with open(counter_file, "r") as f:
        return int(f.read())

def add_visitor():
    count = get_visitors() + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count

if 'counted' not in st.session_state:
    st.session_state.visitor_count = add_visitor()
    st.session_state.counted = True
else:
    st.session_state.visitor_count = get_visitors()

# 3. ستایلێ سایتێ
st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; text-align: center; }
    h1 { color: #FF4B4B; text-shadow: 2px 2px 5px #000; }
    .stButton>button { width: 100%; background-color: #FF4B4B; color: white; border-radius: 10px; font-weight: bold; }
    .stTextInput>div>div>input { text-align: center; background-color: #1e2130 !important; color: white !important; }
    .visitor-card { background: rgba(255, 75, 75, 0.1); padding: 10px; border-radius: 10px; border: 1px solid #FF4B4B; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("📥 Matin Video Downloader")
st.write("لینکێ ڤیدیۆیا ئینستاگرام، فەیسبووک، یان تیکتۆکێ ل ڤێرە دانە:")

# 4. وەرگرتنا لینکی
url = st.text_input("URL:", placeholder="https://www.instagram.com/reel/...")

if st.button("Download / داونلۆد"):
    if url:
        with st.spinner('چەند چرکەکێ چەبەرێ بە...'):
            try:
                ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4', 'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video.mp4"):
                    with open("video.mp4", "rb") as f:
                        st.video(f.read())
                        st.download_button(
                            label="📥 Save Video / پاشکەفت بکە",
                            data=f,
                            file_name="matin_video.mp4",
                            mime="video/mp4"
                        )
                    os.remove("video.mp4")
            except:
                st.error("کێشەیەک هەیە، تکایە لینکێ ڕاست بدە")
    else:
        st.warning("تکایە لینکەکێ بنویسە!")

# 5. نیشاندانا بینەران و تێلەگرامێ
st.write("---")
st.markdown(f"""
<div class="visitor-card">
    <p style="margin:0; color:#FF4B4B;">👤 بینەرێن حەقیقی: {st.session_state.visitor_count:,}</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div style="margin-top:20px; color:#bf953f; font-weight:bold;">Matin A. Muhammed - 2026</div>', unsafe_allow_html=True)
st.markdown('<a href="https://t.me/badinimatin" target="_blank" style="display:block; background:#0088cc; color:white; text-align:center; padding:12px; border-radius:10px; text-decoration:none; margin-top:10px;">✈️ Join Telegram Channel</a>', unsafe_allow_html=True)
