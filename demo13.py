person = {
    'name': "tot",
    'age': 10
}
print(person['name'])  # tot 方法1
print(person.get("age"))  # 10  方法2

person["add"] = "dalian"
print(person)  # 新增  {'name': 'tot', 'age': 10, 'add': 'dalian'}

print("name" in person)  # True
print("name" not in person)  # False

del person["age"]
print(person)  # 删除 {'name': 'tot', 'add': 'dalian'}

person["name"] = "nike"
print(person)  # 修改  {'name': 'nike', 'add': 'dalian'}

# keys() 获取字典中所有的key;value() 获取字典中所有的value;items()  获取字典中所有的key(),value()

keys = person.keys()
print(keys)  # dict_keys(['name', 'add'])
print(list(keys))  # ['name', 'add']

values = person.values()
print(values)  # dict_values(['nike', 'dalian'])
print(list(values))  # ['nike', 'dalian']

items = person.items()
print(items)  # dict_items([('name', 'nike'), ('add', 'dalian')])
print(list(items))  # [('name', 'nike'), ('add', 'dalian')]

person2 = {
    'name': "tot",
    'age': 10
}
for item in person2:
    print(item)  # 遍历KEY name age
    print(person2[item])  # 遍历value  tot  10
