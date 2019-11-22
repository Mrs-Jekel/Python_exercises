# def manual_exponent(base_num, pow_num):
#     result = 1
#     for index in range(pow_num): 
#         result = result * base_num 
#     return result

# print(manual_exponent(3, 4))
# print(manual_exponent(9, 20))

from functools import reduce

"""
manual_exponent(2,3)
#> 8

manual_exponent(10,2)
#> 100
"""
"""
# def manual_exponent(num, exp):
#     counter = exp -1       created a counter variable -1 takes one away (2 x 2 x 2)
#     total = num

#     while counter > 0:
#         total *= num   this will give a product same as total * num
#         counter -= 1   take the counter and decrement it counter is equal to minus 1

#     return total 

# print(manual_exponent(2,3))
# print(manual_exponent(10,2))
#----Functional approach below---------------------------------------------------------------------------
# lambda = an function without a name anonyanous function-takes in total and element
reduce iterates over a list and then runs whatever process you tell it to run,
in this case its the lambda function- and keeps the state. 

to understand Reduce https://bottega.devcamp.com/full-stack-development-javascript-python/guide/1689
"""
def manual_exponent(num, exp):
    computed_list = [num] * exp   
    return (reduce(lambda total, element: total * element, computed_list))


print(manual_exponent(2,3))
print(manual_exponent(10,2)) 
