import json
from pathlib import Path

from ujeebu_python import UjeebuClient

API_KEY = "__YOUR-API-KEY__"
ujeebu = UjeebuClient(api_key=API_KEY)
url = "https://ujeebu.com/docs/scrape-me/load-more"

response = ujeebu.scrape(url=url, params={
    "wait_for": 5000,
    "block_resources": 0,
    "js": 1,
    "extract_rules": {
        "products": {
            "selector": ".product-card",
            "type": "obj",
            "multiple": 1,
            "children": {
                "name": {
                    "selector": ".title",
                    "type": "text"
                },
                "description": {
                    "selector": ".description",
                    "type": "text"
                },
                "price": {
                    "selector": ".price",
                    "type": "text"
                },
                "image": {
                    "selector": ".card__image > img",
                    "type": "image",
                }
            }
        }
    }
})
if(response.status_code == 200):
    print(json.dumps(response.json(), indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
