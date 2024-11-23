import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class AbstractiveSummary:
    def __init__(self,text):
        self.tokenizer = AutoTokenizer.from_pretrained('T5-base')
        self.model = AutoModelForSeq2SeqLM.from_pretrained('T5-base', return_dict=True)

        self.text = text
        
    def summarize(self):
        sequence = (self.text)

        inputs = self.tokenizer.encode("sumarize: " +sequence,return_tensors='pt', max_length=512, truncation=True)
        output = self.model.generate(inputs, min_length=80, max_length=100)
        summary = self.tokenizer.decode(output[0])
        
        return summary