from if_name_example import divide_numbers


# def divide_numbers(num, den):
#     try:
#         val = num/den
#         return val
#     except TypeError:
#         generic_err = "Numerator and Denominator must be numerics (float or int):\n"
#         data_err = f"numerator was {num} and denominator was {den}"

#         raise TypeError(generic_err + data_err)
    
#     # except ZeroDivisionError:
#     #     err = "Denominator must not be zero"
#     #     raise ZeroDivisionError(err)


class my_ratio:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self._validate_data()

    
    def _validate_data(self):
        list_of_valid_types = [int, float]
        if type(self.numerator) not in list_of_valid_types:
            raise TypeError("The numerator must be a numeric")
        if type(self.denominator) not in list_of_valid_types:
            raise TypeError("The denominator must be a numeric") 

        if self.denominator == 0:
            raise TypeError("The denominator must not be zero.")

    
    def value(self):
        return divide_numbers(self.numerator,self.denominator)

print(f"Howdy from {__name__}")
       
if __name__ == "__main__":
    numerator = 12
    denominator = 1
    a = my_ratio(numerator, denominator)
    print(a.value())