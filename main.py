import streamlit as st
from reportlab.pdfgen import canvas

def convert_to_pdf(text):
    pdf = canvas.Canvas("converted.pdf")
    pdf.setFont("Helvetica", 12)
    lines = text.split("\n")
    y = 720
    for line in lines:
        pdf.drawString(50, y, line)
        y -= 15
    pdf.save()

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
