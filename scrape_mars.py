from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_data ={}

    # Visit Nasa 
    n_url = "https://mars.nasa.gov/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the hemisphere dat
    # Store data in a dictionary
   
    # Close the browser after scraping
    browser.quit()

    # Return results
    return data
