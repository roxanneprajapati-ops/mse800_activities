"""
CV Analyzer: extracts text from PDF/DOCX and asks Google Gemini for CV feedback.
"""
import os
import re
import sys

import pdfplumber
import docx
from google import genai

# Code reference: https://ai.google.dev/gemini-api/docs
# removed api key intentionally in git
API_KEY = ""
client = genai.Client(api_key=API_KEY)

PROMPT_TEMPLATE = """
You are a professional AI recruiter and career advisor with expertise in IT, Software Engineering, Data Analytics, and Computer Science.

Instructions:
1. Analyze the candidate’s CV provided below.
2. Break down their experience into relevant fields (e.g., Software Engineering, Data Science, Business, Finance).
3. Identify the two strongest areas of expertise for this candidate.
4. Suggest 2–3 job roles that best fit the candidate's profile.
5. Provide 3 actionable recommendations to improve the CV, focusing on clarity, impact, and keyword optimization for applicant tracking systems (ATS).
6. Keep your response concise, professional, and easy to understand. Use bullet points or numbered lists.

CV Text:
{cv_text}
"""

def extract_text_from_pdf(pdf_path: str)-> str:
    """Extract and return all text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            text += (page_text or "") + "\n"
    return text.strip()


def extract_text_from_docx(docx_path: str) -> str:
    """Extracts text from a DOCX file."""
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def analyze_cv(cv_text: str) -> str:
    """Send CV text to Gemini and return the analysis result as plain text."""
    prompt = PROMPT_TEMPLATE.format(cv_text=cv_text)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text

def clean_markdown(text: str) -> str:
    """Remove simple markdown formatting from the model output."""
    # Convert * bullets to -
    text = re.sub(r'^\s*\*\s+', '- ', text, flags=re.MULTILINE)

    # Remove bold (**text**)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)

    # Remove extra spaces after dash
    text = re.sub(r'-\s+', '- ', text)

    return text.strip()

def main() -> int:
    """Run the CV analysis workflow and print results."""
    file_path = input("Enter CV file path (PDF/DOCX): ").strip()

    if not os.path.exists(file_path):
        print("File not found!")
        return 1

    # Extract text based on file type
    if file_path.endswith(".pdf"):
        cv_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        cv_text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format!")
        return 1

    print("\nAnalyzing CV with Google Gemini...\n\n ", cv_text,"\n\n")
    analysis_result = analyze_cv(cv_text)

    cleaned_result = clean_markdown(analysis_result)

    # print("\n--- CV Analysis Results ---\n")
    # print(analysis_result)

    print("\n" + "=" * 60)
    print("           CV ANALYSIS RESULTS")
    print("=" * 60 + "\n")

    print(cleaned_result)
    print("\n" + "=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
