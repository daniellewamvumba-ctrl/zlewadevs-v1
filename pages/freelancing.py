import streamlit as st

st.title("💼 Freelancing")

st.write(
    "Services I am developing as I grow my skills and portfolio."
)

st.divider()

services = [
    "Python Automation",
    "Web Scraping",
    "Data Cleaning",
    "Data Analysis",
    "Data Visualization Dashboards",
]

for service in services:
    st.write(f"✅ {service}")

st.divider()

st.subheader("Freelancing Platforms")

st.write("🔹 Upwork")
st.write("🔹 Fiverr")
st.write("🔹 Freelancer")

st.info(
    "My freelancing profiles are currently being built and will be linked here."
)