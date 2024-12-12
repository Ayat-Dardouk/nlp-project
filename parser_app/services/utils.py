import re

def get_contact_info(doc):
    """Extract contact details (email, phone number) from the resume."""
    email = ""
    phone = ""
    
    for ent in doc.ents:
        if ent.label_ == "EMAIL":
            email = ent.text
        elif ent.label_ == "PHONE":
            phone = ent.text
    
    return {"email": email, "phone": phone}

def get_skills(doc):
    """Extract skills from the resume using AI model or predefined list."""
    skills = []
    predefined_skills = ["python", "java", "c++", "html", "css", "javascript", "data analysis", "machine learning"]  # Add more skills
    for ent in doc.ents:
        if ent.label_ == "SKILL":  # Custom label for skills (or use predefined skills)
            skills.append(ent.text.lower())
    
    # If no AI-based skills, use predefined list for matching
    for skill in predefined_skills:
        if skill.lower() in doc.text.lower():
            skills.append(skill)
    
    return list(set(skills))

def get_experience(doc):
    """Extract work experience (companies, positions, dates)"""
    # You can implement this using a custom logic based on resume structure
    experience = []
    for ent in doc.ents:
        if ent.label_ == "ORG":  # Extract organization names
            experience.append(ent.text)
    return experience

def get_education(doc):
    """Extract education information from the resume."""
    education = []
    for ent in doc.ents:
        if ent.label_ == "EDUCATION":  # Custom or based on keywords
            education.append(ent.text)
    return education
