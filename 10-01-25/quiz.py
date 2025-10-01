import numpy as np

my_arr = np.array([0,1,2,3,4,5])

my_arr[0] += my_arr[5]

print(f"my_arr[0] is now {my_arr[0]}")
n = my_arr[5]
print(f"n is now {n}")
for i in range(n):
    my_arr += my_arr
    print(f"After iteration {i} my_arr is now {my_arr}")

print(f"The final value of my_arr at the zero-th index is {my_arr[0]}")