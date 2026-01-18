import streamlit as st
import requests
import yt_dlp
import os

# --- زانیاریێن بۆتی ---
BOT_TOKEN = "7612088680:AAHcS-ne1w1_zELDGu-htQAKs6wIQfSbzj4"
CHANNEL_ID = "@badinimatin" 
MY_ADMIN_ID = "2010296486" # ئایدییا تە یا تایبەت بۆ هندێ بێ مەرج داخل ببی

st.set_page_config(page_title="Matin VIP Downloader", page_icon="📥")

# ستایلێ سایتێ
st.markdown("<style>.stApp{background:#0e1117; color:white; text-align:center;}</style>", unsafe_allow_html=True)

if "authorized" not in st.session_state:
    st.session_state.authorized = False

# ١. پشکا پشکنینا تێلەگرامێ
if not st.session_state.authorized:
    st.title("📥 Matin VIP Downloader")
    st.warning("⚠️ تکایە جوین کەنالی بکی بەری داونلۆدێ")
    st.markdown(f'<a href="https://t.me/badinimatin" target="_blank" style="background:#0088cc; color:white; padding:10px 20px; border-radius:10px; text-decoration:none;">Join Telegram Channel</a>', unsafe_allow_html=True)
    
    user_id = st.text_input("ئایدییا خۆ یا تێلەگرامێ ل ڤێرە بنویسە (User ID):")
    
    if st.button("پشکنین و چوونە ناڤ سایتی"):
        # ئەگەر ئایدییا تە بوو، ڕاستەوخۆ سایت ڤەبیت
        if user_id == MY_ADMIN_ID:
            st.session_state.authorized = True
            st.success("✅ سلاڤ مەتین! تو ب سەرکەفتییانە داخل بووی.")
            st.rerun()
        
        # بۆ خەلکێ دی، پشکنینا کەنالی دکەت
        url_check = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id={CHANNEL_ID}&user_id={user_id}"
        try:
            res = requests.get(url_check).json()
            if res.get("ok") and res["result"]["status"] in ["member", "administrator", "creator"]:
                st.session_state.authorized = True
                st.success("✅ سوپاس! نوکە تو دشێی داونلۆد بکەی.")
                st.rerun()
            else:
                st.error("❌ تە هێشتا جوین نەکرییە یان ئایدی خەلەتە.")
        except:
            st.error("کێشەیەک د سێرڤەری دا هەیە.")
    st.stop()

# ٢. پشکا داونلۆدەرێ (VIP)
st.title("📥 Matin Downloader (VIP Access)")
video_url = st.text_input("لینکێ ڤیدیۆیێ ل ڤێرە دانە:")

if st.button("Download"):
    if video_url:
        with st.spinner('Preparing video...'):
            try:
                ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                with open("video.mp4", "rb") as f:
                    st.video(f.read())
                    st.download_button("📥 Save Video", f, "video.mp4")
                os.remove("video.mp4")
            except:
                st.error("کێشەیەک هەیە، لینکێ ڕاست بدە.")
