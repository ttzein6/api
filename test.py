import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"name": "tim","likes": 10,"views":10000},
#     {"name": "how to make mloukheye","likes": 10,"views":80000},
#     {"name": "joe","likes": 35,"views":35000}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE+"video/"+ str(i), data[i])
#     print(response.json())


response = requests.get(BASE + "video")
print(response.json())