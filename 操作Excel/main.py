import pandas as pd

data = pd.read_excel('excel.xlsx', dtype={'联系人电话': str})

arr = ['年份', '国家', '类型']

for index, value in enumerate(arr):
    data[value] = data['type'].astype(str).apply(
        lambda x: x.split("/")[index].strip() if len(x.split("/")) > index else None)
writer = pd.ExcelWriter('temp.xlsx')
# data.to_excel(writer, sheet_name='原始数据')

# 根据年限分割
for i in data['年份'].unique():
    data[data['年份'] == i].to_excel(writer, sheet_name=i)
writer.close()
