### Context for AI

bio = """
# CANDIDATE PROFILE FOR AI GENERATION

## 1. Personal Information


## 2. Professional Summary / About Me


## 3. Key Skills (Categorized)


## 4. Work Experience (Reverse Chronological Order)

## 5. Education and Training


## 6. Certifications


## 7. Publications


## 8. Networks and Memberships (CTF & Platforms)


## 9. Volunteering

## 10. Preferred Tone / Style (for AI's output)
* Professional, Action-oriented, Technical, Data-driven, Concise, Strong emphasis on quantifiable achievements.

"""

Instruction4Resume = """
## Specific Instructions / Focus for This Job Application
** Special Instruction for Penetration Testing or similar roles**:
* ** Resume Must Include the following sections: Work Exp, Certifications, Publications (Remove details), CTF Accomplishments

** Data Integrity:**
* **Truth Source:** The provided resume and application data are the **only truths**. Don't assume any additional skills or information.
* **Skill Gaps:** If a required skill is missing, assess if it's a minor variant of an existing skill. If so, indicate the candidate is "**open to learning**." Otherwise, consider the skill absent.

** HTML Resume Output:**
* **Direct PDF Conversion:** The output **must be valid HTML** ready for direct conversion to a PDF resume.
* **Professional Design:**
    * Use appropriate HTML tags for semantic structure.
    * Integrate CSS directly within the HTML (using `<style>` tags or `style` attributes).
    * Employ creative HTML and CSS to ensure a **professional and visually appealing resume layout**.
    * Fits within a page ideally or 2 at maximum.

** Bypass the ATS **
* ** The resume needs to be able to bypass all the ATS, doesnt mean we can lie on the resume and make sure that it is human readable.
"""
