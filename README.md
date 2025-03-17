# Selenium-Project
This project uses Selenium and BeautifulSoup to scrape laptop listings from Amazon India. First, Selenium initializes a Chrome browser instance to automate web browsing. A loop navigates through Amazon's search result pages (1 to 20) for the query "laptop," loading each page and identifying product listings based on a specific class name (`puis-card-container`). The HTML content of each listing is then saved as a separate file in a local directory.

Once all pages are scraped, BeautifulSoup is used to parse these HTML files. For each product, BeautifulSoup extracts essential details: the product title from the `h2` tag, a direct link by appending the product's partial URL to Amazon's base URL, and the price from a specific `span` tag containing pricing information. If a product's information is incomplete, the program catches the error and moves on without stopping.

Finally, the extracted data (title, price, and link) is stored in a pandas DataFrame and saved to a CSV file. This structured CSV file provides easy access to the scraped data, which can be used for further analysis or reporting. 
