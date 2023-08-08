
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=flutter"

# قائمة لتخزين البيانات
job_data_list = []

for page_number in range(1, 5):
    print("------", page_number, "------")
    try:
        page_url = base_url + "&page=" + str(page_number)
        client = urlopen(page_url)
    except Exception as e:
        print("Error:", e)
        continue

    page_html = client.read()
    client.close()
    page_soup = BeautifulSoup(page_html, "html.parser")
    job_containers = page_soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
    
    for job_container in job_containers:
        print("Job Number", page_number)

        job_title = job_container.find("h2", {"class": "css-m604qf"})
        company_name = job_container.find("a", {"class": "css-17s97q8"})
        location = job_container.find("span", {"class": "css-5wys0k"})
        job_type = job_container.find("div", {"class": "css-1lh32fc"})
        skills = job_container.find("div", {"class": "css-y4udm8"})

        if job_title and company_name and location and job_type and skills:
            job_data_list.append({
                "Job Title": job_title.text.strip(),
                "Company Name": company_name.text.strip(),
                "Location Job": location.text.strip(),
                "Job Type": job_type.text.strip(),
                "Skills": skills.text.strip()
            })

# إنشاء DataFrame من قائمة البيانات وحفظه في ملف CSV
job_data_df = pd.DataFrame(job_data_list)
job_data_df.to_csv("flutter_job_data.csv", index=False, encoding="utf-8")