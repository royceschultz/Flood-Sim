import plot
import simulate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

x = np.arange(-5,4,.4)
y = np.arange(-4,5,.4)
xs, ys = np.meshgrid(x, y)
# z = calculate_R(xs, ys)
zs = np.cos(xs) + np.cos(ys)
#zs = xs**2 + ys**2

minn, maxx = xs.min(), xs.max()

m,n = zs.shape
color = 0.5*np.ones((m,n))
minn, maxx = 0,1.5

fig = plt.figure()
plot.plot(zs,color,minn,maxx,0)

for i in range(100):
    print(i)
    color = simulate.step(zs,color,1,.2)
    plot.plot(zs,color,minn,maxx,i+1)
