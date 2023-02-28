import json

from ujeebu_python import UjeebuClient

API_KEY = "__YOUR-API-KEY__"
ujeebu = UjeebuClient(api_key=API_KEY)

url = "https://ujeebu.com/docs/scrape-me/load-more"
response = ujeebu.scrape(url, params={
    # define what to extract 'raw', 'html', 'screenshot' or 'pdf'
    "response_type": "dddd",

    # return response in json format or
    "json": False,
    # user-agent header to forward
    "useragent": "Ujeebu-Node",

    # cookies to forward
    "cookies": {"Cookie1": "Cookie Value"},

    # execute js
    "js": True,

    # wait for selector or time in ms
    "wait_for": ".products-list",

    # if the selector doesn't appear in 5000ms, ignore and continue
    "wait_for_timeout": 5000,

    # scroll the page down
    "scroll_down": True,

    # wait 2000ms between two scrolls
    "scroll_wait": 2000,

    # scroll to this element in each scroll
    "scroll_to_selector": ".load-more-section",

    # scroll condition. while this is true the page will continue to perform more scrolls
    "scroll_callback": "() => (document.querySelector('.no-more-products') === null)",

    "proxy_type": "premium",

    # proxy country code
    "proxy_country": "US",

    # device type "desktop" or "mobile"
    "device": "desktop",

    "window_width": 1200,

    "window_height": 900,

    "block_ads": True,

    "block_resources": True,
}, headers={
    # forwarded headers
    "Authorization": "Basic eWSjaW5lnlhY4luZUdxMDE2"
})
if(response.status_code == 200):
    print(response.content)
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
