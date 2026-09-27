import streamlit as st


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Projects | Z.LewaDevs",
    page_icon="🚀",
    layout="wide"
)


# --------------------------------------------------
# GITHUB REPOSITORY LINKS
# --------------------------------------------------

CLEANING_REPO = "https://github.com/daniellewamvumba-ctrl/cleaning-project"

ANALYSIS_REPO = "https://github.com/daniellewamvumba-ctrl/analysis_project"

VISUALIZATION_REPO = "https://github.com/daniellewamvumba-ctrl/data-visualisation-project"

PIPELINE_REPO = "https://github.com/daniellewamvumba-ctrl/end-to-end-data-pipeline"


# --------------------------------------------------
# LIVE DEMO LINKS
# Leave empty until a project has a live demo
# --------------------------------------------------

CLEANING_DEMO = ""

ANALYSIS_DEMO = ""

VISUALIZATION_DEMO = ""

PIPELINE_DEMO = ""


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 My Projects")

st.write(
    "A growing collection of practical Python, data, "
    "web scraping, visualization, and automation projects."
)

st.divider()


# --------------------------------------------------
# PROJECT CARD FUNCTION
# --------------------------------------------------

def project_card(
    project_id,
    icon,
    title,
    status,
    description,
    built,
    results,
    tools,
    github_link,
    demo_link
):

    with st.container(border=True):

        # Project title
        st.markdown(f"## {icon} {title}")

        # Status
        st.caption(status)

        # Description
        st.write(description)

        # What I built
        st.markdown("### 🧠 What I Built")

        st.write(built)

        # Results
        st.markdown("### 📌 Key Results")

        for result in results:
            st.write(f"• {result}")

        # Tools
        st.markdown("### 🛠️ Tech Stack")

        st.write(tools)

        # Buttons
        col1, col2 = st.columns(2)

        with col1:

            st.link_button(
                "💻 GitHub Repository",
                github_link,
                use_container_width=True
            )

        with col2:

            if demo_link:

                st.link_button(
                    "🌐 Live Demo",
                    demo_link,
                    use_container_width=True
                )

            else:

                st.button(
                    "🌐 Live Demo — Coming Soon",
                    disabled=True,
                    use_container_width=True,
                    key=f"live_demo_{project_id}"
                )


# --------------------------------------------------
# PROJECT 1 — DATA CLEANING
# --------------------------------------------------

project_card(

    project_id="cleaning",

    icon="🧹",

    title="Data Cleaning Project",

    status="✅ Completed",

    description=(
        "A reusable Python data-cleaning pipeline designed "
        "to transform messy datasets into structured, "
        "analysis-ready data."
    ),

    built=(
        "Built a cleaning workflow that checks missing values, "
        "data types, duplicates, and data quality before "
        "producing a cleaned dataset."
    ),

    results=[
        "Detected missing values",
        "Checked duplicate records",
        "Handled inconsistent data",
        "Validated cleaned data",
        "Created a reusable cleaning workflow"
    ],

    tools=(
        "Python • Pandas • Data Cleaning • "
        "Data Validation"
    ),

    github_link=CLEANING_REPO,

    demo_link=CLEANING_DEMO
)


st.write("")


# --------------------------------------------------
# PROJECT 2 — DATA ANALYSIS
# --------------------------------------------------

project_card(

    project_id="analysis",

    icon="📊",

    title="Sales Data Analysis Project",

    status="✅ Completed",

    description=(
        "A business-focused data analysis project that "
        "turns raw sales data into useful business insights."
    ),

    built=(
        "Built an analysis workflow to calculate revenue, "
        "discounts, average order value, product performance, "
        "regional performance, and customer segments."
    ),

    results=[
        "30 orders analyzed",
        "170 total units sold",
        "2,798,550 total revenue",
        "93,285 average order value",
        "Laptop was the top product",
        "Nairobi was the top region",
        "Corporate was the top customer segment"
    ],

    tools=(
        "Python • Pandas • Data Analysis • "
        "Business Intelligence"
    ),

    github_link=ANALYSIS_REPO,

    demo_link=ANALYSIS_DEMO
)


st.write("")


# --------------------------------------------------
# PROJECT 3 — DATA VISUALIZATION
# --------------------------------------------------

project_card(

    project_id="visualization",

    icon="📈",

    title="Data Visualization Project",

    status="✅ Completed",

    description=(
        "A visualization project that transforms business "
        "data into charts and visual insights that are easier "
        "to understand."
    ),

    built=(
        "Built visualizations for product performance, "
        "regional revenue, customer segments, and monthly "
        "revenue trends."
    ),

    results=[
        "Laptop generated the highest product revenue",
        "Nairobi generated the highest regional revenue",
        "Corporate generated the highest segment revenue",
        "March 2026 had the highest monthly revenue",
        "Created reusable visualization scripts"
    ],

    tools=(
        "Python • Pandas • Matplotlib • "
        "Data Visualization"
    ),

    github_link=VISUALIZATION_REPO,

    demo_link=VISUALIZATION_DEMO
)


st.write("")


# --------------------------------------------------
# PROJECT 4 — END-TO-END PIPELINE
# --------------------------------------------------

project_card(

    project_id="pipeline",

    icon="🔄",

    title="End-to-End Data Pipeline",

    status="🚧 In Progress",

    description=(
        "A complete data pipeline connecting web scraping, "
        "data cleaning, validation, analysis, and "
        "visualization."
    ),

    built=(
        "Built a workflow that collects raw book data from "
        "the web, stores the raw dataset, cleans it, validates "
        "the results, and prepares the data for analysis."
    ),

    results=[
        "Scraped 100 books",
        "Created raw data storage",
        "Created processed data storage",
        "Added data-cleaning workflow",
        "Added validation checks",
        "Connected multiple stages into one pipeline"
    ],

    tools=(
        "Python • Web Scraping • Requests • "
        "BeautifulSoup • Pandas • Streamlit"
    ),

    github_link=PIPELINE_REPO,

    demo_link=PIPELINE_DEMO
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.success(
    "🚀 Building practical systems one project at a time."
)