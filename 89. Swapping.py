# 89. Write a Python program to swap two variables.

a = 10
b = 20
print(f"Before Swapping :-\n\ta = {a}\tb = {b}")
a = a+b
b = a-b
a = a-b
print(f"After Swapping :-\n\ta = {a}\tb = {b}")