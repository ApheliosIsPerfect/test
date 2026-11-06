try:
    with open('myfile.txt') as f:
        s = f.readline()
        i = int(s.strip())
        print(f"读取到的数字是: {i}")
except FileNotFoundError:
    print("文件不存在")
except ValueError:
    print("文件内容不是有效的数字")