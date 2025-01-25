# # Web Scraping Exercises 
# 
# # Import Libraries
import requests
import bs4

# Use http://quotes.toscrape.com/ and get the HMTL text from the homepage to start scraping.

res = requests.get('http://quotes.toscrape.com/')

soup = bs4.BeautifulSoup(res.text, 'lxml')

soup

# Pull out the Authors
soup.select('.author')

authors = set() 

for name in soup.select(".author"):
    authors.add(name.text)

authors

# Create a list of all the quotes on the first page.

quotes = soup.select('.text')

quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)

quotes

# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page.

tags = soup.select('.tag-item')

tags

for item in soup.select(".tag-item"):
    print(item.text)

# Since there is more than one page, use a loop to get all the authors from the web page.

# Set URL.

url = 'http://quotes.toscrape.com/page/'

# Loop through all the pages to get all the authors.

authors = set()

for page in range(1,10):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

# end


