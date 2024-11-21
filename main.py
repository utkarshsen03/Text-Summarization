import streamlit as st
from web_scraping import WebScraper
from spacy_summariser import TextSummarizer

def summarization(path):
    scraper = WebScraper(path)
    heading, content = scraper.extract_text()
    summarizer = TextSummarizer(content,phrase,sentence)
    summary = summarizer.summarize()
    return heading, summary

st.title("Text Summarization")

with st.sidebar:
    st.title("Text Summarizer")
    st.markdown('---')
    option = st.selectbox("**Select Summarization way:**",["URL","PDF","TEXT"])
    phrase = st.slider("Select phrase limit:",5,50,15)
    sentence = st.slider("Select sentence limit:",2,25,5)

if option == "URL":
    url = st.text_input("Enter URL:")
    if url != "":
        heading, summary = summarization(url)
        st.title(heading)
        st.write(summary)
    
if option == "PDF":
    pdf = st.file_uploader("Drop File:")

if option == "TEXT":
    text = st.text_input("Enter TEXT:")
    if text != "":
        summarizer = TextSummarizer(text,phrase,sentence)
        summary = summarizer.summarize()
        st.write(summary)
        
# extractive, abstractive = st.tabs(["Extractive","Abstractive"])

