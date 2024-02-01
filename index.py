# QUESTIONS:
# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):
# ..... 
def Hello(USERNAME):
    print(f'hello_{USERNAME}')
Hello('nate')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
# ..... 
def first_odds():
    for i in range(1, 100, 2):
        print(i)
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
# ..... 
max_num_in_list = lambda a_list: max(a_list) if a_list else 'not list silly'
#there were no restrictions on this one :) 
print(f"The maximum number in the list [5, 8, 2, 10, 3, 6] is: {max_num_in_list([5, 8, 2, 10, 3, 6])}")

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
# ..... 
def is_leap_year(a_year):
    return True if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0) else False
print(f"Is {2024} a leap year? {is_leap_year(2024)}")

# Question 5

# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
# .....
def is_consecutive(a_list):
    sorted_list = sorted(a_list)

    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 != sorted_list[i + 1]:
            return False
    return True
print(f"Is [2, 3, 4, 5, 6, 7] consecutive? {is_consecutive([2, 3, 4, 5, 6, 7])}")
# HOW TO SUBMIT:
# You will click the blue button that says add or create click link then paste the URL from the GitHub repository you created then click mark as done.