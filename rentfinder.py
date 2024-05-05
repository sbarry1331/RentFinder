from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/Zillow-Clone/"

class RentFinder():

    def __init__(self):
        self.response = requests.get(URL)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def get_prices(self):
        price_list = self.soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        prices = [f'{price.text[:6]}' for price in price_list]
        return prices

    def get_links(self):
        link_list = self.soup.find_all('a', class_="property-card-link")
        links = [f'{link['href']}' for link in link_list]
        return links

    def get_addresses(self):
        addr_list = self.soup.find_all('address')
        addrs = [f"{addr.text.strip().replace('|', '')}" for addr in addr_list]
        return addrs