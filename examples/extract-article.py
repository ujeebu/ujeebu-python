import json

from ujeebu_python import UjeebuClient
API_KEY = "__YOUR-API-KEY__"
ujeebu = UjeebuClient(api_key=API_KEY)

url = "https://thenextweb.com/news/european-space-agency-unveils-new-plan-for-growing-plants-on-the-moon"

response = ujeebu.extract(url=url, params={
    "js": True
})
if(response.status_code == 200):
    result = response.json()
    print(json.dumps(result['article'], indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
