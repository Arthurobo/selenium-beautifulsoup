import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import csv
import random

from my_beautiful_soup_functions import (get_product_title, get_product_price, 
                                         get_product_description, get_product_sizes, 
                                         get_product_images
                                        )

# Set up the Selenium web driver
driver = webdriver.Chrome()
driver.get("https://www.zara.com/uk/en/woman-shirts-l1217.html?v1=2184371")

# Wait for the dynamic content to load
time.sleep(3)

# Find the dynamic popup button with a class of "zds-button__lines-wrapper"
button = driver.find_element(By.CLASS_NAME, "geolocation-modal__button")

# Click the button to load the main page content
button.click()

# Wait for the dynamic main page content to load
time.sleep(3)


""" Beautiful soul beginning """
# Extract the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')


def get_links():
    empty_list_of_links = []

    link_tags = soup.find_all('a', class_='product-grid-product-info__name')

    for link in link_tags:
        href = link.get('href')
        empty_list_of_links.append(href)

    return empty_list_of_links

# Total scraped urls links
complete_urls = get_links()
print(complete_urls)

# Use this urls if you want to get only random 5 urls from the list of complete urls. This is becuase
# the total number of urls are much for testing purposes.
urls = random.sample(complete_urls, 5)
print(urls)


csv_filename = 'test.csv'

# Open the CSV file in append mode
with open(csv_filename, 'a', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    for url in urls:
        # Set up the Selenium web driver
        driver = webdriver.Chrome()
        driver.get(url)

        # Wait for the dynamic content to load
        time.sleep(3)

        # Find the dynamic popup button with a class of "zds-button__lines-wrapper"
        button = driver.find_element(By.CLASS_NAME, "geolocation-modal__button")

        # Click the button to load the main page content
        button.click()

        # Wait for the dynamic main page content to load
        time.sleep(3)

        """ Beautiful soup beginning """
        # Extract the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Calling functions
        product_title = get_product_title(soup)
        product_price = get_product_price(soup)
        product_description = get_product_description(soup)
        product_sizes = get_product_sizes(soup)
        product_image_links = get_product_images(soup)
        product_url = url

        # print(product_title)
        # print(product_price)
        # print(product_description)
        # print(product_sizes)

        file_object = [product_title, product_price, product_description, product_sizes, product_url, product_image_links]
        print(file_object)
        csv_writer.writerow(file_object)    

# Close the web driver
driver.quit()
