import streamlit as st

st.set_page_config(
    page_title="Z.LewaDevs",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Z.LewaDevs")

st.subheader("Building in Public")

st.write("""
Welcome to my developer journey.

I am learning and building:
- Python
- Web Scraping
- Data Cleaning
- Data Analysis
- Data Visualization
- Streamlit Applications
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Skills", "7")

with col2:
    st.metric("Projects", "4")

with col3:
    st.metric("Platforms", "4")

st.divider()

st.header("Current Mission")

st.info(
    "Build Z.LewaDevs Version 1 and document the journey publicly."
)
