import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = ["https://video.az/movie", 
        "https://video.az/movie?page=2", 
        "https://video.az/movie?page=3", 
        "https://video.az/movie?page=4"]

# Iterate through each URL
for url in urls:
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content of the page
        src = response.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(src, 'html.parser')

        # Find all <h1> tags on the page
        h1_tags = soup.find_all('h1', class_='h4 no-margin')

        # Check if any tags are found
        if h1_tags:
            # Extract and print the text content of each <h1> tag
            for h1_tag in h1_tags:
                title_text = h1_tag.get_text(strip=True)
                print(f" {title_text}")
        else:
            print(f"Couldn't find any <h1> tags with the specified class on {url}.")
    else:
        print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
