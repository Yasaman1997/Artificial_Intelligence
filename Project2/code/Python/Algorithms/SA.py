import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math


def f(x):
    x1 = x[0]
    x2 = x[1]
    object = x1 ** 2 + x2 ** 2 - 0.1 * math.cos(6.0 * 3.1415 * x1) - 0.1 * math.cos(6.0 * 3.1415 * x2) + 0.2
    return object


# Start location
x_start = [0.8, -0.5]

# Design variables at mesh points
T1 = np.arange(-1.0, 1.0, 0.01)
T2 = np.arange(-1.0, 1.0, 0.01)
meshgrid1, meshgrid2 = np.meshgrid(T1, T2)
fm = np.zeros(meshgrid1.shape)

for i in range(meshgrid1.shape[0]):
    for j in range(meshgrid1.shape[1]):
        fm[i][j] = meshgrid1[i][j] ** 2 + meshgrid2[i][j] ** 2 + 0.2 \
                   - 0.1 * math.cos(6.0 * 3.1415 * meshgrid1[i][j]) \
                   - 0.1 * math.cos(6.0 * 3.1415 * meshgrid2[i][j])

# plot
plt.figure()

# Plot contours
CS = plt.contour(meshgrid1, meshgrid2, fm)

# Label contours
plt.clabel(CS, inline=1, fontsize=10)

plt.title('Non-Convex Function')
plt.xlabel('x1')
plt.ylabel('x2')

##################################################
# Simulated Annealing
##################################################
# Number of cycles
n = 50
# Number of trials per cycle
m = 50
# Number of accepted solutions
na = 0.0
# Probability of accepting worse solution at the start
p1 = 0.7
# Probability of accepting worse solution at the end
p50 = 0.001
# Initial temperature
t1 = -1.0 / math.log(p1)
# Final temperature
t50 = -1.0 / math.log(p50)
# Fractional reduction every cycle
fraction = (t50 / t1) ** (1.0 / (n - 1.0))
# Initialize x
x = np.zeros((n + 1, 2))

x[0] = x_start

na = na + 1.0

# Current best results so far
xc = np.zeros(2)
xc = x[0]

xi = np.zeros(2)
xi = x_start

fc = f(xi)
fs = np.zeros(n + 1)
fs[0] = fc

# Current temperature
t = t1
# DeltaE Average
DeltaE_avg = 0.0
for i in range(n):
    print('Cycle: ' + str(i) + ' in Temperature: ' + str(t))
    for j in range(m):
        # Generate new trial points
        xi[0] = xc[0] + random.random() - 0.5
        xi[1] = xc[1] + random.random() - 0.5
        # Clip to upper and lower bounds
        xi[0] = max(min(xi[0], 1.0), -1.0)
        xi[1] = max(min(xi[1], 1.0), -1.0)
        DeltaE = abs(f(xi) - fc)
        if (f(xi) > fc):
            # Initialize DeltaE_avg if a worse solution was found
            #   on the first iteration
            if (i == 0 and j == 0): DeltaE_avg = DeltaE
            # objective function is worse
            # generate probability of acceptance
            p = math.exp(-DeltaE / (DeltaE_avg * t))
            # determine whether to accept worse point
            if (random.random() < p):
                # accept the worse solution
                accept = True
            else:
                # don't accept the worse solution
                accept = False
        else:
            # objective function is lower, automatically accept
            accept = True
        if (accept == True):
            # update currently accepted solution
            xc[0] = xi[0]
            xc[1] = xi[1]
            fc = f(xc)
            # increment number of accepted solutions
            na = na + 1.0
            # update DeltaE_avg
            DeltaE_avg = (DeltaE_avg * (na - 1.0) + DeltaE) / na

    # Record the best x values at the end of every cycle
    x[i + 1][0] = xc[0]
    x[i + 1][1] = xc[1]
    fs[i + 1] = fc

    # Lower the temperature for next cycle
    t = fraction * t

# print solution
print('Best solution: ' + str(xc))
print('Best objective: ' + str(fc))

plt.plot(x[:, 0], x[:, 1], 'y-o')
plt.savefig('overview.png')

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(fs, 'r.-')
ax1.legend(['Objective'])
ax2 = fig.add_subplot(212)
ax2.plot(x[:, 0], 'b.-')
ax2.plot(x[:, 1], 'g--')
ax2.legend(['x1', 'x2'])

# Save the figure as a PNG
plt.savefig('finalIterations.png')

plt.show()
