import numpy as np

def make_array(n_rows, n_columns):
    # Make the entries for each row
    ps = np.arange(n_columns)
    # Initialize an empty 2D array
    data_arr = np.zeros((n_rows, n_columns))
    # Fill the array with rows
    for i in range(n_rows):
        for j in range(n_columns):
            data_arr[i, j] = ps[j]

    return data_arr
 
if __name__ == "__main__":
    my_data_arr = make_array(4,5)
    print(f"my_data_arr is : \n {my_data_arr}")