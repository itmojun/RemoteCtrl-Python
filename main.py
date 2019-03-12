from urllib import request
import time
import os
import pygame

pygame.mixer.init()
pygame.mixer.music.load("bg.mp3")

while True:
    # 调用Web接口获取微信端发送的最新消息
    cmd = request.urlopen("http://api.itmojun.com/pc/cmd/get?id=dj").read()
    cmd = cmd.decode("gbk")  # 将gbk编码的bytes类型数据转换为str类型

    if cmd != "":
        print(cmd)

        if "关机" in cmd:
            # os.system("shutdown -s -t 0")
            pass  # 空语句，啥也不做，只是为了满足语法规则
        elif "重启" in cmd:
            # os.system("shutdown -r -t 0")
            pass
        elif "网站" in cmd:
            os.system("explorer https://itmojun.com")
        elif "播放 " in cmd:
            pygame.mixer.music.play()
        elif "暂停" in cmd:
            pygame.mixer.music.pause()
        elif "停止" in cmd:
            pygame.mixer.stop()

        time.sleep(3)  # 成功接收一条消息后间隔3秒再接收，避免接收到重复消息
    else:
        time.sleep(1)  # 没有接收到消息则间隔1秒再接收
