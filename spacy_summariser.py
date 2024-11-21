import spacy
import pytextrank


class TextSummarizer:
    def __init__(self,text,phrase_limit,sentence_limit):
        self.text = text
        self.phrase_limit = phrase_limit
        self.sentence_limit = sentence_limit
    
    def summarize(self):
        nlp = spacy.load('en_core_web_md')
        nlp.add_pipe("textrank", last=True)
        doc = nlp(self.text)

        # examine the top-ranked phrases in the document
        # for p in doc._.phrases:
        #     print('{:.4f} {:5d}  {}'.format(p.rank, p.count, p.text))
        #     print(p.chunks)
        
        summary = ''                
        for sent in doc._.textrank.summary(limit_phrases=self.phrase_limit, limit_sentences=self.sentence_limit):
            summary += str(sent)
        return summary