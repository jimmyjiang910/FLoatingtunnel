import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
#定义物理常量
g=9.81                                                      #重力加速度（m/s2）
pi=np.pi                                                    #圆周率
#定义变量
T=12                                                        #波浪周期（s）
w=2*pi/T                                                    #圆频率（rad）
d=100                                                       #静水深
#设置方程
def dispresion_eq(k):
    return g*k*np.tanh(k*d)-w**2
#提供猜测值
k_guess=w**2/g
#求解
k_solution=fsolve(dispresion_eq,k_guess)[0]
#输出结果
print("-"*30)
print(f"已知条件： 周期T={T}s,静水深d={d}m")
print(f"计算出的波数k={k_solution:.6f}rad/m")
L=2*pi/k_solution                                           #计算波长
print(f"对应、的波长为L={L}m")
#LL=2*pi/k_guess
#print(LL)                                                  #近似波长
print("-"*30)