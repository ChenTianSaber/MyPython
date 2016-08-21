import os
import time

def shutdown(seconds):
    print(str(seconds)+"秒后将会关机")
    time.sleep(seconds)
    print("关机啦！")
    os.system("shutdown -s -f -t 1")

def main():
    hour=input("请问你要多久后关机（小时数）:")
    print("收到："+str(hour))
    hour=float(hour)
    shutdown(hour*3600)

if __name__=='__main__':
    main()














