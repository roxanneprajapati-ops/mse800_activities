import os
import argparse
import re
import sys

import pdfplumber
import docx
from google import genai

PROMPT_TEMPLATE = """
You are a professional AI recruiter and career advisor with expertise in IT, Software Engineering, Data Analytics, and Computer Science.

Instructions:
1. Analyze the candidate's CV provided below.
2. Break down their experience into relevant fields (e.g., Software Engineering, Data Science, Business, Finance).
3. Identify the two strongest areas of expertise for this candidate.
4. Suggest 2-3 job roles that best fit the candidate's profile.
5. Provide 3 actionable recommendations to improve the CV, focusing on clarity, impact, and keyword optimization for applicant tracking systems (ATS).
6. Keep your response concise, professional, and easy to understand. Use bullet points or numbered lists.

CV Text:
{cv_text}
""".strip()


def extract_text_from_pdf(file_path: str) -> str:
    text_parts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)
    return "\n".join(text_parts).strip()


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs]).strip()


def clean_markdown(text: str) -> str:
    # Convert * bullets to -
    text = re.sub(r'^\s*\*\s+', '- ', text, flags=re.MULTILINE)
    # Remove bold (**text**)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    # Normalize dash spacing
    text = re.sub(r'-\s+', '- ', text)
    return text.strip()


def get_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Missing GOOGLE_API_KEY environment variable.")
    return genai.Client(api_key=api_key)


def analyze_cv(cv_text: str) -> str:
    client = get_client()
    prompt = PROMPT_TEMPLATE.format(cv_text=cv_text)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    # Some SDKs return text in different places; this is the common one.
    return getattr(response, "text", str(response))


def load_cv_text(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    lower = file_path.lower()
    if lower.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    if lower.endswith(".docx"):
        return extract_text_from_docx(file_path)

    raise ValueError("Unsupported file format. Use .pdf or .docx")


def main():
    parser = argparse.ArgumentParser(description="AI-Powered CV Analyzer (Gemini API)")
    parser.add_argument("--file", help="Path to CV file (PDF/DOCX)")
    parser.add_argument("--out", help="Optional output file path (saves cleaned result)")
    args = parser.parse_args()

    # Interactive input if --file not provided
    file_path = args.file
    if not file_path:
        file_path = input("Enter CV file path (PDF/DOCX): ").strip()

    try:
        cv_text = load_cv_text(file_path)
        analysis_result = analyze_cv(cv_text)
        cleaned = clean_markdown(analysis_result)

        print("\n" + "=" * 60)
        print("           CV ANALYSIS RESULTS")
        print("=" * 60 + "\n")
        print(cleaned)
        print("\n" + "=" * 60)

        if args.out:
            os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(cleaned + "\n")
            print(f"\nSaved results to: {args.out}")

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
