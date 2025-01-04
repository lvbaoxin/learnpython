import json

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 音乐列表的URL
list_url = "https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1728642413777&mid=9311f60bac20e69a9f601fac41df82bf&uuid=9311f60bac20e69a9f601fac41df82bf&dfid=34br5N4EQeYc1JPJV13Tnpp4&keyword=%E5%88%80%E9%83%8E&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=19aabba126576aa910777b117479f83e"

# 音乐信息的URL
info_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1728642502472&mid=9311f60bac20e69a9f601fac41df82bf&uuid=9311f60bac20e69a9f601fac41df82bf&dfid=34br5N4EQeYc1JPJV13Tnpp4&appid=1014&platid=4&encode_album_audio_id=12e7yw9e&token=&userid=0&signature=7e29f8b15e88d7f55eaf89ed25d95773"

# 音乐MP3的URL
mp3_url = "https://webfs.kugou.com/202410111726/de12b5e8cb17768ed02ce087ed4a5a20/v3/b261b8fc3a14082a3883ac13b7dbe320/yp/p_0_960125/ap1014_us0_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx568185746_s1714556545.mp3"

list_res = requests.get(list_url, headers=headers)

hash_list = json.loads(list_res.text[12:-2])['data']['lists']
# 原地址加密了
info_res = requests.get(info_url, headers=headers)
print(info_res.json()['data']['play_url'])

# 一首歌的下载
# m_res = requests.get(mp3_url, headers=headers)
# with open('test.mp3', 'wb') as f:
#     f.write(m_res.content)

for i, s in enumerate(hash_list):
    print(s.get("SongName"), s.get("FileHash"))
    print(info_res.json()['data']['play_url'])
    m_res = requests.get(info_res.json()['data']['play_url'], headers=headers)

    with open('{}.mp3'.format(s.get("SongName")), 'wb') as f:
        f.write(m_res.content)
