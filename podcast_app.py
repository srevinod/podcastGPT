import streamlit as st

# Title of your app
st.title("Podcast Summaries Showcase")

# Stylish header
st.markdown(
    "<h2 style='text-align: center; color: #FF5733;'>Dive into Podcast Summaries</h2>",
    unsafe_allow_html=True
)

# Sample podcast summary with enhanced formatting
sample_summary = """
<div style='background-color: #F7F7F7; padding: 10px; border-radius: 10px;'>
    <h3 style='color: #333;'>Episode: AI and Society</h3>
    <p>In this episode, we dive deep into the world of artificial intelligence and its impact on society.</p>
    <p>Our guest, Dr. Jane Smith, a leading AI researcher, shares insights into the latest advancements</p>
    <p>and discusses ethical considerations surrounding AI technologies.</p>
</div>
"""

# Display the enhanced sample summary
st.markdown(sample_summary, unsafe_allow_html=True)

# User input for RSS feed URL
rss_feed_url = st.text_input("Enter RSS Feed URL:", "")

# Display the user input
st.write(f"You entered: {rss_feed_url}")