# LinkedIn Scrapper and AI Resume Maker

Scrapes job postings from LinkedIn for a specified designation and location, then generates tailored resumes using AI.

## Features

* Fetches job listings from LinkedIn based on a defined role, location (currently set to United Kingdom), and time posted.
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
4.  **Configuration Variables:**
    Modify these variables at the top of the script:
    * `designation`: Set your desired job title (use `%2b` for spaces).
        ```python
        designation = r"Your%2bJob%2bTitle"
        ```
    * `dur_seconds`: Set the time frame for job postings to fetch, in seconds (e.g., '3600' for last 1 hour, '86400' for last 24 hours).
        ```python
        dur_seconds = r'3600' # Fetches jobs posted in the last 1 hour
        ```
    * The `job_listing_url` is currently configured to search for jobs in the "United Kingdom". You can modify the `geoId` or location parameters in the URL directly if needed.

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
```

The script will:
1.  Fetch job IDs from LinkedIn based on your configuration.
2.  For each job ID, fetch the job details.
3.  Generate an HTML resume using Gemini AI based on your bio and the job description.
4.  Convert the HTML resume to a PDF.
5.  HTML and PDF files will be saved in the script's directory, named as `{JID}_{JobTitle}_Resume.html` and `{JID}_{JobTitle}_Resume.pdf`.

**Note:** Web scraping can be fragile and subject to changes in website structure. This script was last confirmed working on 28th May 2025.
