import re
import nltk
from io import StringIO
import streamlit as st
from web_scraping import WebScraper
from spacy_summariser import TextSummarizer
from pdf_text_extracter import Pdf2Text
from PyPDF2 import PdfReader

nltk.download('punkt_tab')

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return str(text)

def preprocess(summary_text):
    
    clean_text = re.sub(r'\[\d+\]', '', summary_text)

    sentences = nltk.sent_tokenize(clean_text)

    joined_sentences = []
    for i in range(0, len(sentences) - 1, 2):
        joined_sentences.append(f"{sentences[i]} {sentences[i + 1]}")

    if len(sentences) % 2 != 0:
        joined_sentences.append(sentences[-1])

    bullet_points = '\n'.join([f"- {sentence}" for sentence in joined_sentences])

    return bullet_points

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
        bullets = preprocess(summary)
        st.title(heading)
        st.write(bullets)
    
if option == "PDF":
    pdf = st.file_uploader("Drop File:")
    if pdf is not None:
        try:
            content = extract_text_from_pdf(pdf)
            summarizer = TextSummarizer(content,phrase,sentence)
            summary = summarizer.summarize()
            bullets = preprocess(summary)
            st.write(summary)
        except Exception as e:
            st.write("An error occurred:", e)
    
if option == "TEXT":
    text = st.text_input("Enter TEXT:")
    if text != "":
        summarizer = TextSummarizer(text,phrase,sentence)
        summary = summarizer.summarize()
        st.write(summary)
        
# extractive, abstractive = st.tabs(["Extractive","Abstractive"])

