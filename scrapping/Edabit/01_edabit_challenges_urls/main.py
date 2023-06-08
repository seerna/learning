from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# Path to the ChromeDriver executable
driver_path = 'path/to/chromedriver'

# Create a ChromeOptions instance to disable browser notifications
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

# Create a ChromeDriver instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the page
url = 'https://edabit.com/challenges'
driver.get(url)

# Wait for the page to load
time.sleep(3)


dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ui fluid selection dropdown']")))

# Click on the dropdown to expand it
dropdown.click()

# Locate the "Python" option within the dropdown and click on it
python_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option' and span[text()='Python']]")))
python_option.click()

time.sleep(3)

dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@style='margin-top: -2px;']")))
dropdown.click()
difficulty_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option' and span[text()='Very Easy']]")))
difficulty_option.click()

time.sleep(3)

# Scroll down to load more content
while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        # Wait for the "LOAD MORE" button to be clickable
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ui fluid button' and span='LOAD MORE']"))
        )

        # Click the "LOAD MORE" button
        load_more_button.click()

    except Exception:
        # If TimeoutException occurs, print a message and break the loop to continue the algorithm
        print("Load more button not found. Exiting the loop.")
        break

# Get the HTML content after JavaScript rendering
html = driver.page_source
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(html)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all the challenge URLs for Python challenges
challenge_urls = []
for item in soup.find_all('div', class_='item no-highlight'):
    link = item.find('a', href=True)
    if link:
        challenge_urls.append('https://edabit.com' + link['href'])

# Print the scraped challenge URLs
with open('URLs.txt', 'w', encoding='utf-8') as file:
    for url in challenge_urls:
        file.write(url + "\n")
print(challenge_urls)

# Close the browser
driver.quit()
