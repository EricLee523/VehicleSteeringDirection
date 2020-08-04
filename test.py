import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
file=open('trajectories.pickle','rb')
a_dict1=pickle.load(file)
df = pd.DataFrame(a_dict1)
sli=df.loc[ :,['pos_x','pos_y']]
plt.figure('trajectories')
for i in range(100):
    posx=sli.iloc[i,0]
    posy=sli.iloc[i,1]

    # first point
    preX1 = sli.iloc[i, 0][0]
    preY1 = sli.iloc[i, 1][0]
    # second point
    preX2 = sli.iloc[i, 0][2]
    preY2 = sli.iloc[i, 1][2]

    size = len(sli.iloc[i, 0])
    # thrid point
    postX1 = sli.iloc[i, 0][size - 3]
    postY1 = sli.iloc[i, 1][size - 3]
    # last point
    postX2 = sli.iloc[i, 0][-1]
    postY2 = sli.iloc[i, 1][-1]

    #转换成从0到360连续的角度
    preAngle = math.atan2(preY2-preY1, preX2-preX1)
    preAngle = 180 - math.degrees(preAngle)
    postAngle = math.atan2(postY2-postY1, postX2-postX1)
    postAngle = 180 - math.degrees(postAngle)

    #直行
    if (math.fabs(preAngle-postAngle) < 45 or math.fabs(360 - math.fabs(preAngle-postAngle))<45):
        print("直行")
        plt.xlim(-30, 35)
        plt.ylim(-25, 35)
        plt.xlabel('position x')
        plt.ylabel('position y')
        new_ticks1 = np.linspace(-30, 35, 14)
        plt.xticks(new_ticks1)
        new_ticks2 = np.linspace(-25, 35, 13)
        plt.yticks(new_ticks2)
        plt.plot(posx, posy, 'b-')

    #右转
    if (45 < postAngle - preAngle < 162 or 45 < 360 - preAngle + postAngle < 162):
        print("右转")
        plt.xlim(-30,35)
        plt.ylim(-25,35)
        plt.xlabel('position x')
        plt.ylabel('position y')
        new_ticks1=np.linspace(-30,35,14)
        plt.xticks(new_ticks1)
        new_ticks2=np.linspace(-25,35,13)
        plt.yticks(new_ticks2)
        plt.plot(posx,posy,'r-')

    #左转
    if (45 < preAngle - postAngle < 162 or 45 < 360 - postAngle + preAngle < 162):
        print("左转")
        plt.xlim(-30, 35)
        plt.ylim(-25, 35)
        plt.xlabel('position x')
        plt.ylabel('position y')
        new_ticks1 = np.linspace(-30, 35, 14)
        plt.xticks(new_ticks1)
        new_ticks2 = np.linspace(-25, 35, 13)
        plt.yticks(new_ticks2)
        plt.plot(posx, posy, 'g-')

    # 掉头
    if (math.fabs(math.fabs(preAngle - postAngle) - 180) < 18 ):
        print("左转")
        plt.xlim(-30, 35)
        plt.ylim(-25, 35)
        plt.xlabel('position x')
        plt.ylabel('position y')
        new_ticks1 = np.linspace(-30, 35, 14)
        plt.xticks(new_ticks1)
        new_ticks2 = np.linspace(-25, 35, 13)
        plt.yticks(new_ticks2)
        plt.plot(posx, posy, 'k-')

plt.show()




