from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Path to the ChromeDriver executable
driver_path = 'path/to/chromedriver'

# Create a ChromeOptions instance to disable browser notifications
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

# Create a ChromeDriver instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the page
url = 'https://edabit.com/challenge/v2eHXTn2qobw2WYJP'
driver.get(url)

# Wait for the necessary elements to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'grey-segment')))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'sub.header.no-highlight')))

# Get the HTML content after JavaScript rendering
html = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Extract the desired information
title = soup.find('h2', class_='content').text.strip()
tags = [tag.text for tag in soup.find_all('a', class_='ui label')]

# Find the description and extract the desired portion
scrapped_segment = soup.find('div', class_='grey-segment code-area instructions')

# scrapped_export = scrapped_segment.prettify()
# with open('scrap.html', 'w', encoding='utf-8') as file:
#     file.write(scrapped_export) 

#print(scrapped_segment)
description = ''
if scrapped_segment:
    description = scrapped_segment.find('p').text.strip()
    examples_header = soup.find('h3', text='Examples')
    if examples_header:
        description += examples_header.find_previous_sibling('p').text.strip()

examples = [pre.text.strip() for pre in soup.find_all('pre')]
notes = soup.find('div', class_='grey-segment code-area instructions').find_next_sibling('div').find('p')
notes_text = notes.text.strip() if notes else "No additional notes available."

# Format and print the extracted information
print(f"- Title:\n{title}")
print(f"- Tags:\n{tags}")
print(f"- Description:\n{description}")
print(f"- Examples:\n{examples}")
print(f"- Notes:\n{notes}")

# Close the browser
driver.quit()