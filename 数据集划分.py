import os
import random
path1=r'C:\Users\16609\Desktop\greenorange.v15i.yolov5pytorch - 副本\train\images'
path2=r'C:\Users\16609\Desktop\greenorange.v15i.yolov5pytorch - 副本\train\labels'


for j in range(int(0.3*326)):
    list=os.listdir(path1)
    shanchuduixiang=random.choice(list)
    print(shanchuduixiang)
    shanchuduixiang2=shanchuduixiang.replace('.jpg','.txt')
    os.remove(path1+'\\'+shanchuduixiang)
    os.remove(path2 + '\\' + shanchuduixiang2)
print(len(path1))
