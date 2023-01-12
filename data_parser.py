import time

import requests
from bs4 import BeautifulSoup

from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import URL, HEADERS


def translator(text, lang="uk", translator=Translator()):
    w = translator.translate(text, dest=lang)
    return w.text


def get_html(url, params=""):
    r = requests.get(url, headers=HEADERS, params=params)
    return r.text


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="vn-accordion__item")
    cards = {}
    for j, card in enumerate(items, start=1):
        my_list_cards = []
        title_card = card.find("span", class_="vn-accordion__title")
        blocks = card.find_all("a", class_="vn-nav__link")
        for block in blocks[2:]:
            data = {"title": block.text, "link": block["href"]}
            my_list_cards.append(data)
        cards[title_card.text] = my_list_cards
    return cards


html = get_html(URL)
IKEA_data = get_content(html)


def format_str_command_manu():
    command_manu = ""
    command_dict = {}
    for index, key in enumerate(IKEA_data.keys(), start=1):
        command_manu += f"/{index}" + f" - {key} \n"
        command_dict[f"/{index}"] = key
    return command_manu, command_dict, IKEA_data


def parser_items(test_data):
    link_from_data, title_from_data = test_data["link"], test_data["title"]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link_from_data + "?page=999")
    element = browser.find_element(By.CLASS_NAME, "plp-filter-information__total-count").text[18:]
    waiting_response = f"Wait about {int(((int(element) // 6.5) * 1.1 + 10) // 1)} seconds"
    print(waiting_response)
    time.sleep((int(element) // 6.5))
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="plp-product-list__fragment")
    data = []
    for i, item in enumerate(items, start=1):
        if item:
            title = item.find("span", class_="pip-header-section__title--small")
            data_title = title.text
            description = item.find("span", class_="pip-header-section__description-text")
            data_description = description.text
            price = item.find("span", class_="pip-price__integer")
            data_price = price.text
            photos = item.find_all("img", class_="pip-image")
            colect_item_data = [data_title, data_description, data_price]
            for photo in photos:
                colect_item_data.append(photo["src"])
            data.append(colect_item_data)
    return data, title_from_data
