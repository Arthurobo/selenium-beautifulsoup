import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from my_beautiful_soup_functions import get_product_title, get_product_price, get_product_description, get_product_sizes

# Set up the Selenium web driver
driver = webdriver.Chrome()
# driver.get("https://www.zara.com/uk/en/printed-ruffled-shirt-p03488246.html?v1=259639138&v2=2184371")
driver.get("https://www.zara.com/uk/en/asymmetric-linen-shirt-p04786117.html?v1=271289127&v2=2184357")
# driver.get("https://www.zara.com/uk/en/woman-shirts-l1217.html?v1=2184371")

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




def get_product_title(soup):
    # Find the first h1 element with a class of "product-detail-info__header-name"
    product_name = soup.find('h1', class_='product-detail-info__header-name')

    # Extract the text content of the element
    product_name_text = product_name.text.strip()
    return product_name_text

def get_product_price(soup):
    # Find the first h1 element with a class of "product-detail-info__header-name"
    product_price = soup.find('span', class_='money-amount__main')

    # Extract the text content of the element
    product_price_text = product_price.text.strip()
    return product_price_text

def get_product_description(soup):
    # Find all the 'div' tags with the certain class
    div_tags = soup.find_all('div', class_='expandable-text__inner-content')

    # Initiate an empty list
    empty_span_list = []

    # Append all description in the div_tags objects in the empty list
    for div_tag in div_tags:
        empty_span_list.append(div_tag)

    # Get the second div from the empty_span_list object
    second_div = empty_span_list[1]

    # Find the p tag
    description_tags = second_div.find('p')
    p_tag = description_tags.text.strip()

    return p_tag


def get_product_sizes(soup):
    # Find the 'span' tag(s)
    span_tags = soup.find_all('span', class_='product-size-info__main-label')

    # Initiate an empty list
    empty_span_list = []

    # Append all sizes in the span objects in the empty list
    for span in span_tags:
        span = span.text.strip()
        empty_span_list.append(span)

    return empty_span_list


# Print the product name
print(get_links())
print(get_product_title(soup))
print(get_product_price(soup))
print(get_product_description(soup))
print(get_product_sizes(soup))

# Close the web driver
driver.quit()
