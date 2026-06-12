import streamlit as st

st.title("📱 Content Creation")

st.write(
    "I document my learning journey and share what I build."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("▶️ YouTube")
    st.write("Python tutorials, projects, and learning updates.")

with col2:
    st.subheader("🎵 TikTok")
    st.write("Short-form coding content and programming tips.")

st.divider()

st.subheader("💼 LinkedIn")

st.write(
    "Professional updates, networking, and project sharing."
)

st.divider()

st.subheader("💻 GitHub")

st.write(
    "Source code, repositories, and open project development."
)