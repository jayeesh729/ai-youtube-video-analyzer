import streamlit as st
from yt import build_youtube_agent
from styles import load_css
from utils import *

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="AI YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

st.markdown(load_css(), unsafe_allow_html=True)

# -------------------------------------------------------
# SESSION STATE
# -------------------------------------------------------

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "video_url" not in st.session_state:
    st.session_state.video_url = ""

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

with st.sidebar:

    st.markdown("## 🎥 AI YouTube Analyzer")

    st.markdown("---")

    st.markdown("""
Analyze any public YouTube video using AI.

The application automatically:

- 📜 Extracts Transcript
- 🧠 Generates Summary
- ⏱ Creates Timeline
- 🎯 Finds Key Takeaways
- 📺 Embeds the Video
""")

    st.markdown("---")

    st.markdown("### ⚙ Technology")

    st.markdown("""
- **Framework:** Streamlit
- **Agent:** Agno
- **LLM:** Groq
- **Model:** Llama 3.1 8B Instant
- **Backend:** Python
""")

    st.markdown("---")

    st.markdown("### ✨ Features")

    for feature in FEATURES:
        st.write(feature)

    st.markdown("---")

    st.caption("Made with ❤️ using Streamlit + Agno")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown(
    """
<div class="title">
🎥 AI YouTube Video Analyzer
</div>

<div class="subtitle">
Analyze any YouTube video with AI-generated summaries,
timestamps, insights and key learning points.
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# INPUT AREA (Centered & Constrained to Medium Size)
# -------------------------------------------------------

col_in_left, col_in_mid, col_in_right = st.columns([1, 2, 1])

with col_in_mid:
    video_url = st.text_input(
        "🔗 Enter YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=xxxxxxxxxxx"
    )

    if video_url:
        if is_valid_youtube_url(video_url):
            st.success("✅ Valid YouTube Video")
        else:
            st.error("❌ Invalid YouTube URL")

    analyze = st.button(
        "🚀 Analyze Video",
        use_container_width=True
    )

# -------------------------------------------------------
# AI ANALYSIS
# -------------------------------------------------------

if analyze:

    # Validate input
    if not video_url:
        st.warning("⚠️ Please enter a YouTube video URL.")
        st.stop()

    if not is_valid_youtube_url(video_url):
        st.error("❌ Please enter a valid YouTube URL.")
        st.stop()

    # Save URL
    st.session_state.video_url = video_url

    # Progress UI
    progress_bar = st.progress(0)
    status = st.empty()

    try:

        # Step 1
        status.info(PROGRESS_MESSAGES[0])
        progress_bar.progress(20)

        # Create a NEW agent every request
        # (This fixes the token/context issue)
        agent = build_youtube_agent()

        # Step 2
        status.info(PROGRESS_MESSAGES[1])
        progress_bar.progress(40)

        # Step 3
        status.info(PROGRESS_MESSAGES[2])
        progress_bar.progress(60)

        with st.spinner("🧠 AI is analyzing the video..."):

            response = agent.run(
                f"""
Analyze this YouTube video:

{video_url}

Generate a professional report including:

1. Executive Summary

2. Key Topics Covered

3. Important Learning Points

4. Timeline with timestamps

5. Actionable Insights

6. Final Conclusion

Format everything in Markdown.
"""
            )

        # Step 4
        status.info(PROGRESS_MESSAGES[3])
        progress_bar.progress(80)

        report = clean_response(response.content)

        st.session_state.analysis = report

        # Step 5
        status.success(PROGRESS_MESSAGES[4])
        progress_bar.progress(100)

        st.balloons()

    except Exception as e:

        progress_bar.empty()

        status.empty()

        st.error("❌ Unable to analyze the video.")

        with st.expander("Show Error Details"):
            st.exception(e)

        st.stop()

# -------------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------------

if st.session_state.analysis:
    report = st.session_state.analysis

    st.markdown("---")
    st.markdown("### 📊 Analysis Dashboard")

    # Side-by-side layout: Left (Report & Raw Markdown), Right (Video & Actions)
    col_left, col_right = st.columns([13, 7], gap="large")

    with col_left:
        tab1, tab2 = st.tabs(["📝 Detailed Report", "💻 Raw Markdown"])
        
        with tab1:
            st.markdown(report)
            
        with tab2:
            st.code(report, language="markdown")

    with col_right:
        # Video Player Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 📺 Video Player")
        st.video(st.session_state.video_url)
        st.markdown('</div>', unsafe_allow_html=True)

        # Statistics Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 📈 Video Stats")
        stats = report_statistics(report)
        s1, s2, s3 = st.columns(3)
        s1.metric("Words", stats["Words"])
        s2.metric("Chars", stats["Characters"])
        s3.metric("Read Time", stats["Reading Time"])
        st.markdown('</div>', unsafe_allow_html=True)

        # Downloads Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 📥 Download Report")
        
        markdown_file = create_markdown_report(st.session_state.video_url, report)
        text_file = create_text_report(st.session_state.video_url, report)
        
        st.download_button(
            "⬇ Download Markdown",
            markdown_file,
            file_name=generate_filename("md"),
            mime="text/markdown",
            use_container_width=True,
        )
        st.download_button(
            "⬇ Download TXT",
            text_file,
            file_name=generate_filename("txt"),
            mime="text/plain",
            use_container_width=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Feedback Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### ⭐ Feedback")
        rating = st.slider("Rate the analysis", 1, 5, 5, key="user_rating")
        if st.button("Submit Feedback", use_container_width=True):
            st.success(f"Thank you! You rated this analysis ⭐ {rating}/5")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center;color:#64748B;font-size:0.9rem;padding:1rem 0;'>
    Made with 💙 using <b>Streamlit</b>, <b>Agno</b>, <b>Groq</b>, and <b>YouTubeTools</b>
    </div>
    """,
    unsafe_allow_html=True
)