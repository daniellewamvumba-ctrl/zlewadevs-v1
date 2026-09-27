import streamlit as st


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Freelancing | Z.LewaDevs",
    page_icon="💼",
    layout="wide"
)


# --------------------------------------------------
# PROFILE LINKS
# 👇 PASTE YOUR REAL PROFILE LINKS HERE
# --------------------------------------------------

UPWORK_PROFILE = "https://www.upwork.com/freelancers/~01f9d84c917fb0e0f6"

FREELANCER_PROFILE = "https://www.freelancer.com/u/daniell643"


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>

    .freelance-card {
        padding: 28px;
        border-radius: 20px;
        border: 1px solid #334155;
        background: linear-gradient(
            145deg,
            #1e293b,
            #111827
        );
        min-height: 390px;
    }

    .platform-icon {
        font-size: 48px;
    }

    .platform-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 10px;
    }

    .platform-description {
        color: #cbd5e1;
        line-height: 1.6;
        margin-top: 12px;
    }

    .profile-status {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: #064e3b;
        color: #6ee7b7;
        font-size: 13px;
        margin-top: 10px;
    }

    .service-tag {
        color: #93c5fd;
        font-size: 14px;
        margin-top: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("💼 Freelancing Dashboard")

st.write(
    "Building a professional freelance presence around "
    "Python, data, web scraping, automation, and tools."
)

st.divider()


# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Freelance Platforms",
        "2"
    )

with col2:
    st.metric(
        "Core Services",
        "4"
    )

with col3:
    st.metric(
        "Portfolio Projects",
        "4"
    )

with col4:
    st.metric(
        "Profile Status",
        "Active"
    )


st.write("")


# --------------------------------------------------
# SERVICES
# --------------------------------------------------

st.subheader("🛠️ Services I Offer")

service1, service2, service3, service4 = st.columns(4)

with service1:
    st.info("🐍 **Python Development**")
    st.caption(
        "Python scripts, tools and automation."
    )

with service2:
    st.info("🕷️ **Web Scraping**")
    st.caption(
        "Collect structured data from websites."
    )

with service3:
    st.info("📊 **Data Analysis**")
    st.caption(
        "Clean, analyze and understand datasets."
    )

with service4:
    st.info("⚙️ **Automation**")
    st.caption(
        "Automate repetitive data workflows."
    )


st.divider()


# --------------------------------------------------
# FREELANCE PLATFORMS
# --------------------------------------------------

st.subheader("🌐 Freelance Platforms")

st.write(
    "Connect with me through my freelance profiles."
)

st.write("")


# --------------------------------------------------
# UPWORK CARD
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.markdown("## 💼 Upwork")

        st.markdown(
            '<div class="profile-status">'
            '🟢 Profile Active'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("### Python & Data Freelancer")

        st.write(
            "Offering practical Python, web scraping, "
            "data cleaning, data analysis, and automation services."
        )

        st.markdown("### 🛠️ Skills")

        st.write(
            "Python • Pandas • Web Scraping • "
            "Data Cleaning • Data Analysis • Automation"
        )

        st.markdown("### 📁 Portfolio")

        st.write(
            "4 practical projects available through "
            "the Z.LewaDevs portfolio."
        )

        st.link_button(
            "💼 View Upwork Profile",
            UPWORK_PROFILE,
            use_container_width=True
        )


# --------------------------------------------------
# FREELANCER CARD
# --------------------------------------------------

with col2:

    with st.container(border=True):

        st.markdown("## 🌐 Freelancer")

        st.markdown(
            '<div class="profile-status">'
            '🟢 Profile Active'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("### Python & Data Freelancer")

        st.write(
            "Providing Python development, web scraping, "
            "data cleaning, analysis, visualization, "
            "and automation solutions."
        )

        st.markdown("### 🛠️ Skills")

        st.write(
            "Python • Pandas • Matplotlib • Web Scraping • "
            "Data Analysis • Automation"
        )

        st.markdown("### 📁 Portfolio")

        st.write(
            "Projects and technical work are connected "
            "through the Z.LewaDevs portfolio."
        )

        st.link_button(
            "🌐 View Freelancer Profile",
            FREELANCER_PROFILE,
            use_container_width=True
        )


# --------------------------------------------------
# WORKFLOW
# --------------------------------------------------

st.divider()

st.subheader("🔄 My Freelancing Workflow")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.markdown("### 01")
    st.write("**Find the Problem**")
    st.caption(
        "Understand what the client needs."
    )

with step2:
    st.markdown("### 02")
    st.write("**Build the Solution**")
    st.caption(
        "Use Python, data and automation."
    )

with step3:
    st.markdown("### 03")
    st.write("**Deliver**")
    st.caption(
        "Provide a working, documented solution."
    )

with step4:
    st.markdown("### 04")
    st.write("**Build Long-Term Value**")
    st.caption(
        "Turn useful solutions into reusable systems."
    )


# --------------------------------------------------
# PORTFOLIO CONNECTION
# --------------------------------------------------

st.divider()

st.subheader("🚀 Freelancing + Z.LewaDevs")

st.write(
    "My freelance work is connected to my growing "
    "developer portfolio. Every project helps build "
    "real-world experience and demonstrates what I can build."
)

st.info(
    "💡 Portfolio → Freelance Skills → Client Projects → "
    "Reusable Systems → Future Products"
)