from lxml import etree

text = '''
<div>
<ul>
        <li class="item1"><a href="#link1">Item 1</a></li>
        <li class="item1"><a href="#link2">Item 2</a></li>
        <li class="item1"><a href="#link3">Item 3</a></li>
        <li class="item"><a href="#link4">Item 3</a></li>
        <li class="item"><a href="#link5">Item 5</a></li>
    </ul>
    </div>
'''
html = etree.HTML(text)
# 查询a的值是Item 3的的元素
result = html.xpath('//li/a[text()="Item 3"]')
print(result)
# 查询所有a标签的值  ['Item 1', 'Item 2', 'Item 3', 'Item 3', 'Item 5']
result2 = html.xpath('//li/a/text()')
print(result2)
# 查询li的class属性是的item1的
result3 = html.xpath('//li[contains(@class,"item1")]')
print(result3)

# 查询a的值的包含Item 3的
result4 = html.xpath('//li/a[contains(text(),"Item 3")]')
print(result4)