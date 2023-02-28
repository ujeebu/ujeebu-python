import json

from ujeebu_python import UjeebuClient
API_KEY = "__YOUR-API-KEY__"
ujeebu = UjeebuClient(api_key=API_KEY)

url = "https://ujeebu.com/blog/scraping-javascript-heavy-pages-using-puppeteer/"
response = ujeebu.extract(url=url)
if(response.status_code == 200):
    result = response.json()
    print(json.dumps(result['article'], indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
