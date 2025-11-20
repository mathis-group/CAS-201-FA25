from random import shuffle

def split_l(this_l):
    n = len(this_l)
    left = int(n/2)
    
    return this_l[:left], this_l[left:]

def can_split(this_l):
    return len(this_l) > 1

def decompose_list(this_l):

    # d_lists = [[x] for x in this_l]
    d_lists = []
    for x in this_l:
        d_lists.append([x])

    return d_lists






def merge_sorted(left, right):
    # print(f"Merging {left} and {right}")
    merged_list = []
    # print(f"merged_list started as: {merged_list}")
    while (len(left) > 0) and (len(right) > 0):
        l = left[0]
        r = right[0]
        # print(f"l = {l}, and r = {r}")
        if l <= r:
            # print(f"{l} is less than (or equal to) {r}")
            merged_list.append(left.pop(0))
            # print(f"Merged list is now: {merged_list}")
        else:
            merged_list.append(right.pop(0))
            # print(f"{r} is less than {l}")
            # print(f"Merged list is now: {merged_list}")

            
    if len(right) > 0:
        merged_list.extend(right)
    
    elif len(left) > 0:
        merged_list.extend(left)

    return merged_list


def merge_sort(my_list):

    # n = len(my_list)
    decomposed_lists = decompose_list(my_list)

    while len(decomposed_lists) > 1:
        left = decomposed_lists.pop(0)
        right = decomposed_lists.pop(0)
        

        merged = merge_sorted(left, right)
        
        decomposed_lists.append(merged)
    return decomposed_lists[0]
    

def random_list(size):
    r = [x for x in range(size)]
    shuffle(r)
    return r

if __name__ == "__main__":

    r = random_list(100_000)
    # print(r)
    merge_sort(r)
    print('Sorted! ')