# #### Running Sum of 1-D Array

# # Input = [3,1,2,10,1]
# # output = [3,4,6,16,17]
#  #solution 

# list = [3,1,2,10,1]
# new_list = []
# sum = 0
# for i in list:
#   sum += i
#   new_list.append(sum)
# print(new_list)


# # input = [3,4,6,16,17]
# # output = [3,1,2,10,1]

# def transform_list(input_list):
#     output_list = [input_list[0]]
#     for i in range(1, len(input_list)):
#         output_list.append(input_list[i] - input_list[i-1])
#     return output_list


# input_list = [3, 4, 6, 16, 17]
# output_list = transform_list(input_list)
# print(output_list)  # Output: [3, 1, 2, 10, 1]
##############################################################################################################################################

############# Richest Customer Wealth
##  Day2
# Input =  [[7,1,3],[2,8,7],[1,9,5]]
# output=  17

# account = [[7,1,3],[2,8,7],[1,9,5]]
# list = []
# for i in account:
#   list.append(sum(i))
# print(max(list))

# ### Input = 17
# ### Output = [[7,1,3],[2,8,7],[1,9,5]]

# a = 17
# b = [[7,1,3],[2,8,7],[1,9,5]]
# for j in b:
#   if sum(j) == a:
#     print(j)


#####
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 
# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]


# n = 3
# el = []
# a = "FizzBuzz"
# b = "Fizz"
# c = "Buzz"
# for i in range(1,n+1):
#     if i%3 == 0 and i%5 == 0:
#         # print("FizzBuzz")
#         el.append(a)
#     elif i%3 == 0:
#         # print("Fizz")
#         el.append(b)
#     elif i %5 == 0:
#         # print("Buzz")
#         el.append(c)
#     else:
#         el.append(str(i))

# print(str(el))

# #############  ANOTHER METHOD ############

# class Solution(object):
#     def fizzBuzz(self, n):
#         el = []
#         a = "FizzBuzz"
#         b = "Fizz"
#         c = "Buzz"
#         for i in range(1,n+1):
#             if i%3 == 0 and i%5 == 0:
#                 # print("FizzBuzz")
#                 el.append(a)
#             elif i%3 == 0:
#                 # print("Fizz")
#                 el.append(b)
#             elif i %5 == 0:
#                 # print("Buzz")
#                 el.append(c)
#             else:
#                 el.append(str(i))
#         return el
#     n = 3

###############################################################################################################################################
### Day 3

# def check_even_or_odd(n):
#     if n % 2 == 0:
#         print("Even")

#     else:
#         print("Odd")
# n = 0
# check_even_or_odd(n)

###########################################################################################################################################
# ### Day 4 
import math

# a = [1,2,3,4,5,6,7]
# b = len(a)
# c = []
# if len(a) % 2 != 0:
#     m = b/2
#     n = math.ceil(m)
#     o = a[n] - 1
#     for i in range(o,b+1):
#         c.append(i)
# else:
#     p = b/2
#     q = math.ceil(p)
#     r = a[q]
#     for i in range(r,b+1):
#         c.append(i)
# print(c)

########################## Vatsal Bro code ####
# lis = [1,2,3,4,5,6,7,8]
# l = len(lis)
# if l%2 == 0:
#     a = l//2 
# else:
#     a = l//2 
# print(lis[a:])


def calculate_mid_value(list):
    b = len(list)
    c = []
    if len(list) % 2 != 0:
        m = b/2
        n = math.ceil(m)
        o = list[n] - 1
        for i in range(o,b+1):
            c.append(i)
    else:
        p = b/2
        q = math.ceil(p)
        r = list[q]
        for i in range(r,b+1):
            c.append(i)
    return c

list = [1,2,3,4,5]

