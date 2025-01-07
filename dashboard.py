import streamlit as st
import pandas as pd

st.set_page_config(page_title="Real-Time Health Advisory System", layout="wide")

st.title("📊 Real-Time Health Advisory System")
st.markdown("A live dashboard for tracking health metrics and RAG-based recommendations.")

@st.cache_data
def load_data(file_name="processed_health_data.csv"):
    """
    Load processed health data.
    """
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        return pd.DataFrame(columns=["timestamp", "heart_rate", "steps", "spo2", "calories", "recommendation"])

data = load_data()

if not data.empty:
    st.subheader("Latest Metrics and Recommendations")
    st.dataframe(data.tail(10))

    st.subheader("Summary Insights")
    avg_heart_rate = data["heart_rate"].mean()
    total_steps = data["steps"].sum()
    avg_spo2 = data["spo2"].mean()

    st.write(f"**Average Heart Rate:** {avg_heart_rate:.2f} BPM")
    st.write(f"**Total Steps:** {total_steps}")
    st.write(f"**Average SpO₂:** {avg_spo2:.2f}%")

    st.subheader("Latest Recommendation")
    latest_recommendation = data.iloc[-1]["recommendation"]
    st.success(latest_recommendation)
else:
    st.write("Waiting for processed data...")
