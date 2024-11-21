import pymupdf

try:
    doc = pymupdf.open("a.pdf")  # open a document
    out = open("output.txt", "wb")  # create a text output
    print("File opened successfully.")

    for page in doc:  # iterate the document pages
        text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
        out.write(text)  # write text of page
        out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
    out.close()
    print("Text extraction complete.")
except Exception as e:
    print("An error occurred:", e)
