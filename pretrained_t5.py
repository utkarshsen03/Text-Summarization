import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class AbstractiveSummary:
    def __init__(self, text):
        self.tokenizer = AutoTokenizer.from_pretrained('T5-base')
        self.model = AutoModelForSeq2SeqLM.from_pretrained('T5-base', return_dict=True)
        self.text = text
        
    def chunk_text(self, max_chunk_size):
        """Splits text into chunks within the max_chunk_size token limit."""
        tokens = self.tokenizer.tokenize(self.text)
        chunks = []
        current_chunk = []

        for token in tokens:
            current_chunk.append(token)
            if len(self.tokenizer.convert_tokens_to_ids(current_chunk)) >= max_chunk_size:
                chunks.append(self.tokenizer.convert_tokens_to_string(current_chunk))
                current_chunk = []

        # Add the last chunk if it exists
        if current_chunk:
            chunks.append(self.tokenizer.convert_tokens_to_string(current_chunk))
        
        return chunks

    def summarize_chunk(self, chunk):
        """Generates a summary for a single chunk."""
        inputs = self.tokenizer.encode("summarize: " + chunk, return_tensors='pt', max_length=512, truncation=True)
        output = self.model.generate(inputs, min_length=80, max_length=100)
        summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return summary
    
    def summarize(self):
        """Summarizes the entire text by chunking it first."""
        max_chunk_size = 512  # Limit for the model
        chunks = self.chunk_text(max_chunk_size)
        summaries = [self.summarize_chunk(chunk) for chunk in chunks]
        return " ".join(summaries)
