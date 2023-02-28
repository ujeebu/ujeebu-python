import json
import urllib

import requests


class UjeebuClient:
    def __init__(self, api_key=None):
        if not api_key:
            raise ValueError("api_key is required")
        self.base_url = 'https://api.ujeebu.com'
        self.api_key = api_key

    def extract(self, url, params={}, headers=None):
        headers = headers or {}
        has_raw_html = None
        if 'raw_html' in params:
            has_raw_html = len(params['raw_html']) > 0

        headers = self.handle_headers(headers)

        if has_raw_html:
            headers['apiKey'] = self.api_key
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            return requests.post(self.base_url + '/extract', data={
                **params,
                **{
                    "url": url,
                }
            }, headers={
                **headers,
                **{"user-agent": "Ujeebu-Python/1.0.0"}
            })

        params = self.handle_ujeebu_params({
            **{"url": url},
            **params
        })
        return requests.get(self.base_url + '/extract', params={
            **params,
            **{"apiKey": self.api_key}
        }, headers={
            **headers,
            **{"user-agent": "Ujeebu-Python/1.0.0"}
        })

    def scrape(self, url, params={}, headers=None):
        headers = headers or {}

        has_extract_rules = False
        if 'extract_rules' in params:
            has_extract_rules = bool(params['extract_rules'])

        headers = self.handle_headers(headers)
        if has_extract_rules:
            return requests.post(self.base_url + '/scrape', data=json.dumps({
                **{"url": url},
                **params
            }), headers={
                **{
                    "apiKey": self.api_key,
                    "user-agent": "Ujeebu-Python/1.0.0",
                    "Content-Type": "application/json"
                },
                **headers
            })

        params = self.handle_ujeebu_params({
            **{"url": url, "apikey": self.api_key},
            **params
        })
        return requests.get(self.base_url + '/scrape', params=params, headers={
            **headers,
            **{"user-agent": "Ujeebu-Python/1.0.0"}
        })

    def preview(self, url, params={}, headers=None):
        headers = headers or {}
        headers = self.handle_headers(headers)
        params = self.handle_ujeebu_params({
            **params,
            **{
                "url": url,
                "apikey": self.api_key
            }
        })
        return requests.get(self.base_url + '/card', params=params, headers={
            **headers,
            **{"user-agent": "Ujeebu-Python/1.0.0"}
        })

    @staticmethod
    def handle_url(url):
        return url
        # return urllib.parse.quote_plus(url)

    @staticmethod
    def handle_custom_js(js):
        return urllib.parse.quote_plus(js)
        # return base64.b64encode(s.encode()).decode()

    @staticmethod
    def handle_headers(headers):
        if headers is None:
            return None
        return {f'Ujb-{k}': v for k, v in headers.items()}

    @staticmethod
    def handle_cookies(cookies):
        if cookies is None:
            return None
        if isinstance(cookies, dict):
            stringified_cookies = ';'.join(f'{k}={v}' for k, v in cookies.items())
            return urllib.parse.quote(stringified_cookies)
        elif isinstance(cookies, list):
            # Ujeebu only supports name=value cookies ATM
            raise NotImplementedError
        elif isinstance(cookies, str):
            return cookies

    @classmethod
    def handle_ujeebu_params(cls, params):
        new_params = {}
        for k, v in params.items():
            if v in (None, '', [], {}):
                new_params[k] = v
            elif k == 'url':
                new_params[k] = cls.handle_url(v)
            elif k == 'custom_js':
                new_params[k] = cls.handle_custom_js(v)
            elif k == 'cookies':
                new_params[k] = cls.handle_cookies(v)
            else:
                new_params[k] = v
        return new_params
