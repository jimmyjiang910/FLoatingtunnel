import numpy as np
#定义变量
dens=1025
D=12
Cm=2.0
Cd=1.0
pi=np.pi
a_max=0.9041573343025038
u_max=1.7268133090444173
#求惯性力和阻力(每米隧道受到的力)
FI_max=dens*Cm*pi*((D/2)**2)*a_max
FD_max=0.5*dens*Cd*D*(u_max**2)
#输出惯性力与阻力
print("-"*30)
print(f"管道每米受到的最大惯性力为FI_max={FI_max}N/m")
print(f"管道每米受到的最大阻力为FD_max={FD_max}N/m")
print("-"*30)