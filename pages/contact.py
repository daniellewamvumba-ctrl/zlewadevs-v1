import streamlit as st

st.title("📧 Contact")

st.write(
    "Connect with me and follow my development journey."
)

st.divider()

st.subheader("Platforms")

st.write("💻 GitHub")
st.write("▶️ YouTube")
st.write("🎵 TikTok")
st.write("💼 LinkedIn")

st.divider()

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    st.success(
        "Contact form received. Backend functionality will be added in a future version."
    )