import streamlit as st

# Page title
st.set_page_config(page_title="Asthma Safety Monitor", layout="centered")

st.title("🫁 Asthma Safety Monitoring System")
st.write("Monitoring health and air quality to keep you safe")

# Sidebar
st.sidebar.header("User Details")
name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Age", min_value=1, max_value=100)

# Health data section
st.header("📊 Health Data")
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200)
oxygen_level = st.number_input("Oxygen Level (%)", min_value=50, max_value=100)

# Location section
st.header("📍 Location")
location = st.text_input("Current Location")

# Air Quality section
st.header("🌫️ Air Quality Index (AQI)")
aqi = st.number_input("Enter AQI value", min_value=0, max_value=500)

# Risk analysis
st.header("⚠️ Risk Analysis")

if st.button("Check Safety"):
    if oxygen_level < 92 or aqi > 150:
        st.error("⚠️ High Risk! Air quality is unsafe. Please take precautions.")
        st.write("✔️ Wear a mask")
        st.write("✔️ Avoid outdoor activities")
        st.write("✔️ Keep inhaler with you")
    else:
        st.success("✅ You are safe. Air quality is acceptable.")

# Footer
st.markdown("---")
st.caption("Developed using Streamlit")
