from bs4 import BeautifulSoup
import requests
import pandas as pd



# extract, transform, load processes

def extract(page):
    url = "https://www.freelancer.co.uk/jobs/"+ str(page) + "/?keyword=data%20science"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    #r.status_code
    return soup


def transform(soup):
    divs = soup.find_all('div', class_ = "JobSearchCard-primary")
    
    for item in divs:
        title = item.find('a', class_ = "JobSearchCard-primary-heading-link").text.strip()
        description = item.find('p', class_ = "JobSearchCard-primary-description").text.strip()
        price= item.find('div', class_ = "JobSearchCard-primary-price").text.strip()
        skills = item.find('div', class_ = "JobSearchCard-primary-tags")
        if skills:
            skills_link = item.find_all('a', href = True)
            for i in skills_link:
                skills_text = i.text.strip()
        
        jobs ={
            'Title': title,
            'Description': description,
            'Price': price,
            'Skills': skills_text
        }
        jobs_list.append(jobs)
    
    return

jobs_list =[]
for i in range(0,8):
    c = extract(0)
    transform(c)
    
df = pd.DataFrame(jobs_list)
df.to_csv('DataScience_jobs.csv')
    
           
    