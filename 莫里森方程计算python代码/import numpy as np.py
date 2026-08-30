import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#定义物理常量
g=9.81                                                      #重力加速度（m/s2）
pi=np.pi                                                    #圆周率

#定义变量
T=12                                                        #波浪周期（s）
w=2*pi/T                                                    #圆频率（rad）
d=100                                                       #静水深(m)
H=15                                                        #波高（m）
z=-30                                                       #管道中心水深（m）
dens=1025                                                   #海水密度（kg/m^3）
D=12                                                        #管体直径(m)
Cm=2.0                                                      #惯性系数
Cd=1.0                                                      #阻力系数

#一，色散关系求波长和波数

#设置方程
def dispresion_eq(k):
    return g*k*np.tanh(k*d)-w**2
#提供猜测值
k_guess=w**2/g
#求解
k_solution=fsolve(dispresion_eq,k_guess)[0]
L=2*pi/k_solution                                           #计算波长

#二，线性波理论求流体质点最大加速度和速度
u_max=pi*H*np.cosh(k_solution*(z+d))/(T*np.sinh(k_solution*d))
a_max=2*(pi**2)*H*np.cosh(k_solution*(z+d))/((T**2)*np.sinh(k_solution*d))

#三，求惯性力和阻力(每米隧道受到的力)
FI_max=dens*Cm*pi*((D/2)**2)*a_max
FD_max=0.5*dens*Cd*D*u_max*abs(u_max)

#四，输出结果
print("-"*30)
print("1.色散关系求波长和波数")
print(f"已知条件： 周期T={T}s,静水深d={d}m")
print(f"计算出的波数k={k_solution:.6f}rad/m")
print(f"对应的波长为L={L}m")
print("2.线性波理论求流体最大加速度和速度")
print(f"流体速度最大值u_max={u_max}m/s")
print(f"流体加速度最大值a_max={a_max}m/s^2")
print("3.莫里森方程求管体收到的最大惯性力和阻力")
print(f"管道每米受到的最大惯性力为FI_max={FI_max}N/m")
print(f"管道每米受到的最大阻力为FD_max={FD_max}N/m")
print("-"*30)
# ==========================================
# 五，双自变量动态分析与图表绘制 (时间序列 vs 空间序列)
# ==========================================

# --- 解决中文显示问题 ---
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ---------------------------------------------------
# 情景 1: 随【时间 t】变化 (固定位置 x=0)
# ---------------------------------------------------
x_fixed = 0
# 生成时间数组 t: 0 到 2个周期，200个点
t_arr = np.linspace(0, 2 * T, 200)
phase_t = k_solution * x_fixed - w * t_arr  # 相位 theta = kx - wt

# 计算速度和加速度 (时间序列)
u_t = u_max * np.cos(phase_t)
a_t = a_max * np.sin(phase_t)

# 计算力 (时间序列)
FI_t = dens * Cm * pi * ((D/2)**2) * a_t
FD_t = 0.5 * dens * Cd * D * u_t * np.abs(u_t) # 注意阻力方向 u*|u|
F_total_t = FI_t + FD_t

# ---------------------------------------------------
# 情景 2: 随【空间位置 x】变化 (固定时间 t=0)
# ---------------------------------------------------
t_fixed = 0
# 生成空间数组 x: 0 到 2个波长，200个点
x_arr = np.linspace(0, 2 * L, 200)
phase_x = k_solution * x_arr - w * t_fixed  # 相位 theta = kx - wt

# 计算速度和加速度 (空间序列)
u_x = u_max * np.cos(phase_x)
a_x = a_max * np.sin(phase_x)

# 计算力 (空间序列)
FI_x = dens * Cm * pi * ((D/2)**2) * a_x
FD_x = 0.5 * dens * Cd * D * u_x * np.abs(u_x)
F_total_x = FI_x + FD_x

# ---------------------------------------------------
# 开始绘制双子图 (1个窗口，上下2张图)
# ---------------------------------------------------
# 创建画布和子图：2行1列，共享相同的画布尺寸
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# --- 绘制图1：时间历程图 (ax1) ---
ax1.plot(t_arr, FI_t / 1000, label='惯性力 $F_I$', color='blue', linestyle='--')
ax1.plot(t_arr, FD_t / 1000, label='阻力 $F_D$', color='green', linestyle='-.')
ax1.plot(t_arr, F_total_t / 1000, label='总力 $F_{total}$', color='red', linewidth=2)

ax1.set_title(f'时间历程图: 固定位置 x={x_fixed}m (水深 d={d}m)', fontsize=14)
ax1.set_xlabel('时间 t (s)', fontsize=12)
ax1.set_ylabel('受力 (kN/m)', fontsize=12)
ax1.axhline(0, color='black', linewidth=1)
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend(loc='upper right') # 将图例固定在右上角

# --- 绘制图2：空间波形图 (ax2) ---
ax2.plot(x_arr, FI_x / 1000, label='惯性力 $F_I$', color='blue', linestyle='--')
ax2.plot(x_arr, FD_x / 1000, label='阻力 $F_D$', color='green', linestyle='-.')
ax2.plot(x_arr, F_total_x / 1000, label='总力 $F_{total}$', color='red', linewidth=2)

ax2.set_title(f'空间波形图: 固定时间 t={t_fixed}s (管心深度 z={z}m)', fontsize=14)
ax2.set_xlabel('水平位置 x (m)', fontsize=12)
ax2.set_ylabel('受力 (kN/m)', fontsize=12)
ax2.axhline(0, color='black', linewidth=1)
ax2.grid(True, linestyle=':', alpha=0.7)
ax2.legend(loc='upper right')

# 调整两张图的间距，防止文字重叠
plt.tight_layout()

# 终极展示！
plt.show()
