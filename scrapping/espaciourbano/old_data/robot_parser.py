import urllib.robotparser

# Create a RobotFileParser object
rp = urllib.robotparser.RobotFileParser()

# Set the URL of the robots.txt file
robots_txt_url = 'https://www.espaciourbano.com/robots.txt'

# Read and parse the robots.txt file
rp.set_url(robots_txt_url)
rp.read()

# Check if scraping is allowed for a specific URL
url_to_scrape = 'https://www.espaciourbano.com'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Arc/1.0 (Educational Scraper)'

if rp.can_fetch(user_agent, url_to_scrape):
    print("You can scrap")
else:
    print("You cannot scrap")