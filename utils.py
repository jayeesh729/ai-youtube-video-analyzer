import re
from datetime import datetime


# ---------------------------------------------------
# Validate YouTube URL
# ---------------------------------------------------
def is_valid_youtube_url(url: str) -> bool:
    """
    Validate different YouTube URL formats.
    """

    if not url:
        return False

    pattern = (
        r'^(https?://)?(www\.)?'
        r'(youtube\.com|youtu\.be)/'
        r'(watch\?v=|embed/|shorts/|v/)?'
        r'([^&=%\?]{11})'
    )

    return bool(re.match(pattern, url))


# ---------------------------------------------------
# Generate Markdown Report
# ---------------------------------------------------
def create_markdown_report(video_url: str, report: str) -> str:
    """
    Creates a markdown file content.
    """

    return f"""# 🎥 AI YouTube Video Analysis

## Video

{video_url}

---

## Analysis Report

{report}

---

Generated using AI YouTube Video Analyzer

Generated on: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
"""


# ---------------------------------------------------
# Generate TXT Report
# ---------------------------------------------------
def create_text_report(video_url: str, report: str) -> str:

    return f"""
AI YouTube Video Analyzer

Video:
{video_url}

==========================================

Analysis

{report}

==========================================

Generated:
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
"""


# ---------------------------------------------------
# Clean Response
# ---------------------------------------------------
def clean_response(response: str) -> str:
    """
    Removes unwanted whitespace.
    """

    if not response:
        return ""

    response = response.strip()

    response = re.sub(r'\n{3,}', '\n\n', response)

    return response


# ---------------------------------------------------
# Count Words
# ---------------------------------------------------
def word_count(text: str) -> int:

    return len(text.split())


# ---------------------------------------------------
# Count Characters
# ---------------------------------------------------
def character_count(text: str) -> int:

    return len(text)


# ---------------------------------------------------
# Estimate Reading Time
# ---------------------------------------------------
def reading_time(text: str) -> int:
    """
    Average reading speed = 200 words/min
    """

    words = word_count(text)

    return max(1, words // 200)


# ---------------------------------------------------
# Report Statistics
# ---------------------------------------------------
def report_statistics(text: str):

    return {
        "Words": word_count(text),
        "Characters": character_count(text),
        "Reading Time": f"{reading_time(text)} min"
    }


# ---------------------------------------------------
# Download File Name
# ---------------------------------------------------
def generate_filename(extension: str):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"youtube_analysis_{timestamp}.{extension}"


# ---------------------------------------------------
# Progress Messages
# ---------------------------------------------------
PROGRESS_MESSAGES = [
    "🔍 Fetching YouTube metadata...",
    "📜 Extracting transcript...",
    "🧠 Sending transcript to AI...",
    "📊 Generating summary...",
    "✨ Formatting report..."
]


# ---------------------------------------------------
# Feature Cards
# ---------------------------------------------------
FEATURES = [
    "📚 Detailed Summary",
    "🧠 AI Insights",
    "⏱ Timestamp Analysis",
    "🎯 Key Takeaways",
    "📄 Download Report",
    "📺 Embedded Video"
]