import os  # 导入OS库 
print("请确定你的python运行版本低于python3.9或在Windows使用v1.0版本")
os.system('ls')  # 检查文件
print("请检查是否有requirements.txt文件, 如没有请重新选择运行目录")
def continue_execution():
    while True:
        user_input = input("是否继续执行？(y/n) [默认 y]: ").strip().lower()
        if user_input == '' or user_input == 'y':
            return True
        elif user_input == 'n':
            print("程序已结束。")
            return False
        else:
            print("无效输入，请输入 y 或 n。")

# 判断输入
if __name__ == "__main__":
    if continue_execution():
        # 继续执行后续代码
        print("继续运行")
        os.system('pip3 install --upgrade pip')
        os.system('pip3 install -r ./requirements.txt')
    else:
        # 结束程序
        exit()
