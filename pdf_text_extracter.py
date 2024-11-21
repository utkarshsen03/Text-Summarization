import pymupdf

class Pdf2Text:
    def __init__(self,pdf):
        self.pdf = pdf
        
    def extract_text(self):
        try:
            doc = pymupdf.open(self.pdf)
            text = ""
            for page in doc:
                text += str(page.get_text().encode("utf8"))
        except Exception as e:
            return ("An error occurred:", e)
        return text

if __name__ == "__main__":
    pdf2text = Pdf2Text('offer_letter.pdf')
    print(type(pdf2text.extract_text()))