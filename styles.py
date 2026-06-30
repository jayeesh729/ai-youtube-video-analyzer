def load_css():
    return """
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Hide Streamlit Branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Cool-Toned Gradient Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #6366F1 0%, #3B82F6 50%, #06B6D4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
    letter-spacing: -1px;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: inherit;
    opacity: 0.7;
    margin-bottom: 35px;
    font-weight: 400;
}

/* Input Fields - Adaptive to Theme */
.stTextInput input {
    border-radius: 10px;
    padding: 10px 15px;
    transition: all 0.2s ease;
}

/* Main Action Button (Cool Gradient) */
.stButton button {
    background: linear-gradient(135deg, #4F46E5 0%, #06B6D4 100%) !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.15) !important;
}

.stButton button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.3) !important;
    background: linear-gradient(135deg, #5A52FF 0%, #08C7E7 100%) !important;
}

.stButton button:active {
    transform: translateY(0px) !important;
}

/* Cards - Adaptive to Theme */
.card {
    background: var(--secondary-background-color, rgba(0,0,0,0.05));
    padding: 20px;
    border-radius: 12px;
    border: 1px solid var(--border-color, rgba(0,0,0,0.1));
    margin-bottom: 20px;
    max-width: 480px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
}

/* Custom Success/Warning styling overrides */
.stSuccess, .stWarning, .stInfo {
    border-radius: 8px !important;
}

/* Expander Header styling */
.streamlit-expanderHeader {
    font-size: 16px !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
}

/* Cool Tabs Styling - Adaptive */
button[data-baseweb="tab"] {
    font-size: 15px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

button[data-baseweb="tab"]:hover {
    color: #06B6D4 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #3B82F6 !important;
    border-bottom-color: #3B82F6 !important;
}

/* Download Button (Cool Teal) */
.stDownloadButton button {
    background: #0F766E !important;
    color: white !important;
    border: 1px solid #14B8A6 !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

.stDownloadButton button:hover {
    background: #115E59 !important;
    box-shadow: 0 4px 12px rgba(20, 184, 166, 0.15) !important;
    transform: translateY(-1px) !important;
}

/* Cool Teal Spinner */
.stSpinner > div {
    border-top-color: #06B6D4 !important;
}

</style>
"""