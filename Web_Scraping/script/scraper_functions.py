import requests
from bs4 import BeautifulSoup
import random
import time
from itertools import chain
from script.custom_decorators import timer

## ----- Global Constants

URL = "https://www.boulanger.com/c/nav-filtre/smartphone-telephone-portable?_etat_produit~neuf"
URL_INIT = "https://www.boulanger.com"


def create_session() -> requests.Session:
    """`create_session`: Create a requests session with a custom header to make the server believe the scraper is actually a browser opened by a real user.

    `Returns`
    --------- ::

        requests.Session

    `Example(s)`
    ---------

    >>> create_session()
    ... <requests.sessions.Session at 0x223e7834df0>"""
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
    )
    return session


def random_timer() -> None:
    random_delay = random.uniform(0.1, 2)
    return time.sleep(random_delay)


def create_url_list(URL: str, nb_page: int) -> list[str]:
    """`create_url_list`: Generate a URL list of new and unused smartphones from the Boulanger website (https://www.boulanger.com/).

    ---------
    `Parameters`
    --------- ::

        URL (str): # a URL for new products from Boulanger.
        nb_page (int): # Should be 18-19 (to verify.)

    `Returns`
    --------- ::

        list[str]

    `Example(s)`
    ---------

    >>> create_url_list()
    ... #_test_return_"""
    url_list = list()
    url_list.append(URL)

    for index_page in range(2, nb_page):
        page_url = f"{URL}&numPage={index_page}"
        url_list.append(page_url)
    return url_list


@timer
def read_pages(url_list: list[str], session: requests.Session) -> list[str]:
    list_pages = list()
    for page_number, url in enumerate(url_list):
        random_timer()
        response = session.get(url)
        content = response.text
        list_pages.append(content)
        if response.status_code == 200:
            print(f"Page {page_number+1} -> Successfull Extraction.")
        else:
            print(f"Page {page_number+1} -> Unsuccessfull Extraction.")
    return list_pages


@timer
def extract_all_urls(pages: list[str]) -> list[str]:
    """TODO: Voir si il existe une implémentation + rapide avec un array numpy."""
    links_list = list()
    for page in pages:
        soup = BeautifulSoup(page, "html.parser")
        links = soup.find_all("a", attrs={"class": "product-list__product-image-link"})
        links_list.append(links)
    link_matches = list(chain.from_iterable(links_list))
    all_urls = [URL_INIT + link.get("href") for link in link_matches]
    random.shuffle(all_urls)  # mélange aléatoire
    return all_urls


@timer
def extract_all_pages(all_urls: list[str], session: requests.Session) -> list[str]:
    product_pages = list()
    for product_number, url in enumerate(all_urls):
        random_timer()
        response = session.get(url)
        content_page = response.text
        product_pages.append(content_page)
        if response.status_code == 200:
            print(f"Product {product_number+1} -> Successfull Extraction.")
        else:
            print(f"Product {product_number+1} -> Unsuccessfull Extraction.")
    return product_pages
