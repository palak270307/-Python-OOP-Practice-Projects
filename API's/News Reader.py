import requests


class Article:
    def __init__(self, title, description, author, url):
        self.title = title
        self.description = description
        self.author = author
        self.url = url

    def display(self):
        print("\n" + "-" * 50)
        print(f"Title       : {self.title}")
        print(f"Description : {self.description}")
        print(f"Author      : {self.author}")
        print(f"URL         : {self.url}")
        print("-" * 50)


class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def get_news(self, country):
        params = {
            "country": country,
            "apiKey": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            data = response.json()

            if data["status"] == "ok":
                return data
            else:
                print("Error:", data["message"])
                return None

        except requests.exceptions.HTTPError as e:
            print("HTTP Error:", e)

        except requests.exceptions.ConnectionError:
            print("Connection Error! Check your internet connection.")

        except requests.exceptions.Timeout:
            print("Request Timed Out.")

        except requests.exceptions.RequestException as e:
            print("Request Error:", e)

        except Exception as e:
            print("Unexpected Error:", e)

        return None


# ---------------- MAIN PROGRAM ---------------- #

API_KEY = "3df9eff1116947939abc970481e90f0f"      # Replace with your API key

news = NewsAPI(API_KEY)

country = input("Enter country code (in, us, gb, ca, au): ").lower()

data = news.get_news(country)

if data:
    print("\nTop Headlines:\n")

    for item in data["articles"]:
        article = Article(
            item.get("title", "No Title"),
            item.get("description", "No Description"),
            item.get("author", "Unknown"),
            item.get("url", "No URL")
        )

        article.display()
else:
    print("No news available.")