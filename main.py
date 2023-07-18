import streamlit as st
from pdfdocument import PDFDocument

def convert_to_pdf(text):
    pdf = PDFDocument("converted.pdf")
    pdf.init_report()
    pdf.h1("Converted PDF")
    pdf.text(text)
    pdf.generate()

def main():
    st.title("Text to PDF Converter")

    # File upload section
    st.header("Upload Text File")
    file = st.file_uploader("Choose a text file", type=["txt"])
    
    if file is not None:
        file_contents = file.read().decode("utf-8")
        
        # Convert text to PDF
        convert_to_pdf(file_contents)

        # Download link
        st.download_button(
            label="Download PDF",
            data=open("converted.pdf", "rb").read(),
            file_name="converted.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
