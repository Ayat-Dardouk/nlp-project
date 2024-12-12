import spacy
import pandas as pd
import io
import fitz  # PyMuPDF
from .utils import get_contact_info, get_skills, get_experience, get_education

# Load the SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file using PyMuPDF (fitz).
    
    :param file: A file-like object (e.g., uploaded file)
    :return: Text extracted from the PDF
    """
    # Open the file object with PyMuPDF
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    
    # Initialize an empty string to store extracted text
    text = ""
    
    # Iterate over all pages in the PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)  # Load page by page number
        text += page.get_text("text")  # Extract text from the page
    
    # Close the PDF document after extraction
    pdf_document.close()
    
    return text


def parse_resume(resume_text):
    """Extract relevant details using AI-powered parsing."""
    doc = nlp(resume_text)
    
    # Extract contact info (email, phone, etc.)
    contact_info = get_contact_info(doc)
    
    # Extract skills (using a predefined list or via AI model)
    skills = get_skills(doc)
    
    # Extract work experience
    experience = get_experience(doc)
    
    # Extract education
    education = get_education(doc)
    
    return {
        "contact_info": contact_info,
        "skills": skills,
        "experience": experience,
        "education": education
    }

def save_to_excel(parsed_data, filename="parsed_resume.xlsx"):
    """Convert parsed data to Excel and save."""
    # Create a DataFrame from parsed data
    df = pd.DataFrame([parsed_data])  # Wrap parsed_data in a list for row compatibility
    
    # Save to Excel
    df.to_excel(filename, index=False, engine='openpyxl')
    
    return filename
