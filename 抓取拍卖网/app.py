import json

import requests
from lxml import etree

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = "https://fz.51pmf.cn/home/indexb/webhlist?aaaa=bbbb&type=1&focurlist=W10%3D&state=2&sortby=1&mode=0&pi=5&q=&salt=1729049157&sign=5A255195%40%40"

params = {
    "aaaa": "bbbb",
    "type": 1,
    "focurlist": "W10=",
    "state": 2,
    "sortby": 1,
    "mode": 0,
    "pi": 1,
    "q": "",
    "salt": 1729049157,
    "sign": "5A255195@@",
}
pages = [1,2,3]
for i in pages:
    params['pi'] = i
    try:
        # Use params instead of data
        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()  # Raise an error for bad responses

        # Load the JSON response
        html = res.json()

        # Check if 'data' is present in the response
        if 'data' in html:
            for index, v in enumerate(html['data']):
                print(f"Page {i}, Item {index + 1}: fzID = {v['fzID']}")
        else:
            print(f"Page {i} has no data.")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for page {i}: {e}")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON response for page {i}.")
