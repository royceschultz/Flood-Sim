import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure()

def plot(z,color,minn,maxx):
    m,n = z.shape
    X = np.linspace(0,m,m)
    Y = np.linspace(0,n,n)
    x,y = np.meshgrid(X,Y)

    norm = matplotlib.colors.Normalize(minn, maxx)
    m = plt.cm.ScalarMappable(norm=norm, cmap='hot')
    m.set_array([])
    fcolors = m.to_rgba(color)

    ax = Axes3D(fig)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=fcolors, vmin=minn, vmax=maxx, shade=True)
    plt.show(block=False)
    plt.pause(.01)
