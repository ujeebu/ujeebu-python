import json
from os.path import join
from pathlib import Path

from ujeebu_python import UjeebuClient
API_KEY = "__YOUR-API-KEY__"
ujeebu = UjeebuClient(api_key=API_KEY)

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
