import requests

from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def get_mobile(mobile):
    # url = 'https://ip138.com/mobile.asp?mobile=15566714700'
    url = f'https://www.haoshudi.com/{mobile}.htm'
    res = requests.get(url, headers=headers)

    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    table = html.xpath('//tr/td[2]/span/a/text()')
    print(table)


get_mobile('17097704477')

