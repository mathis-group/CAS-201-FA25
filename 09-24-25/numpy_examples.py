import numpy as np
import time

py_list = [1 for x in range(10)]
#py_2D_list = [[1 for x in range(10)] for y in range(10) ]
# print(py_2D_list)

np_arr = np.arange(10)
#print(np_arr)

np_ones = np.ones((10,10))

np_ones[0,0] = 100
# print(np_ones)



# Example comparison

py_list = [x for x in range(1,101)]
another_list = [y for y in range(201, 301)]
sum_list = []

for i in range(len(py_list)):
    val = py_list[i] + another_list[i]
    sum_list.append(val)

# print(py_list)
# print(another_list)

# print(sum_list)


# Using numpy

np_arr = np.arange(1,101)
another_arr = np.arange(201,301)

sum_arr = np_arr + another_arr
# print(sum_arr)


# # Python implementation
# N = 100000
# py_list = [x for x in range(N)]
# another_list = [y for y in range(N)]
# sum_list = []
# start_time = time.time()
# for i in range(len(py_list)):
#     val = py_list[i] + another_list[i]
#     sum_list.append(val)

# end_time = time.time()
# print(f"Python Runtime: {end_time - start_time}")

# # Python implementation
# N = 100000
# np_arr = np.arange(N)
# another_arr = np.arange(N) 

# start_time = time.time()
# sum_arr = np_arr + another_arr

# end_time = time.time()
# print(f"NumPy Runtime: {end_time - start_time}")

# # Polynomials
# my_poly = np.polynomial.Polynomial([1,2,3])
# print(my_poly)
# print(my_poly.roots())


# An example of confusing arrays
one_matrix = np.zeros((3,3)) + np.eye((3))
one_matrix[2,0] = 1.0
two_arr = np.array([1,2,3])

print(one_matrix)
print(two_arr)

print(one_matrix * two_arr)