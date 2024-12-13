import re
import spacy
print(spacy.__version__)


def get_contact_info(doc):
    """Extract contact information like email and phone."""
    contact_info = {"email": None, "phone": None}
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_regex = r'\+?\d{10,15}'

    contact_info["email"] = re.search(email_regex, doc.text)
    contact_info["phone"] = re.search(phone_regex, doc.text)

    return contact_info

def get_skills(doc):
    """Match predefined skills from the text."""
    skills_set = {"python", "java", "html", "css", "javascript", "sql", "machine learning", "c++"}
    skills = [skill for skill in skills_set if skill in doc.text.lower()]
    return skills

def get_experience(doc):
    """Extract work experience sections."""
    experience = []
    for sent in doc.sents:
        if "years of experience" in sent.text.lower():
            experience.append(sent.text)
    return experience

def get_education(doc):
    """Extract education-related details."""
    education_keywords = ["university", "college", "bachelor", "master", "phd", "diploma"]
    education = [sent.text for sent in doc.sents if any(keyword in sent.text.lower() for keyword in education_keywords)]
    return education

def get_gender(doc):
    """Guess gender from explicit mentions or name."""
    gender = "Not specified"
    male_keywords = ["he", "him", "mr."]
    female_keywords = ["she", "her", "ms.", "mrs."]

    if any(word in doc.text.lower() for word in male_keywords):
        gender = "Male"
    elif any(word in doc.text.lower() for word in female_keywords):
        gender = "Female"
    
    return gender

def get_age(doc):
    """Extract age or estimate based on years."""
    for ent in doc.ents:
        if ent.label_ == "DATE" and re.match(r'\d{4}', ent.text):
            year = int(ent.text)
            return 2024 - year
    return "Not specified"

def get_summary(doc):
    """Extract the summary section of the resume."""
    for sent in doc.sents:
        if "summary" in sent.text.lower() or "objective" in sent.text.lower():
            return sent.text
    return "Not specified"

def get_sector_name(doc):
    """Extract industry sectors."""
    sectors = ["IT", "Education", "Healthcare", "Marketing", "Finance"]
    sector_names = [sector for sector in sectors if sector.lower() in doc.text.lower()]
    return sector_names or ["Not specified"]

def get_experience_level(doc):
    """Infer experience level from text."""
    levels = {"junior", "mid", "senior", "lead", "manager"}
    experience_level = [level for level in levels if level in doc.text.lower()]
    return experience_level or ["Not specified"]


def get_qualification(doc):
    """Extract qualifications from the text."""
    qualifications_keywords = [
        "bachelor's", "master's", "phd", "associate", "diploma",
        "degree", "certification", "certified", "course", "training"
    ]
    qualifications = [
        sent.text for sent in doc.sents
        if any(keyword in sent.text.lower() for keyword in qualifications_keywords)
    ]
    return qualifications
