import numpy as np

def step(elevation, rain, distanceUnit, timeUnit):
    print('water capacity:' + str(rain.sum()))
    m,n = elevation.shape
    next = np.zeros((m,n))
    for i in range(0,m):
        for j in range(0,n):
            if rain[i][j] > 0:
                hHere = elevation[i][j] + rain[i][j]
                if i+1 < m: #top
                    hThere = elevation[i+1][j] + rain[i+1][j]
                    slope = (hHere-hThere)/distanceUnit
                    if slope > 0:
                        flow = slope*rain[i][j]*timeUnit
                        next[i+1][j] += flow
                        next[i][j] -= flow
                if i-1 >= 0: #bottom
                    hThere = elevation[i-1][j] + rain[i-1][j]
                    slope = (hHere-hThere)/distanceUnit
                    if slope > 0:
                        flow = slope*rain[i][j]*timeUnit
                        next[i-1][j] += flow
                        next[i][j] -= flow
                if j-1 >= 0: #left
                    hThere = elevation[i][j-1] + rain[i][j-1]
                    slope = (hHere-hThere)/distanceUnit
                    if slope > 0:
                        flow = slope*rain[i][j]*timeUnit
                        next[i][j-1] += flow
                        next[i][j] -= flow
                if j+1 < n: #right
                    hThere = elevation[i][j+1] + rain[i][j+1]
                    slope = (hHere-hThere)/distanceUnit
                    if slope > 0:
                        flow = slope*rain[i][j]*timeUnit
                        next[i][j+1] += flow
                        next[i][j] -= flow
    print('max flow this step:' + str(next.max()))
    print('max rain depth:' + str(rain.max()))
    rain += next
    del next #save the memory
    return rain
