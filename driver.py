import plot
import simulate
import numpy as np

x = np.arange(0,10,.2)
y = np.arange(0,10,.2)
xs, ys = np.meshgrid(x, y)
# z = calculate_R(xs, ys)
zs = np.sin(xs) + np.sin(ys)
zs = xs**2 + ys**2

minn, maxx = xs.min(), xs.max()


m,n = zs.shape
color = np.ones((m,n))
minn, maxx = 0,2

plot.plot(zs,color,minn,maxx)

for i in range(100):
    print(i)
    xs = simulate.step(zs,color,1,0.1)
    plot.plot(zs,color,minn,maxx)
