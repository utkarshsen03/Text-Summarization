import re
import nltk
import time
import streamlit as st
from web_scraping import WebScraper
from spacy_summariser import TextSummarizer
from pretrained_t5 import AbstractiveSummary
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
    source = st.selectbox("**Select Source of text:**",["URL","PDF","TYPING"])
    method = st.selectbox("**Select Summarization Technique:**",["Extractive","Abstractive"])
    phrase = st.slider("Select phrase limit:",5,50,15)
    sentence = st.slider("Select sentence limit:",2,25,5)

if source == "URL":
    url = st.text_input("Enter URL:")
    if url != "":
        try:
            progress = st.status("Summarizing...")
            scraper = WebScraper(url)
            heading, content = scraper.extract_text()
            if method == "Extractive":
                summarizer = TextSummarizer(content,phrase,sentence)
                summary = summarizer.summarize()
            elif method == "Abstractive":
                summarizer = AbstractiveSummary(content)
                summary = summarizer.summarize()
                
            bullets = preprocess(summary)
            st.title(heading)
            st.write(bullets)
            progress.update(state='complete')
        except Exception as e:
            progress.update(state='error')
            st.write("An error occurred:", e)
        
elif source == "PDF":
    pdf = st.file_uploader("Drop File:")
    if pdf is not None:
        try:
            progress = st.status("Summarizing...")
            content = extract_text_from_pdf(pdf)
            summarizer = TextSummarizer(content,phrase,sentence)
            summary = summarizer.summarize()
            if method == "Extractive":
                summarizer = TextSummarizer(content,phrase,sentence)
                summary = summarizer.summarize()
            elif method == "Abstractive":
                summarizer = AbstractiveSummary(content)
                summary = summarizer.summarize()
                
            bullets = preprocess(summary)
            st.write(summary)
            progress.update(state='complete')
        except Exception as e:
            progress.update(state='error')
            st.write("An error occurred:", e)
        
elif source == "TYPING":
    text = st.text_input("Enter TEXT:")
    if text != "":
        try:
            preogress  = st.status("Summarizing...")
            if method == "Extractive":
                summarizer = TextSummarizer(text,phrase,sentence)
                summary = summarizer.summarize()
            elif method == "Abstractive":
                summarizer = AbstractiveSummary(text)
                summary = summarizer.summarize()
            summarizer = TextSummarizer(text,phrase,sentence)
            summary = summarizer.summarize()
            st.write(summary)
            preogress.update(state='complete')
        except Exception as e:
            preogress.update(state='error')
            st.write("An error occurred:", e)
        