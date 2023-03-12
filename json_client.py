import requests

payload = {'lifeCycleId': 1, 'name': 'test', 'gcId': 'gcid-1', 'gender': 0,  'id': 'parkingLotId1',
           'parkingLotType': 1, 'ePay': True}

response = requests.post("http://localhost:9999/feedbackJson", headers={'Content-Type': 'application/json'},
                         json=payload)
print(response.url)  # 有返回，则URL已被正确编码
print(response.text)  # 推测的文本编码
print(response.content)  # 找到 （HTTP 和 XML自身可以指定编码格式）文本编码
print(response.encoding)  # 常用于中文乱码解决。用于修改编码方式（使用 codecs 模块进行注册）
