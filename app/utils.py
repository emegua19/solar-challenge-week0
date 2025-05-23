import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # Add this for displaying messages

# Mapping for Google Drive download URLs
COUNTRY_FILES = {
    "Benin": "https://drive.google.com/uc?export=download&id=1HxFnR8XKpMSxxCxHwIPoLPIenqNfAWWY",
    "Sierra Leone": "https://drive.google.com/uc?export=download&id=1L9XaOIU71XU_4WuSWQJLXZkqYUuZdJYN",
    "Togo": "https://drive.google.com/uc?export=download&id=1YA1FKP3pNywma8oikGv2Y6-_IxOKA03W"
}

def load_country_data(countries):
    frames = []
    for country in countries:
        url = COUNTRY_FILES.get(country)
        if url is None:
            st.warning(f"⚠️ No URL found for {country}")
            continue
        try:
            df = pd.read_csv(url)
            df["Country"] = country
            frames.append(df)
        except Exception as e:
            st.warning(f"⚠️ Could not load data for {country}: {e}")
    
    if not frames:
        st.error("🚫 No data could be loaded. Check your Drive links and file permissions.")
        return pd.DataFrame()
    
    return pd.concat(frames, ignore_index=True)

def plot_ghi_boxplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="Country", y="GHI", palette="Set2", ax=ax)
    ax.set_title("GHI Distribution by Country")
    ax.set_ylabel("GHI (W/m²)")
    ax.set_xlabel("")
    return fig
