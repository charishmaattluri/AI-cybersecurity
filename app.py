import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Cybersecurity Agent",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- Session State ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "show_explanation" not in st.session_state:
    st.session_state.show_explanation = True

if "show_history" not in st.session_state:
    st.session_state.show_history = True

if "max_history" not in st.session_state:
    st.session_state.max_history = 10

# ---------------- Sidebar ----------------
with st.sidebar:

    with st.expander("⚙️ Settings", expanded=False):
        st.session_state.dark_mode = st.toggle(
            "Dark Mode",
            value=st.session_state.dark_mode
        )

        st.session_state.show_explanation = st.toggle(
            "Show AI Explanation",
            value=st.session_state.show_explanation
        )

        st.session_state.show_history = st.toggle(
            "Show Threat History",
            value=st.session_state.show_history
        )

        st.session_state.max_history = st.slider(
            "Max History Records",
            min_value=3,
            max_value=20,
            value=st.session_state.max_history
        )

        if st.button("Clear History", use_container_width=True):
            st.session_state.history = []

    st.divider()

    st.subheader("Threat Simulation")
    scenario = st.selectbox(
        "Select scenario",
        ["Phishing Attack", "Insider Threat"]
    )
    analyze = st.button("Analyze Threat", use_container_width=True)


# ---------------- THEME ----------------
if st.session_state.dark_mode:
    BG = "#020617"
    FG = "#e5e7eb"
    
    ACCENT = "#22d3ee"   # cyan
    MUTED = "#94a3b8"
else:
    BG = "#f1f5f9"
    FG = "#020617"
   
    ACCENT = "#2563eb"
    MUTED = "#475569"

# ---------------- CSS ----------------
st.markdown(f"""
<style>
body {{
    background-color: {BG};
    color: {FG};
}}
.main {{
    background-color: {BG};
}}

.hero {{
    padding: 32px;
    border-radius: 18px;
    background: linear-gradient(135deg, {ACCENT} 0%, #020617 100%);
    color: white;
    margin-bottom: 28px;
}}
.hero-title {{
    font-size: 36px;
    font-weight: 800;
}}
.hero-sub {{
    font-size: 16px;
    opacity: 0.9;
}}


.step {{
    font-size: 13px;
    letter-spacing: 1px;
    color: {ACCENT};
    font-weight: 700;
}}

.value {{
    font-size: 28px;
    font-weight: 800;
}}

.label {{
    font-size: 13px;
    color: {MUTED};
}}

hr {{
    border: none;
    border-top: 1px solid #334155;
    margin: 18px 0;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown(f"""
<div class="hero">
    <div class="hero-title">🛡️ AI Cybersecurity Agent</div>
    <div class="hero-sub">
        Behavioral threat intelligence for phishing & insider risks
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN FLOW ----------------
if analyze:
    url = "http://127.0.0.1:8000/phishing" if scenario == "Phishing Attack" else "http://127.0.0.1:8000/insider"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        st.session_state.history.insert(0, {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Scenario": scenario,
            "Risk": data["risk_level"],
            "Score": data["risk_score"]
        })
        st.session_state.history = st.session_state.history[:8]

        # -------- STEP 2: REPORT --------
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.markdown("<div class='step'>STEP 2 · RISK REPORT</div>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='label'>Risk Level</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='value'>{data['risk_level']}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='label'>Risk Score</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='value'>{data['risk_score']}</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='label'>Scenario</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='value'>{scenario}</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("### 🧠 AI Reasoning")
        st.write(data["explanation"])

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("### ⚡ Response Guidance")
        st.warning(data["recommended_action"])

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>STEP 1 · START ANALYSIS</div>", unsafe_allow_html=True)
    st.write("Choose a threat type from the sidebar and run analysis.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HISTORY ----------------
if st.session_state.history:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>ACTIVITY LOG</div>", unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇ Export Activity Log",
        csv,
        "threat_activity_log.csv",
        "text/csv",
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
