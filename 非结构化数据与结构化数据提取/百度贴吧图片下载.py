import requests
from lxml import etree

# 先requests拿到网页的源代码数据
# 通过lxml对源代码进行解析，拿到图片的URL地址
# 依次对图片地址发送网络请求
# 保存图片
# index_url = 'https://tieba.baidu.com/p/8538075744'
#
# res = requests.get(index_url).text
#
# html = etree.HTML(res)
#
# images_url = html.xpath('//img[@class="BDE_Image"]/@src')
# offset = 0
# for image_url in images_url:
#     image_content = requests.get(image_url).content
#     with open('{}.jpg'.format(offset), 'wb') as f:
#         f.write(image_content)
#     offset = offset + 1
