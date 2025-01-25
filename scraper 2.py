class ProductScraper:
    def __init__(self):
        self.session = requests.Session()

    def fetch_page(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response.text

    def get_product_price(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        price_tag = soup.find('span', class_='product-price')  # Adjust the selector as needed
        if price_tag:
            return price_tag.text.strip()
        return None