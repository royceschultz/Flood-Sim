import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.arange(0,10,.1)
y = np.arange(0,10,.1)

xs, ys = np.meshgrid(x, y)
# z = calculate_R(xs, ys)
zs = xs**2 + ys**2

print(zs.shape)

color_dimension = xs # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(color_dimension)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, facecolors=fcolors, vmin=minn, vmax=maxx, shade=True)
plt.show()
