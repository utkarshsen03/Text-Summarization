import streamlit as st
from web_scraping import WebScraper
from spacy_summariser import TextSummarizer
from streamlit_pdf_viewer import pdf_viewer
from pdf_text_extracter import Pdf2Text

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
        scraper = WebScraper(url)
        heading, content = scraper.extract_text()
        summarizer = TextSummarizer(content,phrase,sentence)
        summary = summarizer.summarize()
        st.title(heading)
        st.write(summary)
    
if option == "PDF":
    pdf = st.file_uploader("Drop File:")
    if pdf != "":
        pdf2text = Pdf2Text(pdf)
        content = pdf2text.extract_text()
        summarizer = TextSummarizer(content,phrase,sentence)
        summary = summarizer.summarize()
        st.write(summary)
    
if option == "TEXT":
    text = st.text_input("Enter TEXT:")
    if text != "":
        summarizer = TextSummarizer(text,phrase,sentence)
        summary = summarizer.summarize()
        st.write(summary)
        
# extractive, abstractive = st.tabs(["Extractive","Abstractive"])

