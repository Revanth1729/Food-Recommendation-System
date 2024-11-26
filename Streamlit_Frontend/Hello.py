import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Welcome message
st.write("# Welcome to Food Recommendation System! 👋")
# Add a background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,0)), 
                    url("https://images.unsplash.com/photo-1490818387583-1baba5e638af?auto=format&fit=crop&q=80");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar content
#st.sidebar.success("Select a recommendation app.")
