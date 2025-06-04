#     _    ___                   __   ______ 
#    (_)  / _ \                 /_ | |____  |
#     _  | | | |   ___   _   _   | |     / / 
#    | | | | | |  / _ \ | | | |  | |    / /  
#    | | | |_| | |  __/ | |_| |  | |   / /   
#    | |  \___/   \___|  \__, |  |_|  /_/    
#   _/ |                  __/ |              
#  |__/                  |___/               
## LinkedIn Scrapper and AI resume maker
## Works: 28th May 2025

import requests
import re
import os
from bs4 import BeautifulSoup as bs
import json
from context import *
from google import genai
from playwright.sync_api import sync_playwright

### RegEx
pattern = r"jobPosting:(\d+)"

### Varaibles and API Key
designation = r"Penetration%2bTester"
GemAPI_Key = r'GEMINI_API'
dur_seconds = r'3600'        # In Seconds, Right now set to fetch all the jobs posted in the last 1 hour

#### URLs
job_listing_url = rf"https://www.linkedin.com/jobs/api/seeMoreJobPostings/search?keywords={designation}&location=United%2BKingdom&geoId=101165590&f_TPR=r{dur_seconds}&start=1"
job_posting_url = r"https://www.linkedin.com/jobs/api/jobPosting/"

####### Methods
### Fetching a url page
def getPage(url):
    try:
        response = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
    except Exception as e:
        print(e)
    if response.status_code == 200:
        return response.text
    else:
        return f"Response Code: {response.status_code}"

### Fetching the Job IDs
def fetchJobIDs():
    job_ids = re.findall(pattern, getPage(job_listing_url))
    return job_ids

### Fetching Job Description
def fetchJD(jid):
    job_holder = dict()

    response = getPage(job_posting_url + jid)
    
    job_page = bs(response, 'html.parser')

    try:
        job_title = job_page.find('h2', class_='top-card-layout__title')
        job_company = job_page.find('a', class_='topcard__org-name-link')
        job_location = job_page.find('span', class_='topcard__flavor topcard__flavor--bullet')
        job_age = job_page.find('span', class_='posted-time-ago__text')
        job_applicants = job_page.find('figcaption', class_='num-applicants__caption') #Not always present
        job_description = job_page.find('div', class_='decorated-job-posting__details')
        job_link = job_page.find('a', class_='topcard__link')

        
        ## Storing Job Description in a Dictionary
        job_holder['JID'] = jid                                  #ID Works
        job_holder['Title'] = job_title.get_text().strip()              #Works
        job_holder['Company'] = job_company.get_text().strip()      #Works, not always
        job_holder['Location'] = job_location.get_text().strip()    #Works
        job_holder['Posted On'] = job_age.get_text().strip()        #Works
        job_holder['Link'] = job_link['href']                       #Works
        job_holder['Description'] = job_description.get_text().strip()  #Works

        # Job Applicants can be empty
        if job_applicants is None:
            job_applicants = 'Not Available'
            job_holder['Applicants'] = job_applicants
        else:
            job_holder['Applicants'] = job_applicants.get_text().strip()

        return job_holder

    except Exception as e:
        print(e)

### Collected Jobs in a list as dict objects
def all_jobs_collect():
    jids = fetchJobIDs()
    print(jids)
    all_jobs_holder = []

    for j in jids:
        current_job_info = fetchJD(j)
        all_jobs_holder.append(current_job_info)
    
    return all_jobs_holder

### Job Collection to JSON
def collected_to_json():
    jobs_data = all_jobs_collect()

    json_jobs_data = json.dumps(jobs_data, indent=2)
    return json_jobs_data

### html to pdf genertation
def htmltopdf(htmlfilename, pdffilename):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto(f'file:///{htmlfilename}')
        page.pdf(path=pdffilename, format='Legal', margin={'top':'20px', 'bottom':'20px'}, print_background=True, prefer_css_page_size=True)
        browser.close()
        print(f"PDF Generated: {pdffilename}")

### Gemini AI integration
def AIResume():
    all_jobs_list = all_jobs_collect()

    StartDel = '```html'
    EndDel = '```'

    pattern_html = re.compile(rf"^{StartDel}\n(.*)\n^{EndDel}$", re.DOTALL | re.MULTILINE)

    for job in all_jobs_list:
        client = genai.Client(api_key=GemAPI_Key)
        ai_resp = client.models.generate_content(
            model="gemini-1.5-pro", contents = f"Create a Ready-to-submit resume with all sections completely generated, using the given condidate bio for the provided job using the provided specific instructions: \r\n here is the candidate Bio: {bio} \r\n here is the Job Description: {job} \r\n\r\n Here are the specific instructions: {Instruction4Resume}"
        )

        extracted_html_resume = pattern_html.search(ai_resp.text)
        html_resume = extracted_html_resume.group(1).strip()

        name = f"{job['JID']}_{job['Title']}_Resume"
        pdfname = name + '.pdf'
        htmlname = name + '.html'

        with open(htmlname, 'wb') as file:
            file.write(html_resume.encode("utf-8"))
            print("HTML Created")

        htmltopdf(htmlname,pdfname)

### Main
AIResume()
