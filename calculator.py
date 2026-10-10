
import streamlit as st
import math

st.set_page_config(page_title="Khadija", layout="centered")

st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at 20% 30%, #1a1f2e, #0f111a); }
    .stButton>button {
        width: 100%; height: 58px; font-size: 19px; font-weight: 600;
        border-radius: 14px;
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.15);
        color: #e6e8ff;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background: rgba(140, 255, 230, 0.15);
        border: 1px solid #8cffe6;
        color: #8cffe6;
        box-shadow: 0 0 15px rgba(140,255,230,0.4);
        transform: translateY(-1px);
    }
    div[data-testid="stTextInput"] input {
        font-size: 26px !important; text-align: right; height: 65px;
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(140,255,230,0.3) !important;
        border-radius: 16px !important;
        color: #b3fff0 !important;
    }
    /* Teal operators */
    .teal button { background: linear-gradient(135deg, #7dd3c0, #5fb3a3) !important; color: #0a1a16 !important; font-weight: 800 !important; }
    /* Purple Calculate */
    div[data-testid="stVerticalBlock"] .calculate button {
        background: linear-gradient(90deg, #8a6cff, #6ecfff) !important;
        color: white !important; font-size: 22px !important; height: 62px !important;
        box-shadow: 0 5px 20px rgba(110,207,255,0.4);
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#c5c8ff;'> Khadija </h2><p style='text-align:center;", unsafe_allow_html=True)

if 'expr' not in st.session_state: st.session_state.expr = ""

def press(v): st.session_state.expr += v
def clear(): st.session_state.expr = ""
def back(): st.session_state.expr = st.session_state.expr[:-1]

def calc():
    try:
        e = st.session_state.expr.replace('^','**').replace('π',str(math.pi)).replace('e',str(math.e))
        e = e.replace('√','math.sqrt').replace('sin','math.sin').replace('cos','math.cos').replace('tan','math.tan').replace('log','math.log10').replace('ln','math.log').replace('fact','math.factorial')
        res = eval(e)
        st.session_state.expr = str(round(res,10) if isinstance(res,float) else res)
    except: st.error("Invalid Expression")

st.text_input("display", value=st.session_state.expr, placeholder="sin(30) + √16", label_visibility="collapsed")

c1,c2,c3,c4,c5 = st.columns(5)
with c1: 
    if st.button("sin"): press("sin(")
    if st.button("7"): press("7")
    if st.button("4"): press("4")
    if st.button("1"): press("1")
    if st.button("π"): press("π")
with c2:
    if st.button("cos"): press("cos(")
    if st.button("8"): press("8")
    if st.button("5"): press("5")
    if st.button("2"): press("2")
    if st.button("e"): press("e")
with c3:
    if st.button("tan"): press("tan(")
    if st.button("9"): press("9")
    if st.button("6"): press("6")
    if st.button("3"): press("3")
    if st.button("("): press("(")
with c4:
    if st.button("log"): press("log(")
    if st.button("÷"): press("/")
    if st.button("×"): press("*")
    if st.button("−"): press("-")
    if st.button(")"): press(")")
with c5:
    if st.button("√"): press("√(")
    if st.button("C"): clear()
    if st.button("⌫"): back()
    if st.button("+"): press("+")
    if st.button("^"): press("^")

st.markdown('<div class="calculate">', unsafe_allow_html=True)
if st.button("✦ Calculate ✦", use_container_width=True): calc()
st.markdown('</div>', unsafe_allow_html=True)
