import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_country_data, plot_ghi_boxplot

# -- Page config --
st.set_page_config(page_title="🌞 Solar Dashboard", layout="wide")

# -- Custom CSS: Argon Theme + Sidebar + Multiselect Fixes --
st.markdown("""
    <style>
        body {
            background-color: #0e1726;
        }

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(120deg, #11998e, #38ef7d);
            padding: 1rem;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: lightorange !important;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #d3d3d3;
            margin: 10px;
        }

        /* Multiselect container background */
        div[data-baseweb="select"] {
            background-color: #2f2f2f !important;  /* Dark gray box */
            border-radius: 10px;
            padding: 8px;
        }

        /* Multiselect text and selected items */
        div[data-baseweb="select"] * {
            color: #000000 !important;  /* Ensure text is visible */
        }

        /* Selected country tag style */
        .css-1r6slb0-MultiValue {
            background-color: lightgreen !important;
            color: black !important;
            border-radius: 8px;
        }

        /* Button hover effect */
        button[kind="primary"] {
            background-color: #e0e0e0 !important;
            color: #000000 !important;
            border-radius: 8px !important;
        }

        button[kind="primary"]:hover {
            background-color: #d6d6d6 !important;
            border-color: #aaaaaa !important;
        }

        .metric-card {
            background-color:darkgray;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .main-container {
            background-color:gray;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }

        .title-text {
            color: #ffffff;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 0.5rem;
        }

        .subtitle-text {
            color: #ecf0f1;
            text-align: center;
            margin-bottom: 2rem;
        }

        .stDataFrame th {
            background-color: #f2f2f2;
        }
    </style>
""", unsafe_allow_html=True)

# -- Header --
st.markdown("<div class='title-text'>🌞 Solar Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Visualizing GHI for Benin, Sierra Leone, and Togo</div>", unsafe_allow_html=True)

# -- Sidebar --
with st.sidebar:
    st.header("🔧 Filters")
    selected_countries = st.multiselect(
        "Select countries:",
        options=["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )

# -- Validation --
if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

# -- Load Data --
data = load_country_data(selected_countries)

# -- Metric Cards --
st.markdown("### 🔢 Key Metrics")
metrics = data.groupby("Country")["GHI"].agg(["mean", "median", "std"]).reset_index()

card_cols = st.columns(len(metrics))

for i, row in metrics.iterrows():
    with card_cols[i]:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #2c3e50;">{row['Country']}</h4>
            <p><b>Mean GHI:</b> {row['mean']:.1f} W/m²</p>
            <p><b>Median GHI:</b> {row['median']:.1f} W/m²</p>
            <p><b>Std Dev:</b> {row['std']:.1f}</p>
        </div>
        """, unsafe_allow_html=True)

# -- Main content container --
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

# -- Boxplot --
with col1:
    st.subheader("📊 GHI Distribution by Country")
    fig = plot_ghi_boxplot(data)
    st.pyplot(fig)

# -- Rankings Table --
with col2:
    st.subheader("🏆 Country Rankings")
    avg_ghi = data.groupby("Country")["GHI"].mean().reset_index().sort_values("GHI", ascending=False)
    st.dataframe(avg_ghi, use_container_width=True)
    top_country = avg_ghi.iloc[0]
    st.success(f"🥇 **{top_country['Country']}** leads with **{top_country['GHI']:.2f} W/m²** average GHI.")

# -- Insights --
st.subheader("📈 Insights")
st.markdown(f"""
- ☀️ **{top_country['Country']}** offers the strongest solar potential based on GHI.
- 📊 Variability is captured in the standard deviation; more consistent data is preferable.
- 📌 Use this data to inform targeted solar infrastructure investment.
""")

st.markdown("</div>", unsafe_allow_html=True)

# -- Footer --
st.caption("🚀 Styled with Argon-like Theme • Built with Streamlit • 10 Academy Week 0")
