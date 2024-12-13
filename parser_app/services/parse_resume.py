import spacy
import pandas as pd
import io
import fitz  # PyMuPDF
from .utils import get_contact_info, get_skills, get_experience, get_education, get_gender, get_age, get_summary, get_qualification, get_sector_name, get_experience_level

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
    
    # Extract skills
    skills = get_skills(doc)
    
    # Extract work experience
    experience = get_experience(doc)
    
    # Extract education
    education = get_education(doc)
    
    # Extract gender (based on common NLP heuristics or predefined keywords)
    gender = get_gender(doc)
    
    # Extract age (inferred based on dates or context)
    age = get_age(doc)
    
    # Extract resume summary
    summary = get_summary(doc)
    
    # Extract qualifications (based on title and experience)
    qualifications = get_qualification(doc)
    
    # Extract sector name (industry or field)
    sector_name = get_sector_name(doc)
    
    # Extract experience level (junior, mid-level, senior)
    experience_level = get_experience_level(doc)
    
    return {
        "contact_info": contact_info,
        "skills": skills,
        "experience": experience,
        "education": education,
        "gender": gender,
        "age": age,
        "summary": summary,
        "qualifications": qualifications,
        "sector_name": sector_name,
        "experience_level": experience_level,
    }


def save_to_excel(parsed_data, filename="parsed_resume.xlsx"):
    """Convert parsed data to a structured format and save."""
    structured_data = {
        "Contact Info": [parsed_data.get("contact_info", {})],
        "Skills": [", ".join(parsed_data.get("skills", []))],
        "Experience": ["; ".join(parsed_data.get("experience", []))],
        "Education": ["; ".join(parsed_data.get("education", []))],
        "Gender": [parsed_data.get("gender", "Not specified")],
        "Age": [parsed_data.get("age", "Not specified")],
        "Summary": [parsed_data.get("summary", "Not specified")],
        "Qualifications": [", ".join(parsed_data.get("qualifications", []))],
        "Sector Name": [", ".join(parsed_data.get("sector_name", []))],
        "Experience Level": [", ".join(parsed_data.get("experience_level", []))]
    }
    df = pd.DataFrame(structured_data)
    df.to_excel(filename, index=False, engine='openpyxl')
    return filename
