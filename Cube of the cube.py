def cube(number):
    return number*number*number
def by_three(number):
    if number%3==0:
     return cube(number)
    else:
        return"Number is not a multiple of 3"
print(by_three(15))