import copy

# 嵌套列表：外层列表，里面还套了一个子列表
a = [1, 2, [3, 4]]
b = copy.copy(a)  # 浅拷贝

print(id(a), id(b)) # ✅ 外层id不一样，外层是新列表
print(id(a[2]), id(b[2])) # ⚠️ 里面嵌套的子列表 id 完全一样！同一个对象

# 修改外层元素
a[0] = 999
print("a=", a)
print("b=", b)
# b不受影响，因为修改的是外层

# 修改嵌套里面的子列表！
a[2].append(5)
print("a=", a)
print("b=", b)
# ❗ b里面的子列表也变了！因为共用同一个 [3,4]
