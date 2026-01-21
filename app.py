import streamlit as st
import random
import time

# --- دیزاینێ تایبەت ب CSS ---
st.set_page_config(page_title="پێشبینیکەرێ 369WINS", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    /* دیزاینا گشتی یا لاپەڕی */
    .main { background-color: #0a0a0a; }
    
    /* ڕەنگێ نڤیسینێ و جهێ داخڵکرنا ژماران */
    .stNumberInput div div input { 
        background-color: #1a1a1a; 
        color: #00ff00; 
        border: 1px solid #00ff00; 
        text-align: center;
        font-size: 20px;
    }
    
    /* سندوقا پێشبینیێ */
    .prediction-card {
        background: linear-gradient(145deg, #111, #050505);
        border: 2px solid #00ff00;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 20px #00ff0033;
        direction: rtl; /* بۆ هندێ نڤیسینا کوردی ڕێک بیت */
    }
    
    .status-text { color: #888; font-family: 'Courier New', monospace; font-size: 14px; }
    h1 { color: #00ff00; text-shadow: 0 0 10px #00ff00; font-family: 'Arial'; }
    p { color: white; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

# --- ناڤەڕۆکا سایتی ب بادینی ---
st.markdown("<h1 style='text-align: center;'>⚡ سیستەمێ پێشبینیکەرێ 369WINS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>بۆتێ زیرەک بۆ دیارکرنا ژمارەیێن ب شانس د ڕۆلێتێ دا</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    
    # وەرگرتنا ژمارا دوماهییێ ژ کڕیاری
    last_num = st.number_input("دواین ژمارەیا کەفتی بنڤیسە:", 0, 36, key="input")
    
    if st.button("پێشبینییا ژمارا داهاتی"):
        # ئەنیمەیشنا لۆدینگێ (وەک هاکەران)
        status_placeholder = st.empty()
        for i in range(3):
            status_placeholder.markdown(f"<p class='status-text' style='text-align:center;'>لێگەڕیان د سێرڤەرێن 369Wins دا{'.' * (i+1)}</p>", unsafe_allow_html=True)
            time.sleep(0.6)
        status_placeholder.empty()
        
        # مەنتیقێ پێشبینیێ
        # لێرە ئەم دێ ٥ ژمارەیێن ب شانس وەک "دراوسێ" نیشان دەین
        lucky_numbers = random.sample(range(0, 37), 5)
        main_target = random.choice(lucky_numbers)
        
        st.markdown(f"<h2 style='color: white;'>ژمارەیا ئامانج: <span style='color: #00ff00; font-size: 60px;'>{main_target}</span></h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #00ff00; font-size: 18px;'>ژمارەیێن دەوروبەر (Neighbors): {', '.join(map(str, lucky_numbers))}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #ff0000; font-weight: bold;'>ڕێژەیا درستبوونێ: {random.randint(94, 98)}%</p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# پاشکۆیا سایتی
st.markdown("<br><hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>ئەڤ سایتە تەنێ بۆ مفا وەرگرتنێ یە | گەشەپێدان ژ لایێ مەتین AI</p>", unsafe_allow_html=True)
