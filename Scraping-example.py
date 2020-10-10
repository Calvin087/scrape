import requests #.get and .content
from bs4 import BeautifulSoup, SoupStrainer

url_base = "https://www.monster.co.uk/jobs/search/?q="
job_title = "QA-tester-python"
url_location = "&where="
location = "London"

new_url = f"{url_base}{job_title}{url_location}{location}"

page = requests.get(new_url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for postings in job_elems:
    title = postings.find('h2', class_='title')
    company = postings.find('div', class_='company')
    location = postings.find('div', class_='location')

    if None in (title, company, location):
        continue
 
    link = postings.find('a').get('href')
    # href = link.get('href')
    
    if link is None:
        continue

    print(title.text.strip())
    print(company.text.strip())
    print(f"View job post: {link}")
    print()

# I WANT TO CREATE A DICTIONARY OF DICTIONARIES
# https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/

# {
#     "data": {
#         "id": "1574083",
#         "username": "snoopdogg",
#         "full_name": "Snoop Dogg",
#         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
#         "bio": "This is my bio",
#         "website": "http://snoopdogg.com",
#         "counts": {
#             "media": 1320,
#             "follows": 420,
#             "followed_by": 3410
#         }
# }