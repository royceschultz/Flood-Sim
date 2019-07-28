import numpy as np

def step(elevation, rain, distanceUnit, timeUnit):
    print(rain.sum())
    m,n = elevation.shape
    next = np.zeros((m,n))
    for i in range(1,m-1):
        for j in range(1,n-1):
            if rain[i][j] > 0:
                hHere = elevation[i][j] + rain[i][j]
                #top
                hThere = elevation[i+1][j] + rain[i+1][j]
                slope = (hHere-hThere)/distanceUnit
                if slope > 0:
                    flow = slope*rain[i][j]*timeUnit
                    next[i+1][j] += flow
                    next[i][j] -= flow
                #bottom
                hThere = elevation[i-1][j] + rain[i-1][j]
                slope = (hHere-hThere)/distanceUnit
                if slope > 0:
                    flow = slope*rain[i][j]*timeUnit
                    next[i-1][j] += flow
                    next[i][j] -= flow
                #left
                hThere = elevation[i][j-1] + rain[i][j-1]
                slope = (hHere-hThere)/distanceUnit
                if slope > 0:
                    flow = slope*rain[i][j]*timeUnit
                    next[i][j-1] += flow
                    next[i][j] -= flow
                #right
                hThere = elevation[i][j+1] + rain[i][j+1]
                slope = (hHere-hThere)/distanceUnit
                if slope > 0:
                    flow = slope*rain[i][j]*timeUnit
                    next[i][j+1] += flow
                    next[i][j] -= flow
    print(next.max())
    print(rain.max())
    rain += next
    print(rain.max())
    return rain
