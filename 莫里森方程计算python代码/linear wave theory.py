import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
#定义物理常量
pi=np.pi
#定义变量
H=15                                     #波高（m）
T=12                                     #周期（s）
k=0.028148                               #波数：由色散关系得出（rad/m）
L=2*pi/k                                 #波长
w=2*pi/T                                 #圆频率
z=-30                                    #管道中心水深
d=100                                    #静水深
#求速度和加速度最大值
u_max=pi*H*np.cosh(k*(z+d))/(T*np.sinh(k*d))
a_max=2*(pi**2)*H*np.cosh(k*(z+d))/((T**2)*np.sinh(k*d))
#输出
print("-"*30)
print(f"流体速度最大值u_max={u_max}m/s")
print(f"流体加速度最大值a_max={a_max}m/s^2")
print("-"*30)