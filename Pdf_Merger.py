from PyPDF2 import PdfMerger
merger = PdfMerger()

pdf_files = ['Samplefile_1.pdf', 'Samplefile_2.pdf']

for pdf_file in pdf_files:
        
        merger.append(pdf_file)
merger.write("combined.pdf")
merger.close()