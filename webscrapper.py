import requests
from bs4 import BeautifulSoup

# URL you want to scrape
url = "https://www.bbc.com/news"

# Send a GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline elements
    headlines = soup.find_all("h2")

    print("Top Headlines:")
    print("----------------------")
    for h in headlines:
        text = h.get_text(strip=True)
        if text:
            print("-", text)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
