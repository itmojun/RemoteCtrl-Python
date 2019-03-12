from urllib import request
import time

while True:
    # 调用Web接口获取微信端发送的最新消息
    cmd = request.urlopen("http://api.itmojun.com/pc/cmd/get?id=dj").read()
    cmd = cmd.decode("gbk")  # 将gbk编码的bytes类型数据转换为str类型

    if cmd != "":
        print(cmd)
        time.sleep(3)  # 成功接收一条消息后间隔3秒再接收，避免接收到重复消息
    else:
        time.sleep(1)  # 没有接收到消息则间隔1秒再接收
