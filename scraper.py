import requests
from bs4 import BeautifulSoup

# Target news website (you can change this)
url = "https://www.bbc.com/news"

# Set headers to act like a browser (avoids blocks)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    # Fetch the HTML content
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise exception for bad status

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <h2> tags (commonly used for headlines)
    headlines = soup.find_all("h2")

    # Extract text from each tag
    titles = [tag.get_text(strip=True) for tag in headlines if tag.get_text(strip=True)]

    # Save to a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, title in enumerate(titles, 1):
            file.write(f"{i}. {title}\n")

    print("✅ Headlines saved successfully to 'headlines.txt'.")

except Exception as e:
    print("❌ An error occurred:", e)
