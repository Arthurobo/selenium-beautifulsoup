import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


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


def get_product_images(soup):
    img_tags = soup.find_all('img', class_='media-image__image media__wrapper--media')

    # Initiate an empty list
    empty_img_list = []

    for img in img_tags:
        href_links = img.get('src')
        empty_img_list.append(href_links)
    first_two_images = empty_img_list[:2]
    return first_two_images