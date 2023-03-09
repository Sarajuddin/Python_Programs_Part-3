# 81. Write a Python program to test whether all numbers of a list is greater than a certain number.

lst = [12, 56, 21, 6, 7, 8, 9, 45]

num = 50

for el in lst:
    if el > num:
        pass
    else:
        print("All numbers in a container are not greater than {}".format(num))
        break
else:
    print("All numbers are greater.")