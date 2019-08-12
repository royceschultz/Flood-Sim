import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D



def plot(z,color,minn,maxx,i,angle):
    fig = plt.figure()
    m,n = z.shape
    X = np.linspace(0,m,m)
    Y = np.linspace(0,n,n)
    x,y = np.meshgrid(X,Y)

    norm = matplotlib.colors.Normalize(minn, maxx)
    m = plt.cm.ScalarMappable(norm=norm, cmap='ocean')
    m.set_array([])
    fcolors = m.to_rgba(color)

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=fcolors, vmin=minn, vmax=maxx, shade=True)
    ax.title.set_text('Elevation map')
    ax.view_init(30, angle)
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_zlabel('Elevation')

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.plot_surface(x, y, z+color, rstride=1, cstride=1, facecolors=fcolors, vmin=minn, vmax=maxx, shade=True)
    ax.title.set_text('Elevation + Rain Level')
    ax.view_init(30,angle)
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_zlabel('Elevation')
    ax.set_zlim3d(-1,2)

    fig.savefig('PlotFrameImgs/'+str(i))
    plt.close(fig)
