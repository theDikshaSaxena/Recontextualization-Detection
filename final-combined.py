import requests
import json
from newspaper import Article

url = "https://api.newscatcherapi.com/v2/search"

querystring = {
    "q": "\"Ukraine\" AND \"Russia\"",
    "not_sources": "businessinsider.com,businessjournaldaily.com,businessreport.com",
    "lang": "en",
    "from": "13 days ago",
    "topic": "politics",
    "page": "1"
}

headers = {
    "x-api-key": "GN8nvzQj7XzIW1IP8OiS7GiaajXM2CCPT7CKDyp2YYg"
}

try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()

    response_data = json.loads(response.text)
    articles = response_data["articles"]

    article_data_list = []

    for article in articles:
        article_url = article["link"]
        article_data = {}

        try:
            # Create an Article object
            article_obj = Article(article_url, language="en")

            # Download the article
            article_obj.download()

            # Parse the article
            article_obj.parse()

            # Perform natural language processing (NLP)
            article_obj.nlp()

            # Extract the title
            article_data["title"] = article_obj.title

            # Extract the text
            article_data["text"] = article_obj.text

            # Extract the keywords
            article_data["keywords"] = article_obj.keywords

            # Extract the top image URL
            article_data["image"] = article_obj.top_image

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print("Skipped article due to 403 Forbidden error:", article_url)
            else:
                raise
        except Exception as e:
            print("Error occurred while processing article at", article_url)
            print("Error:", e)
            continue

        article_data_list.append(article_data)

    # Define the filename to write the article data
    filename = "/Users/dikshasaxena/Documents/2nd sem/Research-NLP- work/Web Scraping/imagesnewscatcherAPI-response-Ukraine_russia.json"

    # Write the article data to the file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(article_data_list, indent=4))

    print("Article data saved to", filename)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)
