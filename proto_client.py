import requests
from proto.p3 import FeedbackP3_pb2
from proto.p2 import FeedbackP2_pb2

# proto3
feedback3 = FeedbackP3_pb2.Feedback()
feedback3.life_cycle_id = 1
# feedback3.name = 'test'
# feedback3.gc_id = 'gcid'
# feedback3.gender = FeedbackP3_pb2.Gender.MALE
# feedback3.id = 'parkingLotId1'
# feedback3.parkingLotType = FeedbackP3_pb2.ParkingLotType.UNDERGROUND
# feedback3.ePay = True

# proto2
feedback2 = FeedbackP2_pb2.Feedback()
feedback2.life_cycle_id = 1
# feedback2.name = 'test'
# feedback2.gc_id = 'gcid'
# feedback2.gender = FeedbackP2_pb2.Gender.MALE
# feedback2.id = 'parkingLotId1'
# feedback2.parkingLotType = FeedbackP2_pb2.ParkingLotType.UNDERGROUND
# feedback2.ePay = True


# 默认值不参与序列化
print('P2\n', feedback2)
print(feedback2.SerializeToString)
print('P3\n', feedback3)

# p3 ->p3interface
response = requests.post("http://localhost:9999/feedbackPro3", headers={'Content-Type': 'application/x-protobuf'},
                          data=feedback3.SerializeToString())
assert response.status_code == 200

# p2 ->p2interface
response = requests.post("http://localhost:9999/feedbackPro2", headers={'Content-Type': 'application/x-protobuf'},
                          data=feedback2.SerializeToString())
assert response.status_code == 200

# p2 -> p3 interface server 升级

response = requests.post("http://localhost:9999/feedbackPro3", headers={'Content-Type': 'application/x-protobuf'},
                          data=feedback2.SerializeToString())
assert response.status_code == 200

# p3 -> p2 interface server 降级
response = requests.post("http://localhost:9999/feedbackPro2", headers={'Content-Type': 'application/x-protobuf'},
                          data=feedback3.SerializeToString())
assert response.status_code == 200


