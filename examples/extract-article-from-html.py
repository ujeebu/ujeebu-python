import json
import os
from os.path import join
from pathlib import Path

from ujeebu_python import UjeebuClient
API_KEY = os.getenv("UJEEBU_API_KEY")
if not API_KEY:
    raise ValueError("Please set UJEEBU_API_KEY environment variable")
ujeebu = UjeebuClient(api_key=API_KEY, base_url="https://api.ujeebu.com")

url = "https://thenextweb.com/news/european-space-agency-unveils-new-plan-for-growing-plants-on-the-moon"
raw_html = Path(join('examples', 'page.html')).read_text('utf8')
response = ujeebu.extract(url=url, params={
    "raw_html": raw_html
})
if(response.status_code == 200):
    result = response.json()
    print(json.dumps(result['article'], indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
