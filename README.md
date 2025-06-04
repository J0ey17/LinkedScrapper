# LinkedIn Scrapper and AI Resume Maker

Scrapes job postings from LinkedIn for a specified designation and generates tailored resumes using AI.

## Features

* Fetches job listings from LinkedIn based on a defined role and location.
* Extracts detailed information for each job posting (Title, Company, Location, Description, etc.).
* Generates resumes tailored to each job description using the Gemini AI API.
* Outputs resumes in HTML and PDF format.

## Requirements

* Python 3.x
* `requests`
* `beautifulsoup4`
* `google-generativeai`
* `playwright`
* A `context.py` file containing your `bio` and `Instruction4Resume`.
* Chromium browser for Playwright (`playwright install chromium`)

## Setup

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4 google-generativeai playwright
    playwright install chromium
    ```
3.  **API Key:**
    Replace `GEMINI_API` in the script with your actual Gemini API Key or set it as an environment variable.
    ```python
    GemAPI_Key = r'YOUR_GEMINI_API_KEY'
    ```
4.  **Designation:**
    Modify the `designation` variable in the script to your desired job title (use `%2b` for spaces).
    ```python
    designation = r"Your%2bJob%2bTitle"
    ```
5.  **Context File:**
    Create a `context.py` file in the same directory with the following variables:
    ```python
    # context.py
    bio = """
    --- Your Professional Bio Here ---
    e.g.,
    Highly motivated and results-oriented Penetration Tester with X years of experience in...
    """

    Instruction4Resume = """
    --- Instructions for the AI Resume Generation ---
    e.g.,
    Focus on skills relevant to the job description.
    Use a professional tone.
    Highlight achievements with quantifiable results.
    The resume should include sections like: Contact Information, Summary, Experience, Education, Skills, Certifications.
    Ensure the contact information includes: [Your Name], [Your Phone], [Your Email], [Your LinkedIn Profile URL].
    """
    ```

## Usage

Run the script from your terminal:

```bash
python your_script_name.py
