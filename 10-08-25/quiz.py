""" This is a quiz. """

import numpy as np

TOP = 8 # Defines the top of the box
BOTTOM = 0 # Defines the bottom of the box
V = 2 # Defines the initial velocity
Y0 = 4 # Defines the inital value of y. 

time_steps = 10
ys = np.zeros(time_steps)
time = np.arange(time_steps) # Make an array that stores time
print(f"ys is {ys}")
print(f"time is {time}")

ys[0] = Y0
print(f"ys is now {ys}")

# Iterate over each time steps and change the position based
# on the current position and the current velocity.
for t in range(1,time_steps):
    last_y = ys[t-1]
    print(f"t is {t}, last_y is {last_y}, and v is {v}")
    if (last_y + v) > top:
        # Ball hit the top, flip direction 
        v = -v
    elif (last_y + v) < bottom:
        # Ball hit the bottom, flip direction
        v = -v 
    print(f"ys[t] is {ys[t]}")
    ys[t] = last_y + v

    input("Press enter to continue")

print(f"The time series for ys is {ys}")
