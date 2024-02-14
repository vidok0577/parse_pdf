import PyPDF2
import re

with open('text.txt', 'w') as txt_file:

    with open('pdf.pdf', 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # print(pdf_reader.numPages)
        for page in range(40, 53): #  range(len(pdf_reader.pages)):
            # text = pdf_reader.pages[page].extract_text().split('\n')
            text = pdf_reader.pages[page].extract_text().replace('\n', '\n|')
            # text = '\n---------\n' + text
            txt = text.split('|')
            # print(text, '\n-----------')
            txt_file.write(re.sub(r'Page\s\d+\sof 442 J1939 –71 Database Report April 15, 2001', '', txt[0]).strip())
            txt_file.writelines(txt[1:])
            txt_file.write('\n')
