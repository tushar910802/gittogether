import time
from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_website(url):
    # Set up the Selenium WebDriver (make sure to have ChromeDriver installed)
    driver = webdriver.Chrome()
    
    # Open the URL
    driver.get(url)
    
    # Wait for the JavaScript to render (adjust the sleep time as needed)
    time.sleep(5)
    
    # Get the page source after JavaScript has rendered
    page_source = driver.page_source
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Extract and print the title of the page
    title = soup.title.string
    print(f"Title of the page: {title}")
    
    # Find all product elements
    products = soup.find_all('li', class_='wizzy-result-product')
    
    for product in products:
        # Extract product name
        name = product.find('p', class_='product-item-title').text.strip()
        
        # Extract product price
        price = product.find('div', class_='wizzy-product-item-price').text.strip()
        
        # Print the extracted values
        print(f"Product Name: {name}")
        print(f"Price: {price}")
        print('-' * 20)
    
    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    url = "https://www.westside.com/collections/beauty"
    scrape_website(url)
