import pandas as pd

# Make an example dataframe
my_data = [{"a":4, "b":2, "c":1}, {"a":2, "b":0, "c":-1}]

my_df = pd.DataFrame(my_data)

print(my_df.head())
### 


# Make an empty list to store all the lists
my_lists = []
# Iterate over the rows, and make a list out of each row
for i, row in my_df.iterrows():
    my_list = row.to_list()
    my_lists.append(my_list)
# Make a new column out of the lists of lists. 
my_df["quad_arr"] = my_lists

# print(my_df)