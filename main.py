import streamlit as st
from fpdf import FPDF
import os

def convert_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=text)
    return pdf

def save_uploaded_file(file):
    file_path = os.path.join("uploads", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

def main():
    st.title("Text to PDF Converter")

    # File upload section
    st.header("Upload Text File")
    file = st.file_uploader("Choose a text file", type=["txt"])
    
    if file is not None:
        file_path = save_uploaded_file(file)
        file_contents = open(file_path, "r").read()
        
        # Convert text to PDF
        pdf = convert_to_pdf(file_contents)

        # Download link
        st.download_button(
            label="Download PDF",
            data=pdf.output(dest="S").encode("latin-1"),
            file_name="converted.pdf",
            mime="application/pdf"
        )
        
        # Display default file path
        st.write("Default File Path:", file_path)

if __name__ == "__main__":
    main()
