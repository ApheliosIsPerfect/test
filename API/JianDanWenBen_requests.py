import requests

# 设置apikey和url
api_key = "sk-ws-H.YHXYDDI.XP2Y.MEQCIFWTMraXMWLo8W1H0B-3U6HsPKIQ9exkPNS2Y1cY12YcAiBfcd3S9T4wm3HuJKCH71ObuvfI1kJ_4E27rmVIi0SUjg"
base_url = "https://ws-ji0i895p4rymg7s3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"

#设置请求头 相当于其他补充信息 
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


# 构造要发送的数据体cl
data = {
    "model": "qwen3.8-max",  # 模型名称看官方文档
    "messages": [
        {"role": "system", "content": "你是一个专业助手，回答简洁清晰"},
        {"role": "user", "content": "用python写一个快速排序"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
}


#发送post请求
resp = requests.post(base_url, headers=headers, json=data)

#解析服务器返回的json数据
res_json = resp.json()

#检验请求是否成功
if resp.status_code == 200:
    answer = res_json["choices"][0]["message"]["content"]
    print("大模型返回：")
    print(answer)
else:
    print("请求失败：", res_json)
