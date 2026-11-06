### {表达式 for 变量 in 可迭代对象 if 条件}

# 去重
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers}
# {1, 4, 9, 16, 25}  ← 自动去重，且无序

# 过滤
words = ["apple", "banana", "cherry", "date"]
vowel_start = {word for word in words if word[0] in "aeiou"}
# {'apple'}  ← 只有 apple 以元音开头

