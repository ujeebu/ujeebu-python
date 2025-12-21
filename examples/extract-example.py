import json
import os

from ujeebu_python import UjeebuClient
API_KEY = os.getenv("UJEEBU_API_KEY")
if not API_KEY:
    raise ValueError("Please set UJEEBU_API_KEY environment variable")
ujeebu = UjeebuClient(api_key=API_KEY, base_url="https://api.ujeebu.com")

url = "https://ujeebu.com/blog/scraping-javascript-heavy-pages-using-puppeteer/"
response = ujeebu.extract(url=url)
if(response.status_code == 200):
    result = response.json()
    print(json.dumps(result['article'], indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
