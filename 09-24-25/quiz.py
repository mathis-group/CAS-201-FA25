def quiz():

    a = 6
    b = 3
    my_list = [x for x in range(a)]
    print(f"my_list is: {my_list}")
    b += my_list[3]
    print(f"The new value of b is {b}")

    print("Start iterating through list")
    for x in my_list:
        print(f" The current x is {x}")
        if b > x:
            print("b is more than x")
            b -= x
            print(f"b is now {b}")
        
        else:
            print("b is not more than x")
            a += 1
            print(f"a is now {a}")
    
    print(f"The final value of a is {a}")
    print(f"The final value of b is {b}")


if __name__ == "__main__":       
    quiz()