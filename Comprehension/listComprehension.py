### [表达式 for 变量 in 可迭代对象 if 条件]

# 生成0-9的平方数
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

squares = [i ** 2 for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 只保留偶数
evens = []
for i in range(20):
    if i % 2 == 0:
        evens.append(i)

evens = [i for i in range(20) if i % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# 生成坐标对
coords = []
for x in range(3):
    for y in range(3):
        coords.append((x, y))

coords = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]


# 字符串处理
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD', 'PYTHON']

first_letters = [word[0] for word in words]
# ['h', 'w', 'p']