import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Mapping for filenames
COUNTRY_FILES = {
    "Benin": "https://drive.google.com/uc?export=download&id=1HxFnR8XKpMSxxCxHwIPoLPIenqNfAWWY",
    "Sierra Leone": "https://drive.google.com/uc?export=download&id=1L9XaOIU71XU_4WuSWQJLXZkqYUuZdJYN",
    "Togo": "https://drive.google.com/uc?export=download&id=1YA1FKP3pNywma8oikGv2Y6-_IxOKA03W"
}

def load_country_data(countries):
    frames = []
    for country in countries:
        file_path = COUNTRY_FILES.get(country)
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df["Country"] = country
            frames.append(df)
    return pd.concat(frames, ignore_index=True)
    if not frames:
        st.error("🚫 No data available. Please upload or link CSV files.")
        return pd.DataFrame()  # Return empty DataFrame
    
def plot_ghi_boxplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="Country", y="GHI", palette="Set2", ax=ax)
    ax.set_title("GHI Distribution by Country")
    ax.set_ylabel("GHI (W/m²)")
    ax.set_xlabel("")
    return fig
