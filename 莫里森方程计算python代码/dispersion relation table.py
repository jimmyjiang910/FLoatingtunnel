import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# --- 解决 Matplotlib 画图时中文显示为方块的问题 ---
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体 (Windows系统适用)
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 1. 定义物理常数和已知变量
g = 9.81
pi = np.pi        # 直接使用 numpy 自带的 pi，更精确
T = 12.0          # 周期 (s)
w = 2 * pi / T    # 角频率 omega (rad/s)

# 2. 准备数据容器
# 使用 np.linspace 生成一个数组：从 10 到 100，均匀取 50 个点作为水深 d
depths = np.linspace(10, 100, 50)
# 创建一个空的列表（就像一个空盒子），用来装一会儿算出来的波长 L
wavelengths = []

# 3. 开始循环计算 (核心部分)
# 遍历 depths 里的每一个水深值，每次取出来的水深命名为 d
for d in depths:
    
    # 针对当前的水深 d，定义色散方程
    def dispersion_eq(k):
        return g * k * np.tanh(k * d) - w**2
    
    # 猜测值与求解
    k_guess = w**2 / g
    k_solution = fsolve(dispersion_eq, k_guess)[0]
    
    # 计算当前水深下的波长 L
    L = 2 * pi / k_solution
    
    # 把算好的波长 L 扔进刚才准备好的空盒子里
    wavelengths.append(L)

# 4. 开始画图！
plt.figure(figsize=(8, 5))  # 设置画布大小

# 画出 d 和 L 的关系曲线 (x轴是水深，y轴是波长)
plt.plot(depths, wavelengths, color='blue', linewidth=2, label=f'周期 T={T}s')

# 美化图表
plt.title('波长随水深的变化曲线 (浅水变深水)', fontsize=15)
plt.xlabel('水深 d (m)', fontsize=12)
plt.ylabel('波长 L (m)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) # 添加网格线
plt.legend() # 显示图例

# 弹出绘图窗口
plt.show()
