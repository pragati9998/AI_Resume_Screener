import os
import pdfplumber

def save_uploaded_file(uploaded_file, folder):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

def extract_text_from_pdf_or_txt(file_path):
    if file_path.lower().endswith('.pdf'):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
    elif file_path.lower().endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return ""

def load_job_description(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_skills(text, skill_keywords):
    found = [skill for skill in skill_keywords if skill.lower() in text.lower()]
    return found

def load_all_resumes(folder):
    # Load resumes as dict with text & filename
    resumes = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        text = extract_text_from_pdf_or_txt(path)
        if text:
            resumes.append({"filename": file, "text": text})
    return resumes
