import json
from os.path import join
from pathlib import Path

from ujeebu_python import UjeebuClient

API_KEY = "__YOUR-API-KEY__"
ujeebu = UjeebuClient(api_key=API_KEY)
url = "https://ujeebu.com/docs/scrape-me/load-more"

response = ujeebu.scrape(url, {
    "response_type": "screenshot",
    "screenshot_fullpage": True,
    "js": True,
    # CSS selector to screenshot or coordinates of the rect to screenshot
    # screenshot_partial: {
    #     x: 0,
    #     y: 0,
    # },
    # If json is set the true the screenshot will be sent in base64 encoding
    "json": False,
    "wait_for": 4000,
    "block_ads": True,
})
if(response.status_code == 200):
    Path(join('examples', 'screenshot.png')).write_bytes(response.content)
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
