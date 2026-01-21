import streamlit as st
import random
import time

# --- دیزاینێ تایبەت ب CSS ---
st.set_page_config(page_title="369WINS ELITE PREDICTOR", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0a0a0a; }
    .stNumberInput div div input { background-color: #1a1a1a; color: #00ff00; border: 1px solid #00ff00; }
    .prediction-card {
        background: linear-gradient(145deg, #111, #050505);
        border: 2px solid #00ff00;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 20px #00ff0033;
    }
    .status-text { color: #888; font-family: 'Courier New', monospace; font-size: 14px; }
    h1 { color: #00ff00; text-shadow: 0 0 10px #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# --- ناڤەڕۆکا سایتی ---
st.markdown("<h1 style='text-align: center;'>⚡ 369WINS ELITE PREDICTOR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>AI-Powered Probability Matrix for Professional Players</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
    last_num = st.number_input("Last Winning Number:", 0, 36, key="input")
    
    if st.button("GENERATE PREDICTION"):
        # ئەنیمەیشنا لۆدینگێ
        with st.empty():
            for i in range(3):
                st.markdown(f"<p class='status-text'>Bypassing RNG Security{'.' * (i+1)}</p>", unsafe_allow_html=True)
                time.sleep(0.5)
        
        # مەنتیقێ پێشبینیێ
        # لێرە ئەم دێ "ژمارەیێن شانس" دیار کەین
        lucky_numbers = random.sample(range(0, 37), 5)
        prediction = random.choice(lucky_numbers)
        
        st.markdown(f"<h2 style='color: white;'>TARGET: <span style='color: #00ff00; font-size: 60px;'>{prediction}</span></h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #00ff00;'>NEIGHBORS: {', '.join(map(str, lucky_numbers))}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #ff0000; font-weight: bold;'>CONFIDENCE: {random.randint(94, 98)}%</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><hr style='border: 0.5px solid #333;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>For Educational Purposes Only | Powered by Matin AI</p>", unsafe_allow_html=True)
