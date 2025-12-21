import json
import os
from os.path import join
from pathlib import Path

from ujeebu_python import UjeebuClient

API_KEY = os.getenv("UJEEBU_API_KEY")
if not API_KEY:
    raise ValueError("Please set UJEEBU_API_KEY environment variable")
ujeebu = UjeebuClient(api_key=API_KEY, base_url="https://api.ujeebu.com")
url = "https://scrape.li/load-more"

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
