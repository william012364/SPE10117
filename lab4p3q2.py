'''
Algorithm maxMin
An algorithm program to read three number A, B, and C and 
prints the largest value and the smallest value.

1. Read A, B, C

2.1 if A > B
    then largest <- A
    else largest <- B
2.2 if C > largest 
    then largest <- C

3.1 if A < B
    then smallest <- A
    else smallest <- B
3.2 if C < smallest 
    then smallest <- C

4. Output largest, smallest
'''
#1. Read A, B, C

A = int(input('enter A: '))  # read A
B = int(input('enter B: '))  # read B
C = int(input('enter C: '))  # read C
'''
if A > B:
    largest = A
else:
    largest = B 

if C > largest:
    largest = C

if A < B:
    smallest = A
else:
    smallest = B

if C < smallest: 
    smallest = C
'''

list = []
list.append(A)
list.append(B)
list.append(C)
largest = max(list)
smallest = min(list)
    
print('the largest number is %5d, and the smallest number is %5d'%(largest,smallest))
