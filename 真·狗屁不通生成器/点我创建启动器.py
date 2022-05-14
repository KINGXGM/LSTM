import os

path = os.getcwd()

with open("点我创建神经网络生成器.bat","w",encoding="utf-8") as file:
file.write("@echo off\necho [32m\n")
    file.write(path[0:2]+"\n")
    file.write("python main.py\necho [0m\n")
    file.write("pause")
with open("点我测试神经网络.bat","w",encoding="utf-8") as file:
    file.write("@echo off\necho [32m\n")
    file.write(path[0:2]+"\n")
    file.write("python main2.py\necho [0m")

print("启动器修改完毕>>>")
