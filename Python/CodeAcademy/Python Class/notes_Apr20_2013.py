"""
CODE ACADEMY NOTES APR 20 2013
"""

threes_and_fives = [x for x in range(1,16) if x%3 ==0 or x%5 ==0]
#above will create a list of numbers only divisible by 3 or 5 evenly
#first x can be also something like x**2

filter(lambda x: x != "X", list)
#This will fiter out anything in list that has X