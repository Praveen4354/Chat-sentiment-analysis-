import streamlit as st
import pandas as pd
from transformers import pipeline
import gc
import io

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = []

# UI Layout
st.set_page_config(page_title="Chat Message Sentiment Analyzer", layout="wide")
st.markdown("""
<style>
.main { background-color: #f0f2f6; padding: 20px; }
.stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
.stButton>button:hover { background-color: #45a049; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Settings")
    message = st.text_input("Enter a chat message:", placeholder="I love this app!")
    uploaded_file = st.file_uploader("Upload Chat Log (TXT)", type="txt")

# Main content
st.header("Chat Message Sentiment Analyzer")
if st.button("Analyze Message"):
    with st.spinner("Analyzing..."):
        try:
            # Cache model
            @st.cache_resource
            def load_model():
                return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=-1)  # CPU
            sentiment_pipeline = load_model()

            # Analyze single message
            if message.strip():
                result = sentiment_pipeline(message)
                st.session_state.results.append({
                    "Message": message,
                    "Sentiment": result[0]["label"],
                    "Score": result[0]["score"]
                })
            else:
                st.warning("Please enter a non-empty message.")
            gc.collect()

        except Exception as e:
            st.error(f"Error analyzing message: {str(e)}")

# Text file analysis
if uploaded_file:
    with st.spinner("Analyzing chat log..."):
        try:
            # Read text file line by line
            text_content = uploaded_file.read().decode("utf-8")
            messages = [line.strip() for line in io.StringIO(text_content).readlines() if line.strip()]
            messages = messages[:100]  # Limit to 100 for memory

            if messages:
                sentiment_pipeline = load_model()
                results = sentiment_pipeline(messages)
                for msg, res in zip(messages, results):
                    st.session_state.results.append({
                        "Message": msg,
                        "Sentiment": res["label"],
                        "Score": res["score"]
                    })
                st.success(f"Analyzed {len(messages)} messages.")
            else:
                st.warning("Text file is empty or contains no valid messages.")
            gc.collect()

        except Exception as e:
            st.error(f"Error analyzing text file: {str(e)}")

# Display results
if st.session_state.results:
    st.subheader("Results")
    st.dataframe(st.session_state.results, use_container_width=True)

# Download results
if st.session_state.results:
    df_results = pd.DataFrame(st.session_state.results)
    st.download_button(
        label="Download Results",
        data=df_results.to_csv(index=False),
        file_name="sentiment_results.csv",
        mime="text/csv"
    )