import requests
from proto.p2 import Feedback_pb2

feedback = Feedback_pb2.Feedback()

feedback.life_cycle_id = 1
feedback.name = 'test'
feedback.gc_id = 'gcid'
feedback.gender = Feedback_pb2.Gender.FEMALE
feedback.id = 'parkingLotId1'
feedback.parkingLotType = Feedback_pb2.ParkingLotType.UNDERGROUND
feedback.ePay = True

print(feedback)
response = requests.post("http://localhost:9999/feedbackPro", headers={'Content-Type': 'application/x-protobuf'},
                        data=feedback.SerializeToString())
print(response.url)  # 有返回，则URL已被正确编码
print(response.text)  # 推测的文本编码
print(response.content)  # 找到 （HTTP 和 XML自身可以指定编码格式）文本编码
print(response.encoding)  # 常用于中文乱码解决。用于修改编码方式（使用 codecs 模块进行注册）
