### {键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}

d = {"a": 1, "b": 2, "c": 3}
# 直接遍历字典，拿到的是键
result = {key: key.upper() for key in d}
print(result)  
# {'a': 'A', 'b': 'B', 'c': 'C'}


d = {"a": 1, "b": 2, "c": 3}
# 用 .values() 遍历值
result = {value: value * 10 for value in d.values()}
print(result)  
# {1: 10, 2: 20, 3: 30}


d = {"a": 1, "b": 2, "c": 3}
# 用 .items() 遍历，拿到的是元组 (键, 值)
result = {item: item[0].upper() + str(item[1]) for item in d.items()}
print(result)  
# {('a', 1): 'A1', ('b', 2): 'B2', ('c', 3): 'C3'}

d = {"a": 1, "b": 2, "c": 3}
# 拆包：key 拿第一个元素，value 拿第二个元素
result = {value: key for key, value in d.items()}
print(result)  
# {1: 'a', 2: 'b', 3: 'c'}