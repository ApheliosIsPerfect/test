### (表达式 for 变量 in 可迭代对象 if 条件)
### 和列表推导式的区别：圆括号，而且惰性求值（用的时候才算）

# 列表推导式：一次性算出所有结果，占用内存
squares_list = [i**2 for i in range(1000000)]   # 立刻占内存

# 生成器表达式：边用边算，不占内存
squares_gen = (i**2 for i in range(1000000))    # 几乎不占内存

# 使用时一样
for num in squares_gen:
    print(num)
    if num > 100:
        break
