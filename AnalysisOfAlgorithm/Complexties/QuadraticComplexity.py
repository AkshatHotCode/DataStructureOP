#---------------------------Quadratic Complexity---------------------------
"""The complexity of an algorithm is said to be quadratic when the steps required to execute an algorithm are quadratic function of the number of item in the input.
Quadratic complexity is denoted as O(n^2)"""

def quadratic_algorithm(items):
    for i in items:
        for a in items:
            print(i, " ", a)

quadratic_algorithm([11, 14, 26])

#We have an outer loop that iterates through all the items in the list in the input list and then a nested inner loop, which again iterates thorugh all the items in the input list.
#The total number of steps performed is n*n, where n is the number of items in the input array.

