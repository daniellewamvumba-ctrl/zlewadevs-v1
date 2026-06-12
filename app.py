import streamlit as st

st.set_page_config(
    page_title="Z.LewaDevs",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Z.LewaDevs")
st.markdown(
    """
    <div style='text-align: center; padding: 10px;'>
        <h3>🚀 Z.LewaDevs</h3>
        <p>Building Python • Data • Automation • SaaS</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", "4")

with col2:
    st.metric("Skills", "7")

with col3:
    st.metric("Platforms", "4")

st.divider()

st.subheader("⚡ Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🛠 Skills"):
        st.switch_page("pages/skills.py")

with col2:
    if st.button("📂 Projects"):
        st.switch_page("pages/projects.py")

with col3:
    if st.button("📱 Content"):
        st.switch_page("pages/content.py")
st.divider()

st.subheader("👤 Developer Profile")

st.info("""
Name: Daniel  
Brand: Z.LewaDevs  
Focus: Python, Data, Automation  
Goal: Build SaaS and automation systems  
Status: Building Version 1
""")

st.subheader("Building in Public")

st.divider()

st.header("👋 About Me")

st.write("""
Hi, I'm Daniel.

I am building Z.LewaDevs while learning software development in public.

My current focus is Python, data projects, web scraping,
data analysis, visualization, and Streamlit applications.

My long-term goal is to build useful software products,
automation systems, and technology businesses.
""")

st.divider()

st.header("🔥 Current Focus")

focus_items = [
    "Python Development",
    "Web Scraping",
    "Data Cleaning",
    "Data Analysis",
    "Data Visualization",
    "Streamlit Development",
    "Building Z.LewaDevs V1"
]

for item in focus_items:
    st.write(f"🎯 {item}")

st.divider()

st.header("📈 Version 1 Progress")

st.progress(40)

st.write(
    "The Z.LewaDevs V1 portfolio is currently under active development."
)

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
st.divider()

st.header("🗺 Current Roadmap")

roadmap = [
    "Learn Python",
    "Build Data Projects",
    "Master Streamlit",
    "Learn FastAPI",
    "Build APIs",
    "Create Automation Systems",
    "Launch SaaS Products"
]

for step in roadmap:
    st.write(f"✅ {step}")

st.divider()

st.header("🌐 Platforms")

st.write("💻 GitHub")
st.write("▶️ YouTube")
st.write("🎵 TikTok")
st.write("💼 LinkedIn")

st.divider()

st.header("🎯 Current Mission")

st.info(
    "Build Z.LewaDevs Version 1, improve my Python skills, "
    "and document my journey publicly."
)
