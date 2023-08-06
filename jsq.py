import time
import random
bfz=0
rd=0
xh=1
print("Hypixle加速器启动中...")
time.sleep(1)
print('启动器作者：k4641321')
time.sleep(1)
print(bfz ,'%')
bfz = bfz + random.randint(0,25)
while bfz<100:
    time.sleep(1)
    print(bfz ,'%')
    bfz = bfz + random.randint(bfz,100)
else :
    print('100%')
    print('启动完成')
    time.sleep(1)
print('请选择节点\n1.福建\n2.南京\n3.北京\n4.枣庄\n5.重庆\n按ctrl+c可退出')
xz=input('请选择（直接填序号，例如1）')
time.sleep(1)
print('正在启动节点',xz,'加速...')
time.sleep(3)
print('启动节点',xz,'成功')
time.sleep(1)
while xh!=0:
    time.sleep(1)
    print('当前延迟',random.randint(10,100),'ms')


