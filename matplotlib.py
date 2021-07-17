import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as colors
import math
import numpy as np 
plt.subplot(1,1,1)

x = np.array([1,2,3,4])
y1 = np.array([8566,6482,5335,7310])
y2 = np.array([4283,2667,3655,3241])

plt.bar(x,y1,width=0.3,label="任务量")
plt.bar(x+0.3,y2,width=0.3,label="完成量")   #x+0.3相当于完成量的每个柱子右移0.3

plt.title("全国各分区任务量",loc="center")

# 添加数据标签
for a,b in zip(x,y1):
    plt.text(a,b,b,ha='center',va="bottom",fontsize=12,color="blue")
    
    
for a,b in zip(x,y2):
    plt.text(a,b,b,ha='center',va="bottom",fontsize=12,color="r")
    
plt.xlabel('区域')
plt.ylabel('任务情况')

#设置x轴刻度值
plt.xticks(x+0.15,["东区","西区","南区","北区"])

plt.grid(False)
plt.legend()     #显示图例
