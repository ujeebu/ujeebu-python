# Ujeebu API Python SDK
[Ujeebu](https://ujeebu.com) is a set of powerful APIs for Web data scraping and automatic content extraction. This SDK provides an easy-to-use interface for interacting with Ujeebu API. It is built on top of Node.js and uses the [axios](https://axios-http.com/) library to make HTTP requests.

## Installation
You can install the SDK using pip:
```shell
pip install ujeebu_python
```


## Usage
To use the SDK, you first need to create an instance of it with your API credentials:
```python
from ujeebu_python import UjeebuClient
import json
ujeebu = UjeebuClient(api_key="__YOUR-API-KEY__")
url = "https://ujeebu.com/blog/scraping-javascript-heavy-pages-using-puppeteer/"
response = ujeebu.extract(url=url)
if(response.status_code == 200):
    result = response.json()
    print(json.dumps(result['article'], indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
```

##  APIs
The SDK provides the following methods:
- `scrape(url, params, headers)`
    - `url`: The url to scrape (required).
    - `params`: Dict of [scrape API params](https://ujeebu.com/docs/scrape#parameters) (optional).
    - `headers`: Dict of headers to forward (optional).


- `extract(url, params, headers)`
    - `url`: The url to extract (required).
    - `params`: Dict of [extract API params](https://ujeebu.com/docs/extract#parameters) (optional).
    - `headers`: Dict of headers to forward (optional).


- `preview(url, params, headers)`
    - `url`: The url to extract (required).
    - `params`: Dicto of [preview API params](https://ujeebu.com/docs/extract#parameters-1) (optional).
    - `headers`: Dicto of headers to forward (optional).


#### Examples
- Example to scrape html of URL with infinite scroll
```python
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
```

- Example to take a screenshot of URL
```python
url = "https://ujeebu.com/docs/scrape-me/load-more";

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
    # from pathlib import Path
    Path('screenshot.png').write_bytes(response.content)
else:
    print("Error:\n", json.dumps(response.json(), indent=2))
```


- Example of extracting list of products from a page
```python
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
```

- Example of extracting main body of an article
```python
url = "https://thenextweb.com/news/european-space-agency-unveils-new-plan-for-growing-plants-on-the-moon"

response = ujeebu.extract(url=url, params={
    "js": True
})
if(response.status_code == 200):
    result = response.json()
    print(json.dumps(result['article'], indent=2))
else:
    print("Error:\n", json.dumps(response.json(), indent=2))

```


## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This library is licensed under the MIT License. See the LICENSE file for more information.

## Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) project template.
